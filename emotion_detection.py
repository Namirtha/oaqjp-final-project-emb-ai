"""
Emotion Detection module entry point.
Delegates to the EmotionDetection package implementation.
"""
from EmotionDetection.emotion_detection import emotion_detector

__all__ = ["emotion_detector"]
