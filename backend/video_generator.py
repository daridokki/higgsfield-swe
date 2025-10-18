from music_analyzer import MusicAnalyzer
from higgsfield_client import HiggsfieldClient
from credit_manager import CreditManager
from config import Config
import os

class VideoGenerator:
    def __init__(self):
        self.music_analyzer = MusicAnalyzer()
        self.api_client = HiggsfieldClient(
            Config.HIGGSFIELD_API_KEY,
            Config.HIGGSFIELD_API_SECRET
        )
        self.credit_manager = CreditManager(Config.TOTAL_BUDGET)
    
    def create_video_from_music(self, audio_file_path):
        """
        Main function: Turn music into video
        """
        print("🎵 Step 1: Analyzing music...")
        music_analysis = self.music_analyzer.analyze_music(audio_file_path)
        print(f"   Analysis: {music_analysis['tempo']} BPM, {music_analysis['mood']}, energy: {music_analysis['energy']:.2f}")
        
        print("🎬 Step 2: Planning video scenes...")
        scene_plan = self._plan_video_scenes(music_analysis)
        
        print("✨ Step 3: Generating video content...")
        video_urls = self._generate_video_content(scene_plan, music_analysis)
        
        return {
            'music_analysis': music_analysis,
            'video_urls': video_urls,
            'budget_used': self.credit_manager.used_budget,
            'budget_remaining': self.credit_manager.get_remaining_budget()
        }
    
    def _plan_video_scenes(self, music_analysis):
        """Create video plan based on music characteristics"""
        tempo = music_analysis['tempo']
        mood = music_analysis['mood']
        
        if mood == "energetic":
            return {
                'style': 'cyberpunk',
                'scenes': [
                    {
                        'image_prompt': 'cyberpunk city with neon lights, vibrant colors, futuristic, detailed',
                        'video_prompt': f'neon lights pulsing to fast {tempo} BPM electronic music, dynamic motion, rhythmic'
                    },
                    {
                        'image_prompt': 'digital particles floating in space, glowing colors, abstract art',
                        'video_prompt': f'particles dancing rhythmically to {tempo} BPM beat, energetic movement'
                    }
                ],
                'special_moments': ['colorful explosion on beat drop, dramatic impact, intense energy']
            }
        elif mood == "calm":
            return {
                'style': 'serene',
                'scenes': [
                    {
                        'image_prompt': 'serene ocean at sunset, soft colors, peaceful atmosphere, cinematic',
                        'video_prompt': f'gentle waves slowly moving to {tempo} BPM music, calm motion, smooth'
                    },
                    {
                        'image_prompt': 'floating through soft clouds, dreamy atmosphere, ethereal light',
                        'video_prompt': f'clouds drifting peacefully to {tempo} BPM tempo, smooth floating motion'
                    }
                ],
                'special_moments': ['soft light burst, gentle glow, subtle transformation']
            }
        else:  # dynamic
            return {
                'style': 'abstract',
                'scenes': [
                    {
                        'image_prompt': 'liquid metal morphing, elegant shapes, modern art, reflective',
                        'video_prompt': f'liquid flowing rhythmically to {tempo} BPM music, dynamic movement'
                    },
                    {
                        'image_prompt': 'colorful light trails in dark space, abstract forms, vibrant',
                        'video_prompt': f'light trails moving gracefully to {tempo} BPM beat, flowing motion'
                    }
                ],
                'special_moments': ['color transformation, dramatic change, morphing effect']
            }
    
    def _generate_video_content(self, scene_plan, music_analysis):
        """Generate actual video content using Higgsfield APIs"""
        video_urls = []
        
        # Generate regular scenes (2 scenes to save credits)
        for i, scene in enumerate(scene_plan['scenes'][:2]):
            print(f"   🎨 Generating scene {i+1}/2...")
            
            # Check budget before proceeding
            if not self.credit_manager.can_afford('nano_banana', 2):
                print("   💰 Budget too low - stopping generation")
                break
            
            try:
                # Generate image
                print("     🖼️ Creating image...")
                image_url = self.api_client.text_to_image(scene['image_prompt'])
                self.credit_manager.add_usage('nano_banana')
                
                # Animate image to video
                print("     🎥 Animating to video...")
                video_url = self.api_client.image_to_video(image_url, scene['video_prompt'])
                self.credit_manager.add_usage('kling-2-5')
                
                video_urls.append({
                    'url': video_url,
                    'description': scene['video_prompt'],
                    'type': 'scene'
                })
                print(f"     ✅ Scene {i+1} completed!")
                
            except Exception as e:
                print(f"     ❌ Failed to generate scene {i+1}: {e}")
                continue
        
        # Add special moment if budget allows and music is energetic
        if (music_analysis['energy'] > 0.7 and 
            len(scene_plan['special_moments']) > 0 and
            self.credit_manager.can_afford('kling-2-1-master-t2v')):
            
            print("   💫 Adding special moment...")
            try:
                special_video = self.api_client.text_to_video(
                    scene_plan['special_moments'][0]
                )
                self.credit_manager.add_usage('kling-2-1-master-t2v')
                video_urls.append({
                    'url': special_video,
                    'description': scene_plan['special_moments'][0],
                    'type': 'special'
                })
                print("     ✅ Special moment added!")
            except Exception as e:
                print(f"     ❌ Special moment failed: {e}")
        
        return video_urls