from music_analyzer import MusicAnalyzer
from higgsfield_client import HiggsfieldClient
from config import Config
import os

class VideoGenerator:
    def __init__(self):
        self.music_analyzer = MusicAnalyzer()
        self.api_client = HiggsfieldClient(
            Config.HIGGSFIELD_API_KEY,
            Config.HIGGSFIELD_API_SECRET
        )
    
    def create_video_from_music(self, audio_file_path, progress_callback=None):
        """
        Main function: Turn music into video with progress tracking
        """
        total_steps = 6  # Total number of major steps
        current_step = 0
        
        def update_progress(step_name, progress_percent):
            if progress_callback:
                progress_callback({
                    'step': step_name,
                    'progress': progress_percent,
                    'current_step': current_step,
                    'total_steps': total_steps
                })
        
        # Step 1: Analyzing music (0-15%)
        print("🎵 Step 1: Analyzing music...")
        update_progress("Analyzing music...", 5)
        music_analysis = self.music_analyzer.analyze_music(audio_file_path)
        print(f"   Analysis: {music_analysis['tempo']} BPM, {music_analysis['mood']}, energy: {music_analysis['energy']:.2f}")
        current_step += 1
        update_progress("Music analysis complete", 15)
        
        # Step 2: Planning video scenes (15-25%)
        print("🎬 Step 2: Planning video scenes...")
        update_progress("Planning video scenes...", 20)
        scene_plan = self._plan_video_scenes(music_analysis)
        current_step += 1
        update_progress("Scene planning complete", 25)
        
        # Step 3: Generating video content (25-100%)
        print("✨ Step 3: Generating video content...")
        update_progress("Starting video generation...", 30)
        video_urls = self._generate_video_content(scene_plan, music_analysis, progress_callback, current_step, total_steps)
        current_step = total_steps
        update_progress("Video generation complete", 100)
        
        return {
            'music_analysis': music_analysis,
            'video_urls': video_urls
        }
    
    def _plan_video_scenes(self, music_analysis):
        """Create sophisticated video plan based on music characteristics"""
        tempo = music_analysis['tempo']
        mood = music_analysis['mood']
        genre = music_analysis.get('genre', 'alternative')
        energy_level = music_analysis.get('energy_level', 'medium')
        energy = music_analysis.get('energy', 0.1)
        spectral_centroid = music_analysis.get('spectral_centroid', 2000)
        
        # Add randomization based on audio characteristics for diversity
        import random
        random.seed(int(tempo * energy * 1000))  # Deterministic but varied
        
        # Enhanced scene generation with more diversity
        if genre == "electronic" and mood == "energetic":
            return self._get_electronic_scenes(tempo, energy_level, energy, spectral_centroid)
        elif genre == "rock" and mood == "energetic":
            return self._get_rock_scenes(tempo, energy_level, energy, spectral_centroid)
        elif genre == "ambient" and mood == "calm":
            return self._get_ambient_scenes(tempo, energy_level, energy, spectral_centroid)
        elif genre == "pop":
            return self._get_pop_scenes(tempo, energy_level, energy, spectral_centroid)
        else:
            return self._get_alternative_scenes(tempo, mood, energy_level, energy, spectral_centroid)
    
    def _get_electronic_scenes(self, tempo, energy_level, energy, spectral_centroid):
        """Electronic music scenes - futuristic, neon, cyberpunk with diversity"""
        import random
        
        # Multiple scene variations based on audio characteristics
        scene_variations = []
        
        if energy_level == "high":
            # High energy electronic scenes
            scene_variations = [
                {
                    'image_prompt': 'massive futuristic cityscape at night, towering skyscrapers with neon lights, rain-soaked streets reflecting neon, cyberpunk atmosphere, cinematic wide shot, detailed architecture, dramatic lighting',
                    'video_prompt': f'neon signs flickering and pulsing intensely to {tempo} BPM electronic beat, rain drops hitting the pavement creating ripples, cars driving by with light trails, city lights dancing'
                },
                {
                    'image_prompt': 'underground rave club interior, laser lights cutting through thick smoke, crowd of people dancing silhouettes, vibrant neon colors, high energy atmosphere, strobe lighting effects',
                    'video_prompt': f'laser lights sweeping rapidly across the dance floor to {tempo} BPM rhythm, smoke swirling in patterns, silhouettes moving intensely to the beat, strobe effects'
                },
                {
                    'image_prompt': 'futuristic space station interior, holographic displays, advanced technology, metallic surfaces, blue and purple lighting, sci-fi atmosphere, high-tech environment',
                    'video_prompt': f'holographic displays responding to {tempo} BPM electronic rhythm, data streams flowing across screens, futuristic technology pulsing with energy'
                },
                {
                    'image_prompt': 'cyberpunk alleyway at night, neon graffiti on walls, steam rising from manholes, urban decay mixed with technology, dramatic shadows, gritty futuristic atmosphere',
                    'video_prompt': f'neon graffiti glowing and pulsing to {tempo} BPM beat, steam swirling in the air, shadows dancing on the walls, urban energy flowing through the space'
                }
            ]
        else:
            # Lower energy electronic scenes
            scene_variations = [
                {
                    'image_prompt': 'modern electronic music studio, synthesizers and equipment, soft neon glow, professional setup, intimate atmosphere, creative workspace',
                    'video_prompt': f'equipment lights pulsing gently to {tempo} BPM electronic rhythm, subtle movements, creative energy flowing through the space'
                },
                {
                    'image_prompt': 'futuristic lounge with ambient lighting, comfortable seating, holographic displays, modern design, relaxed electronic atmosphere',
                    'video_prompt': f'ambient lights shifting colors to {tempo} BPM tempo, holographic displays responding to the music, peaceful electronic vibes'
                },
                {
                    'image_prompt': 'minimalist futuristic apartment, clean lines, soft LED lighting, modern furniture, serene atmosphere, high-tech but comfortable',
                    'video_prompt': f'LED lights gently pulsing to {tempo} BPM rhythm, subtle color changes, peaceful electronic ambiance, modern living space'
                },
                {
                    'image_prompt': 'digital art gallery, abstract geometric patterns, soft neon colors, artistic atmosphere, creative space, modern art installation',
                    'video_prompt': f'geometric patterns shifting and morphing to {tempo} BPM electronic rhythm, colors blending and changing, artistic digital expression'
                }
            ]
        
        # Select 2 scenes based on audio characteristics for diversity
        random.seed(int(tempo * energy * spectral_centroid))
        selected_scenes = random.sample(scene_variations, min(2, len(scene_variations)))
        
        return {'style': 'cyberpunk', 'scenes': selected_scenes, 'special_moments': ['massive bass drop with strobe lights, crowd going wild, intense energy burst']}
    
    def _get_rock_scenes(self, tempo, energy_level, energy, spectral_centroid):
        """Rock music scenes - gritty, urban, powerful with diversity"""
        import random
        
        scene_variations = [
            {
                'image_prompt': 'abandoned warehouse with graffiti walls, dramatic shadows, urban decay, gritty atmosphere, cinematic composition',
                'video_prompt': f'graffiti art coming to life, paint splashing to {tempo} BPM rock rhythm, shadows dancing on the walls'
            },
            {
                'image_prompt': 'concert stage with spotlights, smoke machines, crowd silhouettes, rock concert atmosphere, dramatic lighting',
                'video_prompt': f'guitar strings vibrating to {tempo} BPM beat, spotlights sweeping the stage, crowd headbanging in slow motion'
            },
            {
                'image_prompt': 'underground music venue, dim red lighting, exposed brick walls, intimate setting, raw atmosphere, indie rock vibe',
                'video_prompt': f'red lights pulsing to {tempo} BPM rock rhythm, shadows moving on brick walls, intimate concert energy'
            },
            {
                'image_prompt': 'desert highway at sunset, vintage car, dust clouds, road trip atmosphere, golden hour lighting, freedom and adventure',
                'video_prompt': f'dust clouds swirling to {tempo} BPM rock beat, car headlights cutting through the dust, desert wind moving'
            },
            {
                'image_prompt': 'urban rooftop at night, city skyline, industrial pipes, gritty urban landscape, dramatic city lighting',
                'video_prompt': f'city lights twinkling to {tempo} BPM rhythm, industrial pipes vibrating, urban energy flowing through the night'
            }
        ]
        
        # Select 2 scenes based on audio characteristics
        random.seed(int(tempo * energy * spectral_centroid))
        selected_scenes = random.sample(scene_variations, min(2, len(scene_variations)))
        
        return {'style': 'urban', 'scenes': selected_scenes, 'special_moments': ['guitar solo with sparks flying, crowd erupting, pure rock energy']}
    
    def _get_ambient_scenes(self, tempo, energy_level, energy, spectral_centroid):
        """Ambient music scenes - peaceful, natural, ethereal with diversity"""
        import random
        
        scene_variations = [
            {
                'image_prompt': 'misty forest at dawn, sunlight filtering through trees, peaceful nature scene, soft natural lighting, serene atmosphere',
                'video_prompt': f'gentle mist flowing through the trees to {tempo} BPM ambient rhythm, leaves falling slowly, birds flying in the distance'
            },
            {
                'image_prompt': 'mountain lake at sunset, reflection of clouds in water, peaceful landscape, golden hour lighting, tranquil scene',
                'video_prompt': f'water ripples spreading across the lake to {tempo} BPM tempo, clouds moving slowly across the sky, peaceful meditation'
            },
            {
                'image_prompt': 'northern lights dancing in arctic sky, snow-covered landscape, aurora borealis, magical atmosphere, cold but beautiful',
                'video_prompt': f'aurora lights dancing to {tempo} BPM ambient rhythm, snow gently falling, magical northern lights flowing across the sky'
            },
            {
                'image_prompt': 'zen garden with raked sand, stone arrangements, bamboo, peaceful meditation space, minimalist beauty, tranquil atmosphere',
                'video_prompt': f'sand patterns shifting to {tempo} BPM ambient rhythm, bamboo swaying gently, peaceful zen meditation energy'
            },
            {
                'image_prompt': 'ocean waves at night, moonlight reflecting on water, peaceful seascape, serene ocean atmosphere, calming blue tones',
                'video_prompt': f'waves gently rolling to {tempo} BPM ambient rhythm, moonlight dancing on the water, peaceful ocean meditation'
            }
        ]
        
        # Select 2 scenes based on audio characteristics
        random.seed(int(tempo * energy * spectral_centroid))
        selected_scenes = random.sample(scene_variations, min(2, len(scene_variations)))
        
        return {'style': 'serene', 'scenes': selected_scenes, 'special_moments': ['sunrise breaking through clouds, gentle transformation, peaceful awakening']}
    
    def _get_pop_scenes(self, tempo, energy_level, energy, spectral_centroid):
        """Pop music scenes - vibrant, colorful, mainstream with diversity"""
        import random
        
        scene_variations = [
            {
                'image_prompt': 'colorful city street during golden hour, people walking, vibrant storefronts, upbeat urban atmosphere, warm lighting',
                'video_prompt': f'people walking in rhythm to {tempo} BPM pop beat, street performers dancing, colorful balloons floating by'
            },
            {
                'image_prompt': 'modern apartment with large windows, city view, contemporary interior, bright and clean, stylish atmosphere',
                'video_prompt': f'curtains swaying to {tempo} BPM rhythm, city lights twinkling outside, person dancing in the living room'
            },
            {
                'image_prompt': 'beach party at sunset, colorful umbrellas, people dancing, tropical atmosphere, warm golden lighting, summer vibes',
                'video_prompt': f'people dancing on the beach to {tempo} BPM pop rhythm, colorful umbrellas swaying, sunset creating golden reflections'
            },
            {
                'image_prompt': 'shopping mall with bright lights, people walking, modern architecture, vibrant atmosphere, commercial but energetic',
                'video_prompt': f'people walking in rhythm to {tempo} BPM pop beat, bright lights pulsing, shopping energy flowing through the space'
            },
            {
                'image_prompt': 'rooftop party with city skyline, colorful decorations, people celebrating, urban nightlife, vibrant party atmosphere',
                'video_prompt': f'party decorations swaying to {tempo} BPM pop rhythm, city lights twinkling, people celebrating with energy'
            }
        ]
        
        # Select 2 scenes based on audio characteristics
        random.seed(int(tempo * energy * spectral_centroid))
        selected_scenes = random.sample(scene_variations, min(2, len(scene_variations)))
        
        return {'style': 'contemporary', 'scenes': selected_scenes, 'special_moments': ['confetti explosion, crowd cheering, pure joy and celebration']}
    
    def _get_alternative_scenes(self, tempo, mood, energy_level, energy, spectral_centroid):
        """Alternative music scenes - artistic, unique, creative with diversity"""
        import random
        
        scene_variations = [
            {
                'image_prompt': 'art gallery with abstract paintings, dramatic shadows, artistic atmosphere, creative lighting, modern art space',
                'video_prompt': f'paint strokes moving across canvas to {tempo} BPM alternative rhythm, shadows dancing on the walls, artistic expression'
            },
            {
                'image_prompt': 'underground music venue, intimate setting, dim lighting, artistic crowd, creative atmosphere, indie vibe',
                'video_prompt': f'musicians performing passionately to {tempo} BPM beat, audience swaying, intimate connection between artist and crowd'
            },
            {
                'image_prompt': 'vintage record store, vinyl records on shelves, warm lighting, nostalgic atmosphere, music lover sanctuary',
                'video_prompt': f'record sleeves gently moving to {tempo} BPM alternative rhythm, warm light dancing on vinyl, musical nostalgia flowing'
            },
            {
                'image_prompt': 'coffee shop with exposed brick, indie atmosphere, people working on laptops, creative workspace, hipster vibe',
                'video_prompt': f'coffee steam rising to {tempo} BPM alternative rhythm, people typing in rhythm, creative energy flowing through the space'
            },
            {
                'image_prompt': 'abandoned theater with vintage seats, dramatic lighting, artistic decay, creative space, theatrical atmosphere',
                'video_prompt': f'stage lights flickering to {tempo} BPM alternative rhythm, dust particles dancing in the light, theatrical energy flowing'
            }
        ]
        
        # Select 2 scenes based on audio characteristics
        random.seed(int(tempo * energy * spectral_centroid))
        selected_scenes = random.sample(scene_variations, min(2, len(scene_variations)))
        
        return {'style': 'artistic', 'scenes': selected_scenes, 'special_moments': ['artistic breakthrough, creative explosion, pure artistic expression']}
    
    def _generate_video_content(self, scene_plan, music_analysis, progress_callback=None, current_step=0, total_steps=6):
        """Generate actual video content using Higgsfield APIs with progress tracking"""
        video_urls = []
        
        print(f"🎬 Starting video generation with {len(scene_plan['scenes'])} scenes...")
        
        # Generate regular scenes (limit to 2 for performance)
        max_scenes = min(2, len(scene_plan['scenes']))
        successful_scenes = 0
        
        def update_progress(step_name, progress_percent):
            if progress_callback:
                progress_callback({
                    'step': step_name,
                    'progress': progress_percent,
                    'current_step': current_step,
                    'total_steps': total_steps
                })
        
        for i, scene in enumerate(scene_plan['scenes'][:max_scenes]):
            print(f"   🎨 Generating scene {i+1}/{max_scenes}...")
            print(f"     Image prompt: {scene['image_prompt'][:50]}...")
            print(f"     Video prompt: {scene['video_prompt'][:50]}...")
            
            # Update progress for scene start
            scene_progress = 30 + (i * 30)  # 30% + 30% per scene
            update_progress(f"Generating scene {i+1}/{max_scenes}...", scene_progress)
            
            
            try:
                # Generate image
                print("     🖼️ Creating image with Nano Banana...")
                update_progress(f"Creating image for scene {i+1}...", scene_progress + 5)
                image_url = self.api_client.text_to_image(scene['image_prompt'])
                print(f"     ✅ Image created: {image_url[:50]}...")
                
                # Animate image to video
                print("     🎥 Animating to video with Kling 2.5 Turbo...")
                update_progress(f"Animating scene {i+1} to video...", scene_progress + 10)
                video_url = self.api_client.image_to_video(image_url, scene['video_prompt'])
                print(f"     ✅ Video created: {video_url[:50]}...")
                
                video_urls.append({
                    'url': video_url,
                    'description': scene['video_prompt'],
                    'type': 'scene'
                })
                print(f"     ✅ Scene {i+1} completed successfully!")
                successful_scenes += 1
                update_progress(f"Scene {i+1} completed!", scene_progress + 15)
                
            except Exception as e:
                print(f"     ❌ Failed to generate scene {i+1}: {e}")
                print(f"     Error type: {type(e).__name__}")
                
                # If it's a timeout, try to continue with what we have
                if "timed out" in str(e).lower():
                    print(f"     ⏰ Scene {i+1} timed out - continuing with available results...")
                else:
                    import traceback
                    print(f"     Traceback: {traceback.format_exc()}")
                
                # Continue to next scene instead of breaking
                continue
        
        # Add special moment if music is energetic
        if (music_analysis['energy'] > 0.7 and 
            len(scene_plan['special_moments']) > 0):
            
            print("   💫 Adding special moment...")
            try:
                special_video = self.api_client.text_to_video(
                    scene_plan['special_moments'][0]
                )
                video_urls.append({
                    'url': special_video,
                    'description': scene_plan['special_moments'][0],
                    'type': 'special'
                })
                print("     ✅ Special moment added!")
            except Exception as e:
                print(f"     ❌ Special moment failed: {e}")
        
        # Summary
        print(f"🎬 Generation complete: {successful_scenes} scenes generated successfully")
        if successful_scenes == 0:
            print("   ⚠️ No scenes were generated - check API status and try again")
        
        return video_urls