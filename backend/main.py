from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="BeatVisualizer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://your-vercel-app.vercel.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/analyze")
async def analyze_music(file: UploadFile):
    """Analyze uploaded music file"""
    if not file.content_type.startswith('audio/'):
        raise HTTPException(400, "File must be audio")
    
    # Save temporary file
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())
    
    # Analyze music
    analyzer = AudioAnalyzer()
    analysis = analyzer.analyze_track(temp_path)
    
    return {
        "analysis": analysis,
        "scene_plan": prompt_generator.generate_scene_prompts(analysis)
    }

@app.post("/api/generate")
async def generate_video(analysis: Dict, scene_plan: List[Dict]):
    """Generate complete music video"""
    pipeline = VideoPipeline(higgsfield_client)
    video_clips = await pipeline.create_music_video(scene_plan, analysis)
    
    # Combine clips (using moviepy or similar)
    final_video = await combine_video_clips(video_clips, analysis)
    
    return {
        "video_url": final_video,
        "scene_clips": video_clips,
        "analysis": analysis
    }