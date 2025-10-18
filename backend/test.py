import os
import sys

# Enable mock mode for testing (no credits spent!)
os.environ['USE_MOCK_API'] = 'true'

# Add current directory to path
sys.path.append('.')

from video_generator import VideoGenerator

def test_music_analysis():
    """Test just the music analysis part"""
    print("🧪 Testing Music Analysis...")
    
    generator = VideoGenerator()
    
    # Create a simple test (you'll need actual music files)
    test_cases = [
        {'name': 'Fast Electronic', 'tempo': 130, 'energy': 0.8},
        {'name': 'Slow Piano', 'tempo': 70, 'energy': 0.3},
        {'name': 'Rock Song', 'tempo': 110, 'energy': 0.6}
    ]
    
    for test in test_cases:
        print(f"\n🎵 Testing {test['name']}:")
        # Create mock analysis
        mock_analysis = {
            'tempo': test['tempo'],
            'energy': test['energy'],
            'mood': generator.music_analyzer._classify_mood(test['tempo'], test['energy'])
        }
        
        scene_plan = generator._plan_video_scenes(mock_analysis)
        print(f"   Style: {scene_plan['style']}")
        print(f"   Scenes: {len(scene_plan['scenes'])}")
        for i, scene in enumerate(scene_plan['scenes']):
            print(f"   Scene {i+1}: {scene['image_prompt'][:50]}...")

def test_complete_flow():
    """Test the complete flow with mock API"""
    print("\n🎬 Testing Complete Music-to-Video Flow (Mock Mode)...")
    
    generator = VideoGenerator()
    
    # Test with different music scenarios
    test_scenarios = [
        {'tempo': 135, 'energy': 0.8, 'mood': 'energetic', 'name': 'EDM Track'},
        {'tempo': 72, 'energy': 0.2, 'mood': 'calm', 'name': 'Piano Piece'},
        {'tempo': 105, 'energy': 0.5, 'mood': 'dynamic', 'name': 'Pop Song'}
    ]
    
    for scenario in test_scenarios:
        print(f"\n--- Testing {scenario['name']} ---")
        
        # Create mock file path (in real use, this would be an actual file)
        mock_file = f"test_{scenario['name'].replace(' ', '_').lower()}.mp3"
        
        # Mock the analysis to return our test scenario
        original_analyze = generator.music_analyzer.analyze_music
        generator.music_analyzer.analyze_music = lambda x: scenario
        
        try:
            result = generator.create_video_from_music(mock_file)
            print(f"✅ Success! Generated {len(result['video_urls'])} videos")
            print(f"💰 Budget used: ${result['budget_used']:.2f}")
            
            for i, video in enumerate(result['video_urls']):
                print(f"   🎥 Video {i+1}: {video['url']}")
                
        except Exception as e:
            print(f"❌ Error: {e}")
        
        finally:
            # Restore original method
            generator.music_analyzer.analyze_music = original_analyze

if __name__ == "__main__":
    print("🎵 Music-to-Video System Tests")
    print("===============================")
    
    test_music_analysis()
    test_complete_flow()
    
    print("\n✅ All tests completed! Use 'python app.py' to start the server.")
