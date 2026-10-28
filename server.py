"""
Flask server for the Emotion Detection application.
This module provides a web interface to analyze emotions in text.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyze the emotion of the given text and return a formatted response.
    Returns a string with emotion scores and the dominant emotion,
    or an error message if the input is blank or invalid.
    """
    # Get the text to analyze from the request
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    # Handle blank or invalid input — dominant_emotion is None when status_code was 400
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the output as required
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


@app.route("/")
def render_index_page():
    """
    Render the index page of the Emotion Detection application.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    