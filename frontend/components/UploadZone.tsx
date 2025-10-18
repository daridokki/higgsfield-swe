
export const UploadZone: React.FC = () => {
    const { uploadMusic } = useVideoStore();
    const [isDragging, setIsDragging] = useState(false);
    
    const handleFileSelect = async (files: FileList) => {
      const file = files[0];
      if (file && file.type.startsWith('audio/')) {
        await uploadMusic(file);
      }
    };
    
    return (
      <div className={`border-2 border-dashed rounded-lg p-12 text-center 
        ${isDragging ? 'border-blue-500 bg-blue-50' : 'border-gray-300'}`}
        onDragOver={(e) => { e.preventDefault(); setIsDragging(true); }}
        onDragLeave={() => setIsDragging(false)}
        onDrop={(e) => {
          e.preventDefault();
          setIsDragging(false);
          handleFileSelect(e.dataTransfer.files);
        }}
      >
        <MusicIcon className="mx-auto h-12 w-12 text-gray-400" />
        <div className="mt-4">
          <label className="cursor-pointer">
            <span className="text-lg font-medium">Upload your music</span>
            <input 
              type="file" 
              accept="audio/*"
              className="hidden"
              onChange={(e) => e.target.files && handleFileSelect(e.target.files)}
            />
          </label>
          <p className="text-gray-500 mt-2">MP3, WAV, or M4A files</p>
        </div>
      </div>
    );
  };