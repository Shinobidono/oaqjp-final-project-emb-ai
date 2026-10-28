import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=myobj, headers=header)

    # Handle blank entry — API returns 400 for empty input
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parse the response for valid input
    response_data = json.loads(response.text)

    emotions = response_data['emotionPredictions'][0]['emotion']

    anger_score   = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score    = emotions['fear']
    joy_score     = emotions['joy']
    sadness_score = emotions['sadness']

    emotion_scores = {
        'anger':   anger_score,
        'disgust': disgust_score,
        'fear':    fear_score,
        'joy':     joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger':            anger_score,
        'disgust':          disgust_score,
        'fear':             fear_score,
        'joy':              joy_score,
        'sadness':          sadness_score,
        'dominant_emotion': dominant_emotion
    }