import requests

def emotion_detector(text_to_analyse: str) -> str:

    default_result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    if not text_to_analyse:
        return default_result

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json = { "raw_document": { "text": text_to_analyse } }
    
    try:
        response = requests.post(
            url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
            headers=headers,
            json=json_payload
        )

        # Check for 400 status code
        if response.status_code == 400:
            return default_result

        response.raise_for_status()
        data = response.json()

        predictions = data['emotionPredictions'][0]['emotion']
        return {
            'anger': predictions['anger'],
            'disgust': predictions['disgust'],
            'fear': predictions['fear'],
            'joy': predictions['joy'],
            'sadness': predictions['sadness'],
            'dominant_emotion': max(predictions, key=predictions.get)
        }

    except Exception:
        return default_result