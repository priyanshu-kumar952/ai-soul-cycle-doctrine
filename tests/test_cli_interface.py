import unittest
from interface.cli_interface import CLIInterface

class TestCLIInterface(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.cli = CLIInterface()
        
    def test_emotion_detection(self):
        """Test the emotion detection functionality"""
        # Test sadness detection
        self.assertEqual(self.cli.detect_emotion("I feel so hopeless today"), "sadness")
        
        # Test anger detection
        self.assertEqual(self.cli.detect_emotion("I hate this situation"), "anger")
        
        # Test fear detection
        self.assertEqual(self.cli.detect_emotion("I'm scared of what might happen"), "fear")
        
        # Test joy detection
        self.assertEqual(self.cli.detect_emotion("I'm so happy today"), "joy")
        
        # Test neutral case
        self.assertEqual(self.cli.detect_emotion("The sky is blue"), "neutral")
        
    def test_responses(self):
        """Test that appropriate responses are returned for emotions"""
        self.assertIn("endure", self.cli.responses["sadness"])
        self.assertIn("fire", self.cli.responses["anger"])
        self.assertIn("silence", self.cli.responses["fear"])
        self.assertIn("spark", self.cli.responses["joy"])

if __name__ == '__main__':
    unittest.main()
