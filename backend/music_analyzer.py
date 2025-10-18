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
            
            # Extract features with error handling and multiple methods
            tempo = 120.0  # Default fallback
            beats = []
            
            # Try multiple tempo detection methods
            try:
                # Method 1: Standard beat tracking
                tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
                print(f"   🎵 Beat tracking: {tempo:.1f} BPM")
            except Exception as e:
                print(f"   ⚠️ Beat tracking failed: {e}")
                
                # Method 2: Onset-based tempo estimation
                try:
                    onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
                    if len(onset_frames) > 1:
                        onset_times = librosa.frames_to_time(onset_frames, sr=sr)
                        intervals = np.diff(onset_times)
                        tempo = 60.0 / np.median(intervals)
                        print(f"   🎵 Onset-based tempo: {tempo:.1f} BPM")
                except Exception as e2:
                    print(f"   ⚠️ Onset detection failed: {e2}")
                    
                    # Method 3: Spectral-based estimation
                    try:
                        # Use spectral features to estimate tempo
                        spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
                        tempo = 60.0 + (np.mean(spectral_centroids) / 1000) * 60
                        tempo = max(60, min(200, tempo))  # Clamp to reasonable range
                        print(f"   🎵 Spectral-based tempo: {tempo:.1f} BPM")
                    except Exception as e3:
                        print(f"   ⚠️ All tempo methods failed, using default: {e3}")
                        tempo = 120.0
            
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
            
            # Calculate mood based on tempo, energy, and spectral features
            mood = self._classify_mood(tempo, energy, np.mean(spectral_centroids), np.mean(zero_crossing_rate))
            
            # Get duration
            duration = len(y) / sr
            
            # Calculate total beats
            total_beats = int((duration / 60) * tempo)
            
            # Enhanced analysis
            genre = self._classify_genre(tempo, energy, np.mean(spectral_centroids), np.mean(zero_crossing_rate))
            energy_level = self._get_energy_level(energy)
            
            analysis = {
                'tempo': float(tempo),
                'energy': float(energy),
                'mood': mood,
                'genre': genre,
                'energy_level': energy_level,
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
    
    def _classify_mood(self, tempo, energy, spectral_centroid=None, zero_crossing_rate=None):
        """Enhanced mood classification using multiple features"""
        # More sophisticated mood detection
        mood_score = 0
        
        # Tempo-based scoring
        if tempo > 140:
            mood_score += 3  # Very energetic
        elif tempo > 120:
            mood_score += 2  # Energetic
        elif tempo > 100:
            mood_score += 1  # Moderate
        elif tempo < 80:
            mood_score -= 2  # Calm
        elif tempo < 100:
            mood_score -= 1  # Slow
        
        # Energy-based scoring
        if energy > 0.2:
            mood_score += 3  # High energy
        elif energy > 0.1:
            mood_score += 2  # Medium energy
        elif energy > 0.05:
            mood_score += 1  # Low energy
        else:
            mood_score -= 1  # Very low energy
        
        # Spectral features (if available)
        if spectral_centroid is not None:
            if spectral_centroid > 3000:
                mood_score += 1  # Bright/happy
            elif spectral_centroid < 1500:
                mood_score -= 1  # Dark/serious
        
        if zero_crossing_rate is not None:
            if zero_crossing_rate > 0.1:
                mood_score += 1  # Percussive/rhythmic
            elif zero_crossing_rate < 0.05:
                mood_score -= 1  # Smooth/melodic
        
        # Classify based on total score
        if mood_score >= 4:
            return "energetic"
        elif mood_score <= -2:
            return "calm"
        else:
            return "dynamic"
    
    def _classify_genre(self, tempo, energy, spectral_centroid, zero_crossing_rate):
        """Enhanced genre classification for better scene selection"""
        # More sophisticated genre detection
        if tempo > 150 and energy > 0.2 and spectral_centroid > 4000:
            return "electronic"
        elif tempo > 140 and energy > 0.15:
            return "electronic"
        elif tempo > 120 and energy > 0.12 and zero_crossing_rate > 0.15:
            return "rock"
        elif tempo > 110 and energy > 0.08 and spectral_centroid > 3000:
            return "pop"
        elif tempo < 90 and energy < 0.06 and spectral_centroid < 2000:
            return "ambient"
        elif tempo < 100 and energy < 0.08:
            return "ambient"
        elif tempo > 100 and tempo < 130 and energy > 0.05 and energy < 0.12:
            return "alternative"
        else:
            return "alternative"
    
    def _get_energy_level(self, energy):
        """Get descriptive energy level"""
        if energy > 0.2:
            return "high"
        elif energy > 0.1:
            return "medium"
        else:
            return "low"
    
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