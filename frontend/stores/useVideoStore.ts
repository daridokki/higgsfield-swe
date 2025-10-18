// frontend/stores/useVideoStore.ts
import { create } from 'zustand';

// Define the types
interface MusicAnalysis {
  tempo: number;
  energy: number;
  mood: string;
  beats: number[];
  structure: {
    sections: Array<{
      start: number;
      end: number;
      intensity: number;
    }>;
    intensity_changes: number[];
  };
}

interface GeneratedScene {
  imageUrl: string;
  videoUrl: string;
  prompt: string;
  duration: number;
  transition: string;
}

interface VideoGenerationState {
  currentStep: 'upload' | 'analyzing' | 'generating' | 'complete';
  musicFile: File | null;
  analysis: MusicAnalysis | null;
  progress: {
    currentScene: number;
    totalScenes: number;
    status: string;
  };
  result: {
    videoUrl: string;
    scenes: GeneratedScene[];
  } | null;
}

interface VideoStore extends VideoGenerationState {
  actions: {
    uploadMusic: (file: File) => Promise<void>;
    setProgress: (progress: Partial<VideoGenerationState['progress']>) => void;
    reset: () => void;
  };
}

// API client
const api = {
  analyzeMusic: async (file: File): Promise<MusicAnalysis> => {
    const formData = new FormData();
    formData.append('audio', file);
    
    const response = await fetch('/api/analyze', {
      method: 'POST',
      body: formData,
    });
    
    if (!response.ok) {
      throw new Error('Analysis failed');
    }
    
    const data = await response.json();
    return data.analysis;
  },
  
  generateVideo: async (analysis: MusicAnalysis): Promise<{ videoUrl: string; scenes: GeneratedScene[] }> => {
    const response = await fetch('/api/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ analysis }),
    });
    
    if (!response.ok) {
      throw new Error('Generation failed');
    }
    
    return await response.json();
  }
};

export const useVideoStore = create<VideoStore>((set, get) => ({
  // Initial state
  currentStep: 'upload',
  musicFile: null,
  analysis: null,
  progress: { currentScene: 0, totalScenes: 0, status: '' },
  result: null,
  
  // Actions
  actions: {
    uploadMusic: async (file: File) => {
      set({ 
        musicFile: file, 
        currentStep: 'analyzing',
        progress: { currentScene: 0, totalScenes: 4, status: 'Analyzing music...' }
      });
      
      try {
        // Upload and analyze music
        const analysis = await api.analyzeMusic(file);
        set({ 
          analysis, 
          currentStep: 'generating',
          progress: { currentScene: 1, totalScenes: 4, status: 'Generating scenes...' }
        });
        
        // Start generation
        const result = await api.generateVideo(analysis);
        set({ 
          result, 
          currentStep: 'complete',
          progress: { currentScene: 4, totalScenes: 4, status: 'Complete!' }
        });
        
      } catch (error) {
        console.error('Upload failed:', error);
        set({ 
          currentStep: 'upload',
          progress: { currentScene: 0, totalScenes: 0, status: 'Upload failed' }
        });
      }
    },
    
    setProgress: (progress) => {
      set((state) => ({
        progress: { ...state.progress, ...progress }
      }));
    },
    
    reset: () => {
      set({
        currentStep: 'upload',
        musicFile: null,
        analysis: null,
        progress: { currentScene: 0, totalScenes: 0, status: '' },
        result: null,
      });
    },
  },
}));