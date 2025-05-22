import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        self.assertEqual(emotion_detector('I am glad this happened'), 'joy')

    def test_anger(self):
        self.assertEqual(emotion_detector('I am really mad about this'), 'anger')

    def test_disgust(self):
        self.assertEqual(emotion_detector('I feel disgusted just hearing about this'), 'disgust')

    def test_sadness(self):
        self.assertEqual(emotion_detector('I am so sad about this'), 'sadness')

    def test_fear(self):
        self.assertEqual(emotion_detector('I am really afraid that this will happen'), 'fear')

if __name__ == '__main__':
    unittest.main()