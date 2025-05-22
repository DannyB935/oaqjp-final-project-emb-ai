"""
Flask server module for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__,
    template_folder='templates',
    static_folder='static'
    )

@app.route('/')
def index():
    """
    Renders the home page.
    """
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
        Function to handle requests to get the emotions from a text input
    """
    data = request.args.get("textToAnalyze")
    results = emotion_detector(data)

    if results['dominant_emotion'] is None:
        return 'Invalid text! Please try again!.'

    return (
        f"For the given statement, the system response is "
        f"'anger': {results['anger']}, 'disgust': {results['disgust']}, "
        f"'fear': {results['fear']}, 'joy': {results['joy']}, "
        f"and 'sadness': {results['sadness']}. "
        f"The dominant emotion is {results['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(debug=True)
