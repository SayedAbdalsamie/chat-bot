# Deploy with GitHub Environment Secrets

You've already set up your GitHub environment secrets! Here's how to deploy your API using them.

## ✅ What You've Already Done:

1. **Created Environment**: `env`
2. **Added Secret**: `GEMINI_API_KEY` with your actual API key
3. **Repository is private** (secure)

## 🚀 Deploy Options:

### Option 1: Render (Recommended - Easy)

1. **Go to**: https://render.com/
2. **Sign up with GitHub**
3. **Click "New +"** → "Web Service"
4. **Connect your repository**: `SayedAbdalsamie/chat-bot`
5. **Configure**:
   - **Name**: `chat-bot-api`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
6. **Add Environment Variable**:
   - **Key**: `GEMINI_API_KEY`
   - **Value**: Your actual Gemini API key (same as in GitHub secrets)
7. **Click "Create Web Service"**

### Option 2: Railway (Also Easy)

1. **Go to**: https://railway.app/
2. **Sign up with GitHub**
3. **Click "New Project"** → "Deploy from GitHub repo"
4. **Select your repository**
5. **Add Environment Variable**:
   - **Key**: `GEMINI_API_KEY`
   - **Value**: Your actual Gemini API key
6. **Deploy automatically**

### Option 3: Heroku (Advanced)

1. **Install Heroku CLI**
2. **Login**: `heroku login`
3. **Create app**: `heroku create your-app-name`
4. **Set environment variable**:
   ```bash
   heroku config:set GEMINI_API_KEY=your_actual_api_key
   ```
5. **Deploy**: `git push heroku main`

## 🔐 Security Features:

✅ **Private repository** - Only you can see the code
✅ **Environment secrets** - API key is secure
✅ **No debug mode** - Production ready
✅ **HTTPS enabled** - Secure connections

## 📝 Important Notes:

- **Use the same API key** that you put in GitHub secrets
- **Don't commit the .env file** - It's in .gitignore
- **Your API will be private** - Only you can access it
- **Monitor usage** - Check your Gemini API usage

## 🧪 Test Your Deployed API:

Once deployed, test with:

```bash
curl -X POST https://your-app-url.com/ask_icms \
  -H "Content-Type: application/json" \
  -d '{"question": "What is ICMS?"}'
```

Your API will be completely private and secure! 🎉 