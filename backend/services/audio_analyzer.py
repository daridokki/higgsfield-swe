import librosa
import numpy as np
from typing import Dict, List

class AudioAnalyzer:
    def __init__(self):
        self.sample_rate = 22050
        
    def analyze_track(self, audio_path: str) -> Dict:
        """Comprehensive music analysis"""
        y, sr = librosa.load(audio_path, sr=self.sample_rate)
        
        return {
            'tempo': self._get_tempo(y, sr),
            'beats': self._get_beats(y, sr),
            'energy': self._get_energy(y),
            'mood': self._classify_mood(y, sr),
            'structure': self._analyze_structure(y, sr),
            'key_features': self._get_key_features(y, sr)
        }
    
    def _get_tempo(self, y, sr) -> float:
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        return tempo
    
    def _get_beats(self, y, sr) -> List[float]:
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = librosa.frames_to_time(beats, sr=sr)
        return beat_times.tolist()
    
    def _get_energy(self, y) -> float:
        rms = librosa.feature.rms(y=y)
        return float(np.mean(rms))
    
    def _classify_mood(self, y, sr) -> str:
        # Advanced mood classification using multiple features
        spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
        zero_crossing = np.mean(librosa.feature.zero_crossing_rate(y))
        
        if spectral_centroid > 2000 and self._get_energy(y) > 0.1:
            return "energetic"
        elif spectral_centroid < 1500 and self._get_energy(y) < 0.05:
            return "calm"
        else:
            return "dynamic"
    
    def _analyze_structure(self, y, sr) -> Dict:
        # Detect song sections (verse, chorus, etc.)
        onset_env = librosa.onset.onset_strength(y=y, sr=sr)
        frames = range(len(onset_env))
        times = librosa.frames_to_time(frames, sr=sr)
        
        return {
            'sections': self._detect_sections(onset_env, times),
            'intensity_changes': self._find_intensity_changes(onset_env)
        }