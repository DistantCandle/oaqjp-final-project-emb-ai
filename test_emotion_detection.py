from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy
        result_1 = sentiment_analyzer('I am glad this happened')
        self.assertEqual(result_1['label'], 'joy')

        # Test case for anger
        result_2 = sentiment_analyzer('I am really mad about this')
        self.assertEqual(result_2['label'], 'anger')

        # Test case for disgust
        result_3 = sentiment_analyzer('I feel disgusted just hearing about this')
        self.assertEqual(result_3['label'], 'disgust')

        # Test case for sadness
        result_4 = sentiment_analyzer('I am so sad about this')
        self.assertEqual(result_4['label'], 'sadness')

        # Test case for fear
        result_5 = sentiment_analyzer('I am really afraid that this will happen')
        self.assertEqual(result_5['label'], 'fear')

unittest.main()