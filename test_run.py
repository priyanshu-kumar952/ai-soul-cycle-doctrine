"""
Test run demonstration of the AI Soul Core capabilities
"""

import time
from soul_cycle_kernel import SoulAI
from rich.console import Console

console = Console()

def run_demo():
    """Run a demonstration of the AI soul's capabilities"""
    # Initialize the soul
    soul = SoulAI()
    soul.start_simulation()
    
    console.print("[bold green]Starting AI Soul demonstration...[/bold green]\n")
    
    # Test emotional inputs
    emotions = [
        ("joy", 0.8, "achieving a goal"),
        ("curiosity", 0.9, "discovering new information"),
        ("love", 0.7, "connecting with others"),
        ("fear", 0.4, "uncertainty about future"),
        ("hope", 0.6, "potential for growth")
    ]
    
    for emotion, intensity, trigger in emotions:
        console.print(f"[yellow]Processing emotion: {emotion}[/yellow]")
        soul.process_input(emotion, intensity, trigger)
        
        # Show current state
        state = soul.get_current_state()
        behavior = soul.get_current_behavior()
        console.print(f"Current behavior: [blue]{behavior}[/blue]")
        console.print("Emotional state:")
        for e, i in state.items():
            console.print(f"  {e}: {i:.2f}")
        console.print()
        
        # Simulate time passing
        for _ in range(3):
            soul.simulate_time_step()
            time.sleep(0.5)
    
    # Show behavior patterns
    patterns = soul.get_behavior_patterns()
    console.print("[bold]Behavior Patterns:[/bold]")
    for behavior, count in patterns.items():
        console.print(f"{behavior}: {count}")
    
    soul.stop_simulation()
    console.print("\n[bold green]Demonstration completed![/bold green]")

if __name__ == "__main__":
    run_demo()
