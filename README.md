# ICMS Chatbot Flask Application

This is a Flask-based chatbot application that provides information about the Integrated City Management System (ICMS) using Google's Gemini AI.

## Features

- Web-based chat interface for easy interaction
- RESTful API endpoint for asking questions about ICMS
- Integration with Google Gemini AI for intelligent responses
- Comprehensive ICMS context and information

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

You need to get a Gemini API key from Google AI Studio:
1. Go to https://makersuite.google.com/app/apikey
2. Create a new API key
3. Create a `.env` file in the project root and add:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

### 3. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## Usage

### Web Interface

1. Open your browser and go to `http://localhost:5000`
2. You'll see a chat interface where you can ask questions about ICMS
3. Type your question and press Enter or click Send

### API Usage

#### Endpoint: `/ask_icms`

**Method:** POST  
**Content-Type:** application/json

**Request Body:**
```json
{
    "question": "What is the ICMS system?"
}
```

**Response:**
```json
{
    "answer": "The Integrated City Management System (ICMS) is a unified platform designed to enhance communication, service delivery, and engagement between city residents and local authorities..."
}
```

## Example Usage

### Using the Web Interface
Simply visit `http://localhost:5000` and start chatting!

### Using curl:
```bash
curl -X POST http://localhost:5000/ask_icms \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the key subsystems of ICMS?"}'
```

### Using Python:
```python
import requests

response = requests.post('http://localhost:5000/ask_icms', 
                        json={'question': 'What is ICMS?'})
print(response.json()['answer'])
```

## Project Structure

- `app.py` - Main Flask application
- `templates/index.html` - Web chat interface
- `requirements.txt` - Python dependencies
- `README.md` - This file

## ICMS Information

The chatbot is trained on information about:
- Project overview and objectives
- Key subsystems (Government Tasks Website, City Chat App, Citizen Social Media Platform, Public Services Website)
- Benefits for citizens, city officials, and community

## Troubleshooting

1. **API Key Error**: Make sure you've set up your `.env` file with the correct Gemini API key
2. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
3. **Port Already in Use**: Change the port in `app.py` or stop other applications using port 5000 