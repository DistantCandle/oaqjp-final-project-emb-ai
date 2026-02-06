"""
server.py

Flask web application for emotion detection.
Provides a /emotionDetector endpoint to analyze text and return emotion scores.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Render the home page of the emotion detection app.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handle GET requests to /emotionDetector.

    Retrieves the textToAnalyze query parameter from the request,
    calls the emotion_detector function to analyze emotions, 
    and returns a formatted response.

    Returns:
        str: Formatted emotion scores and dominant emotion,
             or an error message for invalid/blank input.
    """

    text_to_analyze = request.args.get("textToAnalyze")

    # Call the emotion detector
    result = emotion_detector(text_to_analyze)

    # Handle blank or invalid input
    if result is None:
        return "Invalid empty text! Please try again!"
    if result.get("label") is None:
        return "Invalid text! Please try again!"

    # Format response as requested
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['label']}."
    )

    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
