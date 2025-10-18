class VisualPromptGenerator:
    def __init__(self):
        self.visual_library = {
            'energetic': {
                'styles': ['cyberpunk', 'neon', 'futuristic', 'digital art'],
                'motions': ['pulsing', 'rapid', 'explosive', 'dynamic'],
                'colors': ['vibrant', 'saturated', 'contrasting']
            },
            'calm': {
                'styles': ['serene', 'nature', 'minimalist', 'watercolor'],
                'motions': ['gentle', 'flowing', 'slow motion', 'peaceful'],
                'colors': ['pastel', 'soft', 'muted']
            },
            'dynamic': {
                'styles': ['abstract', 'liquid', 'organic', 'surreal'],
                'motions': ['morphing', 'transforming', 'flowing', 'evolving'],
                'colors': ['gradient', 'shifting', 'harmonic']
            }
        }
    
    def generate_scene_prompts(self, analysis: Dict, num_scenes: int = 4) -> List[Dict]:
        """Generate visual prompts for different song sections"""
        scenes = []
        sections = analysis['structure']['sections']
        
        for i in range(num_scenes):
            section_mood = self._get_section_mood(analysis, i, num_scenes)
            visual_style = self.visual_library[section_mood]
            
            scene = {
                'image_prompt': self._build_image_prompt(visual_style, i),
                'video_prompt': self._build_video_prompt(visual_style, analysis['tempo']),
                'duration': self._calculate_duration(analysis, i, num_scenes),
                'transition': self._get_transition_style(section_mood)
            }
            scenes.append(scene)
        
        return scenes
    
    def _build_image_prompt(self, visual_style: Dict, scene_index: int) -> str:
        style = np.random.choice(visual_style['styles'])
        color = np.random.choice(visual_style['colors'])
        
        base_prompts = [
            f"{style} landscape with {color} colors, highly detailed",
            f"abstract {style} composition in {color} palette",
            f"{style} pattern with {color} tones, intricate details"
        ]
        
        return np.random.choice(base_prompts)