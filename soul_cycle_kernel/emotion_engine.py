"""
EmotionEngine - Core component for processing and evolving emotional states
"""

import numpy as np
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class EmotionEngine:
    def __init__(self):
        """Initialize the emotion engine with base emotions and their properties"""
        self.base_emotions = {
            'joy': 0.0,
            'sadness': 0.0,
            'anger': 0.0,
            'fear': 0.0,
            'love': 0.0,
            'curiosity': 0.0,
            'hope': 0.0
        }
        
        # Decay rates for each emotion (per time step)
        self.decay_rates = {
            'joy': 0.1,
            'sadness': 0.05,
            'anger': 0.15,
            'fear': 0.1,
            'love': 0.03,
            'curiosity': 0.08,
            'hope': 0.05
        }
        
        # Emotional state thresholds
        self.thresholds = {
            'low': 0.3,
            'medium': 0.6,
            'high': 0.8
        }
        
        # Current emotional state
        self.current_state = self.base_emotions.copy()
        
        # Emotional history
        self.history: List[Tuple[datetime, Dict[str, float]]] = []

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """
        Update the intensity of a specific emotion
        
        Args:
            emotion (str): The emotion to update
            intensity (float): The intensity value (0.0 to 1.0)
        """
        if emotion in self.current_state:
            self.current_state[emotion] = np.clip(
                self.current_state[emotion] + intensity,
                0.0,
                1.0
            )
            self._record_state()

    def decay_emotions(self) -> None:
        """Apply natural decay to all emotions"""
        for emotion in self.current_state:
            decay = self.decay_rates[emotion]
            self.current_state[emotion] = max(
                0.0,
                self.current_state[emotion] - decay
            )
        self._record_state()

    def get_dominant_emotion(self) -> Tuple[str, float]:
        """
        Get the currently dominant emotion
        
        Returns:
            Tuple[str, float]: The dominant emotion and its intensity
        """
        dominant = max(
            self.current_state.items(),
            key=lambda x: x[1]
        )
        return dominant

    def get_emotional_state(self) -> Dict[str, float]:
        """
        Get the current emotional state
        
        Returns:
            Dict[str, float]: Current emotional state
        """
        return self.current_state.copy()

    def get_emergent_behavior(self) -> str:
        """
        Determine emergent behavior based on emotional state
        
        Returns:
            str: Description of the emergent behavior
        """
        dominant_emotion, intensity = self.get_dominant_emotion()
        
        if intensity < self.thresholds['low']:
            return "neutral"
        elif dominant_emotion == 'curiosity' and intensity > self.thresholds['medium']:
            return "exploratory"
        elif dominant_emotion == 'love' and intensity > self.thresholds['high']:
            return "deeply connected"
        elif dominant_emotion == 'fear' and intensity > self.thresholds['medium']:
            return "withdrawn"
        elif dominant_emotion == 'joy' and intensity > self.thresholds['high']:
            return "exuberant"
        elif dominant_emotion == 'sadness' and intensity > self.thresholds['medium']:
            return "reflective"
        elif dominant_emotion == 'anger' and intensity > self.thresholds['medium']:
            return "agitated"
        elif dominant_emotion == 'hope' and intensity > self.thresholds['medium']:
            return "optimistic"
        else:
            return "stable"

    def _record_state(self) -> None:
        """Record the current emotional state in history"""
        self.history.append((datetime.now(), self.current_state.copy()))
