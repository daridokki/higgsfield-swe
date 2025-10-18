class MusicAnalyzer:
    def analyze_music(self, audio_file_path):
        """
        Simple music analysis - works without any imports
        """
        try:
            # Mock analysis that always works
            return {
                'tempo': 128.0,  # Mock tempo
                'energy': 0.7,   # Mock energy
                'mood': 'energetic',
                'duration': 30.0,
                'total_beats': 60
            }
            
        except Exception as e:
            print(f"Music analysis error: {e}")
            return self._get_default_analysis()
    
    def _classify_mood(self, tempo, energy):
        """Simple rules to determine music mood"""
        if tempo > 120 and energy > 0.1:
            return "energetic"
        elif tempo < 90 and energy < 0.05:
            return "calm"
        else:
            return "dynamic"
    
    def _get_default_analysis(self):
        """Fallback if analysis fails"""
        return {
            'tempo': 120,
            'energy': 0.5, 
            'mood': 'dynamic',
            'duration': 30,
            'total_beats': 60
        }