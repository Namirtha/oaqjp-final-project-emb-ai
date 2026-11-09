# Final Project

## AI-Based Emotion Detection Application

A web application developed using Python, Flask, and Watson NLP for sentiment analysis and emotion detection. This project analyzes customer feedback and statements to determine emotion scores (anger, disgust, fear, joy, and sadness) and identifies the dominant emotion.

## Project Structure

```text
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py               # Package initialization exposing emotion_detector
│   └── emotion_detection.py      # Core detection logic and Watson NLP integration
├── static/
│   └── mywebscript.js            # Frontend JavaScript for AJAX requests
├── templates/
│   └── index.html                # Application user interface template
├── emotion_detection.py          # Root wrapper module
├── requirements.txt              # Project dependencies
├── server.py                     # Flask web server and routing
├── test_emotion_detection.py     # Unit test suite
└── README.md                     # Project documentation
```

## Prerequisites & Installation

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the Flask development server:
```bash
python server.py
```
Open your browser and navigate to:
```text
http://localhost:5000
```

## Running Unit Tests

Execute unit tests to verify emotion assertions:
```bash
python -m unittest test_emotion_detection.py
```

## Static Code Analysis (PyLint)

Verify code compliance against PEP 8 standards:
```bash
python -m pylint server.py
python -m pylint EmotionDetection
```
Expected score: **10.00/10**

## Error Handling

- Blank or invalid inputs are handled gracefully and return:
  ```text
  Invalid text! Please try again!
  ```
- Watson NLP `400` status codes return dictionary with `None` values for all emotion keys.
