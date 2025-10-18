# 🚀 SonicCanvas Deployment Guide

This guide will help you deploy your Music-to-Video Generator to production.

## 📋 Prerequisites

- GitHub account
- Vercel account (free)
- Railway account (free tier available)
- Your Higgsfield API credentials

## 🎯 Deployment Strategy

**Frontend (Next.js)**: Vercel
**Backend (Flask)**: Railway

---

## Step 1: Prepare GitHub Repository

1. **Initialize Git** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: SonicCanvas Music-to-Video Generator"
   ```

2. **Create GitHub Repository**:
   - Go to [GitHub](https://github.com)
   - Click "New repository"
   - Name it: `soniccanvas-music-video`
   - Make it **Public** (required for SWE Track)
   - Don't initialize with README (you already have one)

3. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/soniccanvas-music-video.git
   git branch -M main
   git push -u origin main
   ```

---

## Step 2: Deploy Backend to Railway

### Option A: Railway CLI (Recommended)

1. **Install Railway CLI**:
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway**:
   ```bash
   railway login
   ```

3. **Deploy Backend**:
   ```bash
   cd backend
   railway init
   railway up
   ```

4. **Set Environment Variables**:
   ```bash
   railway variables set HIGGSFIELD_API_KEY="your_api_key_here"
   railway variables set HIGGSFIELD_API_SECRET="your_api_secret_here"
   railway variables set ENVIRONMENT="production"
   ```

### Option B: Railway Web Interface

1. Go to [Railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Select the `backend` folder
6. Add environment variables in Settings

**Environment Variables to Set**:
```
HIGGSFIELD_API_KEY=7f3a2ee6-aeb6-4dc7-bd70-a9c01e841b0c
HIGGSFIELD_API_SECRET=e5d0fdb10e97f43dfcee9031d78ec1ef28e254c20c817010c60050b67f9459eb
ENVIRONMENT=production
```

### Get Backend URL
After deployment, Railway will give you a URL like:
`https://soniccanvas-backend-production.up.railway.app`

---

## Step 3: Deploy Frontend to Vercel

### Option A: Vercel CLI (Recommended)

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Deploy Frontend**:
   ```bash
   cd frontend
   vercel
   ```

3. **Set Environment Variables**:
   ```bash
   vercel env add NEXT_PUBLIC_API_URL
   # Enter your Railway backend URL
   ```

### Option B: Vercel Web Interface

1. Go to [Vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Set Root Directory to `frontend`
5. Add Environment Variable:
   - Name: `NEXT_PUBLIC_API_URL`
   - Value: Your Railway backend URL

---

## Step 4: Update CORS Settings

1. **Get your Vercel URL** (e.g., `https://soniccanvas-frontend.vercel.app`)

2. **Update Backend CORS**:
   - Go to your Railway project
   - Edit the environment variables
   - Add: `FRONTEND_URL=https://your-vercel-url.vercel.app`

3. **Update Flask CORS**:
   ```bash
   # In backend/app_flask.py, update line 18:
   'https://your-vercel-url.vercel.app'
   ```

4. **Redeploy Backend**:
   ```bash
   railway up
   ```

---

## Step 5: Test Your Deployment

1. **Test Backend**: Visit `https://your-railway-url.up.railway.app/health`
2. **Test Frontend**: Visit your Vercel URL
3. **Test Full Flow**: Upload an audio file and generate a video

---

## 🎯 Final URLs

After deployment, you'll have:
- **Frontend**: `https://soniccanvas-frontend.vercel.app`
- **Backend**: `https://soniccanvas-backend.up.railway.app`

---

## 🚨 Troubleshooting

### Common Issues:

1. **CORS Errors**:
   - Make sure your frontend URL is added to backend CORS origins
   - Check that environment variables are set correctly

2. **API Connection Issues**:
   - Verify `NEXT_PUBLIC_API_URL` is set in Vercel
   - Check that backend is running (visit `/health` endpoint)

3. **File Upload Issues**:
   - Check file size limits (50MB max)
   - Verify file type restrictions

4. **Higgsfield API Issues**:
   - Verify API credentials are set correctly
   - Check API rate limits and quotas

### Debug Commands:

```bash
# Check Railway logs
railway logs

# Check Vercel deployment status
vercel ls

# Test backend locally
cd backend && python app_flask.py
```

---

## ✅ Success Checklist

- [ ] GitHub repository is public
- [ ] Backend deployed to Railway with working health endpoint
- [ ] Frontend deployed to Vercel
- [ ] Environment variables configured
- [ ] CORS settings updated
- [ ] Full music-to-video flow working
- [ ] Both URLs accessible from browser

---

## 🎬 Recording Demo Video

1. Go to [Loom.com](https://loom.com)
2. Record your screen showing:
   - Uploading an audio file
   - Music analysis results
   - Video generation process
   - Final generated videos
3. Keep it under 5 minutes
4. Show the working deployed application

---

## 🏆 Submission Ready!

Once all steps are complete, your project will be:
- ✅ Deployed and accessible
- ✅ Production-ready and stable
- ✅ Feature-complete for real use
- ✅ Reliable and testable under real conditions

Perfect for the SWE Track submission! 🚀
