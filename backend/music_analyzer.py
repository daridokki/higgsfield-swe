import librosa
import numpy as np
import os

class MusicAnalyzer:
    def analyze_music(self, audio_file_path):
        """
        REAL music analysis using librosa
        """
        try:
            print(f"🎵 Analyzing music file: {os.path.basename(audio_file_path)}")
            
            # Load audio file
            y, sr = librosa.load(audio_file_path)
            
            # Extract features with error handling
            try:
                tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
            except Exception as e:
                print(f"   ⚠️ Beat tracking failed: {e}")
                tempo = 120.0
                beats = []
            
            try:
                spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
            except Exception as e:
                print(f"   ⚠️ Spectral centroid failed: {e}")
                spectral_centroids = np.array([0.5])
            
            try:
                zero_crossing_rate = librosa.feature.zero_crossing_rate(y)[0]
            except Exception as e:
                print(f"   ⚠️ Zero crossing rate failed: {e}")
                zero_crossing_rate = np.array([0.1])
            
            # Calculate energy (RMS)
            energy = np.sqrt(np.mean(y**2))
            
            # Calculate mood based on tempo and energy
            mood = self._classify_mood(tempo, energy)
            
            # Get duration
            duration = len(y) / sr
            
            # Calculate total beats
            total_beats = int((duration / 60) * tempo)
            
            analysis = {
                'tempo': float(tempo),
                'energy': float(energy),
                'mood': mood,
                'duration': float(duration),
                'total_beats': total_beats,
                'spectral_centroid': float(np.mean(spectral_centroids)),
                'zero_crossing_rate': float(np.mean(zero_crossing_rate))
            }
            
            print(f"   📊 Analysis: {tempo:.1f} BPM, {mood}, energy: {energy:.2f}")
            return analysis
            
        except Exception as e:
            print(f"❌ Music analysis error: {e}")
            print("   Using fallback analysis...")
            return self._get_default_analysis()
    
    def _classify_mood(self, tempo, energy):
        """Classify music mood based on tempo and energy"""
        if tempo > 120 and energy > 0.1:
            return "energetic"
        elif tempo < 90 and energy < 0.05:
            return "calm"
        else:
            return "dynamic"
    
    def _get_default_analysis(self):
        """Fallback analysis if librosa fails"""
        return {
            'tempo': 120.0,
            'energy': 0.5, 
            'mood': 'dynamic',
            'duration': 30.0,
            'total_beats': 60,
            'spectral_centroid': 2000.0,
            'zero_crossing_rate': 0.1
        }