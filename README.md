# AI Soul Core

A sophisticated AI simulation project that models emotional evolution and memory persistence in artificial consciousness.

## Overview

AI Soul Core is a Python-based simulation that creates and evolves a synthetic soul-like entity. It models emotions, stores emotional memory over time, and simulates the evolution of an AI's emotional state through various interactions and time cycles.

## Features

- Emotion Engine: Models and evolves emotions based on input and prior states
- Memory System: Persistent storage of emotional history
- Simulation Engine: Time-based evolution of emotional states
- CLI Interface: Interactive command-line interface for user interactions
- Logging System: Detailed logging of state changes and decisions

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main simulation:
```bash
python main.py
```

Run test demonstration:
```bash
python test_run.py
```

## Project Structure

```
ai_soul_core/
├── soul_cycle_kernel/
│   ├── __init__.py
│   ├── emotion_engine.py
│   ├── memory_system.py
│   └── simulation_engine.py
├── interface/
│   ├── __init__.py
│   └── cli_interface.py
├── main.py
├── test_run.py
├── requirements.txt
├── README.md
└── log.txt (auto-generated)
```

## License

MIT License

## Author

Created with GitHub Copilot
