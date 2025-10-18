import librosa
import numpy as np

class MusicAnalyzer:
    def analyze_music(self, audio_file_path):
        """
        Simple music analysis - extracts tempo, energy, and mood
        """
        try:
            # Load audio file
            y, sr = librosa.load(audio_file_path)
            
            # Basic analysis
            tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
            energy = np.mean(librosa.feature.rms(y=y))
            
            # Simple mood classification
            mood = self._classify_mood(tempo, energy)
            
            return {
                'tempo': float(tempo),
                'energy': float(energy),
                'mood': mood,
                'duration': len(y) / sr,
                'total_beats': len(beats)
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