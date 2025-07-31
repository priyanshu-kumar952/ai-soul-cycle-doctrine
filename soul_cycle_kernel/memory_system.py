"""
MemorySystem - Handles persistent storage and retrieval of emotional states
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path

class MemorySystem:
    def __init__(self, memory_file: str = "soul_memory.json"):
        """
        Initialize the memory system
        
        Args:
            memory_file (str): Path to the memory storage file
        """
        self.memory_file = memory_file
        self.memories: List[Dict[str, Any]] = []
        self._load_memories()

    def store_emotional_state(self, 
                            emotional_state: Dict[str, float],
                            behavior: str,
                            trigger: Optional[str] = None) -> None:
        """
        Store an emotional state with its context
        
        Args:
            emotional_state (Dict[str, float]): Current emotional state
            behavior (str): Current emergent behavior
            trigger (Optional[str]): What triggered this emotional state
        """
        memory = {
            'timestamp': datetime.now().isoformat(),
            'emotional_state': emotional_state,
            'behavior': behavior,
            'trigger': trigger
        }
        
        self.memories.append(memory)
        self._save_memories()

    def get_recent_memories(self, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieve recent memories
        
        Args:
            limit (int): Number of memories to retrieve
            
        Returns:
            List[Dict[str, Any]]: List of recent memories
        """
        return self.memories[-limit:]

    def get_emotional_history(self, emotion: str) -> List[Dict[str, Any]]:
        """
        Get history for a specific emotion
        
        Args:
            emotion (str): The emotion to track
            
        Returns:
            List[Dict[str, Any]]: History of the specified emotion
        """
        return [
            memory for memory in self.memories
            if memory['emotional_state'].get(emotion, 0) > 0.5
        ]

    def get_behavior_patterns(self) -> Dict[str, int]:
        """
        Analyze behavior patterns in memories
        
        Returns:
            Dict[str, int]: Frequency of each behavior
        """
        patterns = {}
        for memory in self.memories:
            behavior = memory['behavior']
            patterns[behavior] = patterns.get(behavior, 0) + 1
        return patterns

    def clear_memories(self) -> None:
        """Clear all stored memories"""
        self.memories = []
        self._save_memories()

    def _load_memories(self) -> None:
        """Load memories from storage file"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    self.memories = json.load(f)
            except json.JSONDecodeError:
                self.memories = []
        else:
            self.memories = []

    def _save_memories(self) -> None:
        """Save memories to storage file"""
        Path(self.memory_file).parent.mkdir(parents=True, exist_ok=True)
        with open(self.memory_file, 'w') as f:
            json.dump(self.memories, f, indent=2)
