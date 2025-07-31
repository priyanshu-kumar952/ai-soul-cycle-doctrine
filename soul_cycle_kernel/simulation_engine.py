"""
SimulationEngine and SoulAI - Core simulation components for the AI soul
"""

import time
import logging
from datetime import datetime
from typing import Dict, Optional, List, Tuple

from .emotion_engine import EmotionEngine
from .memory_system import MemorySystem

# Configure logging
logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SimulationEngine:
    def __init__(self, tick_duration: float = 1.0):
        """
        Initialize the simulation engine
        
        Args:
            tick_duration (float): Duration of each simulation tick in seconds
        """
        self.tick_duration = tick_duration
        self.current_tick = 0
        self.running = False

    def start(self) -> None:
        """Start the simulation"""
        self.running = True
        logging.info("Simulation started")

    def stop(self) -> None:
        """Stop the simulation"""
        self.running = False
        logging.info("Simulation stopped")

    def tick(self) -> None:
        """Process one simulation tick"""
        self.current_tick += 1
        time.sleep(self.tick_duration)

    def is_running(self) -> bool:
        """Check if simulation is running"""
        return self.running

    def get_current_tick(self) -> int:
        """Get current simulation tick"""
        return self.current_tick

class SoulAI:
    def __init__(self):
        """Initialize the AI soul components"""
        self.emotion_engine = EmotionEngine()
        self.memory_system = MemorySystem()
        self.simulation = SimulationEngine()
        
        logging.info("SoulAI initialized")

    def process_input(self, emotion: str, intensity: float, 
                     trigger: Optional[str] = None) -> None:
        """
        Process emotional input
        
        Args:
            emotion (str): The emotion to process
            intensity (float): Intensity of the emotion (0.0 to 1.0)
            trigger (Optional[str]): What triggered this emotion
        """
        # Update emotional state
        self.emotion_engine.update_emotion(emotion, intensity)
        
        # Get current state and behavior
        state = self.emotion_engine.get_emotional_state()
        behavior = self.emotion_engine.get_emergent_behavior()
        
        # Store in memory
        self.memory_system.store_emotional_state(state, behavior, trigger)
        
        # Log the event
        logging.info(
            f"Processed emotion: {emotion} (intensity: {intensity:.2f})"
            f" - Behavior: {behavior}"
        )

    def simulate_time_step(self) -> None:
        """Simulate one time step in the soul's evolution"""
        if not self.simulation.is_running():
            return
            
        # Natural emotion decay
        self.emotion_engine.decay_emotions()
        
        # Get current state
        state = self.emotion_engine.get_emotional_state()
        behavior = self.emotion_engine.get_emergent_behavior()
        
        # Store state
        self.memory_system.store_emotional_state(state, behavior, "time_decay")
        
        # Increment simulation tick
        self.simulation.tick()
        
        # Log the time step
        logging.info(
            f"Time step {self.simulation.get_current_tick()} - "
            f"Behavior: {behavior}"
        )

    def get_current_state(self) -> Dict[str, float]:
        """Get current emotional state"""
        return self.emotion_engine.get_emotional_state()

    def get_current_behavior(self) -> str:
        """Get current emergent behavior"""
        return self.emotion_engine.get_emergent_behavior()

    def get_emotional_history(self, emotion: str) -> List[Dict]:
        """Get history for a specific emotion"""
        return self.memory_system.get_emotional_history(emotion)

    def get_behavior_patterns(self) -> Dict[str, int]:
        """Get behavior pattern statistics"""
        return self.memory_system.get_behavior_patterns()

    def start_simulation(self) -> None:
        """Start the soul simulation"""
        self.simulation.start()
        logging.info("Soul simulation started")

    def stop_simulation(self) -> None:
        """Stop the soul simulation"""
        self.simulation.stop()
        logging.info("Soul simulation stopped")
