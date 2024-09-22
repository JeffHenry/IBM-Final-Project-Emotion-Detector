'''
    Emotion Detection Package
'''

import json
import requests


def emotion_detector(text_to_analyze):
    ''' Detects the emotion of a provided text, analyzes each emotional value and returns a formatted JSON with a dominant emotion '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers=header, timeout=5)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        dominant_emotion = max(emotions, key=emotions.get)
        formatted_response = {
                            'anger': anger_score,
                            'disgust': disgust_score, 
                            'fear': fear_score, 
                            'joy': joy_score, 
                            'sadness': sadness_score, 
                            'dominant_emotion': dominant_emotion}
        return formatted_response
    if response.status_code == 400:
        formatted_response = {
                            'anger': None,
                            'disgust': None, 
                            'fear': None, 
                            'joy': None, 
                            'sadness': None, 
                            'dominant_emotion': None}
        return formatted_response

    return { 'Message' , 'Unexpected Error.' }, 404
