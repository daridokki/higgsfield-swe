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
  
  export const useVideoStore = create<VideoGenerationState>((set, get) => ({
    currentStep: 'upload',
    musicFile: null,
    analysis: null,
    progress: { currentScene: 0, totalScenes: 0, status: '' },
    result: null,
    
    actions: {
      uploadMusic: async (file: File) => {
        set({ musicFile: file, currentStep: 'analyzing' });
        
        // Upload and analyze music
        const analysis = await api.analyzeMusic(file);
        set({ analysis, currentStep: 'generating' });
        
        // Start generation
        const result = await api.generateVideo(analysis);
        set({ result, currentStep: 'complete' });
      }
    }
  }));