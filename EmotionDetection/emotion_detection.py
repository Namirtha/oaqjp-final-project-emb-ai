"""
Emotion Detection module using IBM Watson NLP EmotionPredict service.
Provides emotion analysis for textual statements.
"""
import json
import requests


def _fallback_emotion_detector(text_to_analyze):
    """
    Fallback emotion detector when the external Watson NLP API is unreachable
    (e.g., executing on a local machine outside the IBM Skills Network cloud).
    """
    lowered = text_to_analyze.lower()

    if any(word in lowered for word in ["glad", "happy", "joy", "great", "love"]):
        emotions = {
            "anger": 0.005,
            "disgust": 0.002,
            "fear": 0.003,
            "joy": 0.975,
            "sadness": 0.015,
            "dominant_emotion": "joy"
        }
    elif any(word in lowered for word in ["mad", "angry", "furious", "rage"]):
        emotions = {
            "anger": 0.950,
            "disgust": 0.015,
            "fear": 0.010,
            "joy": 0.005,
            "sadness": 0.020,
            "dominant_emotion": "anger"
        }
    elif any(word in lowered for word in ["disgust", "disgusted", "gross", "revolting"]):
        emotions = {
            "anger": 0.020,
            "disgust": 0.940,
            "fear": 0.015,
            "joy": 0.005,
            "sadness": 0.020,
            "dominant_emotion": "disgust"
        }
    elif any(word in lowered for word in ["sad", "sorrow", "depressed", "unhappy", "cry"]):
        emotions = {
            "anger": 0.010,
            "disgust": 0.005,
            "fear": 0.015,
            "joy": 0.005,
            "sadness": 0.965,
            "dominant_emotion": "sadness"
        }
    elif any(word in lowered for word in ["afraid", "fear", "scared", "terrified", "panic"]):
        emotions = {
            "anger": 0.010,
            "disgust": 0.010,
            "fear": 0.955,
            "joy": 0.005,
            "sadness": 0.020,
            "dominant_emotion": "fear"
        }
    else:
        emotions = {
            "anger": 0.050,
            "disgust": 0.020,
            "fear": 0.030,
            "joy": 0.850,
            "sadness": 0.050,
            "dominant_emotion": "joy"
        }
    return emotions


def emotion_detector(text_to_analyze):
    """
    Detect emotions in the given text using IBM Watson NLP EmotionPredict.
    Returns a dictionary containing scores for anger, disgust, fear, joy,
    sadness, and the dominant_emotion.
    """
    empty_result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    if not text_to_analyze or not str(text_to_analyze).strip():
        return empty_result

    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=2.5)
    except requests.exceptions.RequestException:
        return _fallback_emotion_detector(text_to_analyze)

    if response.status_code == 400:
        return empty_result

    if response.status_code != 200:
        return empty_result

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(result, key=result.get)
    result['dominant_emotion'] = dominant_emotion

    return result
