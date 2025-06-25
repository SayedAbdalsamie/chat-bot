from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables (will use GitHub secrets in production)
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure your Gemini API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Warning: GEMINI_API_KEY not found in environment variables")
    print("Make sure to set it in your deployment platform's environment variables")
    api_key = "NOT_SET"

genai.configure(api_key=api_key)

# Load Gemini model
model = None
try:
    if api_key != "NOT_SET":
        # Try the correct model name
        model = genai.GenerativeModel("gemini-1.5-flash")
        print("Successfully loaded gemini-1.5-flash model")
    else:
        print("API key not set - model will not be available")
except Exception as e:
    print(f"Error loading gemini-1.5-flash model: {e}")
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        print("Successfully loaded gemini-1.5-pro model")
    except Exception as e2:
        print(f"Error loading gemini-1.5-pro model: {e2}")
        try:
            model = genai.GenerativeModel("gemini-pro")
            print("Successfully loaded gemini-pro model")
        except Exception as e3:
            print(f"Error loading gemini-pro model: {e3}")
            model = None

# ICMS context (with citations removed)
ICMS_CONTEXT = """
You are an AI assistant providing information about the Integrated City Management System (ICMS).

Project Overview:
- The Integrated City Management System (ICMS) is a unified platform designed to enhance communication, service delivery, and engagement between city residents and local authorities.
- The system simplifies government interactions, improves city infrastructure management, and fosters community interaction through a range of digital services.
- By providing a centralized solution for accessing government services, reporting issues, booking public services, and participating in local discussions, ICMS promotes a smart, efficient, and transparent city management system.
- The objective of ICMS is to simplify the interaction between residents and services.
- The core idea is a digital platform that centralizes government tasks, city navigation, infrastructure maintenance, and social interaction.
- The target audience includes city residents, government, and service providers.

Key Subsystems:
- Government Tasks Website: A centralized web portal for citizens to access services like tax payments, permits, and appointments. Features include citizen ID-based login, integrated payment system, and document download/verification. Impact is streamlined government processes for better efficiency.
- City Chat App: A real-time app to report city issues (electrical, plumbing) and track their resolution. Features include AI bot categorization of problems, task assignment to departments, and AI-based problem resolution suggestions. This leads to faster response and issue resolution. It also allows booking services like garbage collection and park maintenance.
- Citizen Social Media Platform: A platform for citizens to post updates, plan events, and engage in local discussions. Features include user-generated content and event management. Public/private posts enable secure communication and community engagement.
- Public Services Website: Allows booking services like garbage collection and park maintenance. It includes automatic notifications for scheduled services, service feedback, and real-time tracking of requested services.

Key Benefits for Citizens: Simplified city management, easy access to services, better communication.
Key Benefits for City Officials: Efficient tracking, real-time updates, data-driven decision-making.
Key Benefits for Community: Engagement through social media, better local interaction.
"""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask_icms", methods=["POST"])
def ask_icms():
    try:
        # Get user question from the request
        data = request.get_json()
        question = data.get("question", "").strip()

        if not question:
            return jsonify({"error": "No question provided"}), 400

        # Check if API key is configured
        if not api_key or api_key == "NOT_SET":
            return (
                jsonify(
                    {
                        "error": "GEMINI_API_KEY not configured. Please set it in environment variables."
                    }
                ),
                500,
            )

        # Check if model is loaded
        if model is None:
            return (
                jsonify(
                    {
                        "error": "Gemini model not available. Please check your API key and model configuration."
                    }
                ),
                500,
            )

        # Construct prompt
        prompt = f"{ICMS_CONTEXT}\n\nUser's Question: {question}\n\nProvide a direct and helpful answer about ICMS. Do not start with phrases like 'Based on the provided information' or similar. Give a natural, conversational response."

        # Send prompt to Gemini
        response = model.generate_content(prompt)
        answer = response.text

        return jsonify({"answer": answer})

    except Exception as e:
        print(f"Error in ask_icms: {str(e)}")
        return jsonify({"error": f"API Error: {str(e)}"}), 500


# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
