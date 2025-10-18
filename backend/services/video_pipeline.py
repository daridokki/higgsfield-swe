class VideoPipeline:
    def __init__(self, higgsfield_client: HiggsfieldClient):
        self.client = higgsfield_client
        
    async def create_music_video(self, scene_prompts: List[Dict], 
                               music_analysis: Dict) -> List[str]:
        """Execute the complete video generation pipeline"""
        generated_clips = []
        
        for i, scene in enumerate(scene_prompts):
            print(f"Generating scene {i+1}/{len(scene_prompts)}")
            
            # Step 1: Generate background image
            image_url = await self.client.generate_image(scene['image_prompt'])
            
            # Step 2: Animate the image with music-synced motion
            video_prompt = self._enhance_with_music_cues(
                scene['video_prompt'], music_analysis, i
            )
            video_url = await self.client.animate_image(image_url, video_prompt)
            
            generated_clips.append(video_url)
            
            # Step 3: (Optional) Create special beat-drop moments
            if i == len(scene_prompts) // 2:  # Middle scene for climax
                special_prompt = self._create_special_moment_prompt(music_analysis)
                special_video = await self.client.generate_direct_video(special_prompt)
                generated_clips.append(special_video)
        
        return generated_clips
    
    def _enhance_with_music_cues(self, base_prompt: str, 
                               analysis: Dict, scene_index: int) -> str:
        """Add music-specific motion descriptions to prompt"""
        tempo = analysis['tempo']
        energy = analysis['energy']
        
        motion_intensity = "gentle" if tempo < 90 else "dynamic" if tempo < 130 else "intense"
        
        return f"{base_prompt}, {motion_intensity} motion synced to {tempo}BPM music, {energy} energy level"