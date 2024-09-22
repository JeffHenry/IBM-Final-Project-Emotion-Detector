"""
Unit tests for emotion detection and prediction.

This module contains tests to verify that the emotion detection and prediction functions
correctly identify the dominant emotion from text inputs.
"""

import unittest  # Standard import should come first
from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

class TestEmotionDetection(unittest.TestCase):
    '''
    Unit tests for the emotion detection and prediction functionality.

    This class contains unit tests for verifying the correct prediction of 
    dominant emotions from textual input using the `emotion_detector` and 
    `emotion_predictor` functions from the EmotionDetection library. 
    The tests ensure that the predicted emotions match expected values 
    for various emotional inputs such as joy, anger, disgust, sadness, and fear.
    '''
    def test_emotion_predictor(self):
        '''
        Tests the emotion prediction functionality for various input emotions.

        This method runs unit tests to verify that the `emotion_predictor` correctly identifies 
        the dominant emotion from the output of the `emotion_detector`. It tests five different 
        emotional inputs: joy, anger, disgust, sadness, and fear. Each test checks if the predicted 
        dominant emotion matches the expected result for the given input text.
        '''
        result_1 = emotion_predictor(emotion_detector("I am glad this happened"))
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        result_2 = emotion_predictor(emotion_detector("I am really mad about this"))
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        result_3 = emotion_predictor(emotion_detector("I feel disgusted just hearing about this"))
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        result_4 = emotion_predictor(emotion_detector("I am so sad about this"))
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        result_5 = emotion_predictor(emotion_detector("I am really afraid that this will happen"))
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
