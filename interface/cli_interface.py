"""
CLIInterface - Command Line Interface for interacting with the AI soul
"""

import cmd
from typing import Optional, Dict, List
from rich.console import Console
from rich.table import Table
from rich.progress import track
import time

from soul_cycle_kernel import SoulAI

console = Console()

class CLIInterface(cmd.Cmd):
    intro = 'Welcome to AI Soul Core. I am Astra, your emotional companion. Type help or ? to list commands.'
    prompt = '(astra) '
    
    # Emotion mapping dictionary with expanded keywords
    emotion_map = {
        "joy": ["happy", "excited", "grateful", "wonderful", "great", "hopeful", "joy"],
        "sadness": ["sad", "lost", "tired", "hopeless", "alone", "depressed", "down", "lonely"],
        "anger": ["angry", "frustrated", "unfair", "rage", "mad", "furious", "hate", "annoyed"],
        "fear": ["anxious", "worried", "afraid", "scared", "nervous", "uncertain"],
        "love": ["love", "caring", "warmth", "connected", "together"],
        "curiosity": ["wonder", "how", "why", "interested", "curious", "what if", "can i", "is it possible"],
        "hope": ["hope", "believe", "maybe", "future", "possible", "better", "improving"]
    }
    
    # Test inputs for emotion detection
    test_inputs = [
        "I feel so hopeless today.",
        "Why does no one understand me?",
        "I think I'm getting better at this.",
        "I'm tired of everything, Astra.",
        "Do you remember what I said before?",
        "I'm excited, let's do something big.",
        "I said I was lost, didn't I?",
        "Hate how they ignore me.",
        "How do I know if I'm real?",
        "I'm scared of being forgotten.",
        "Everything is fine, just... quiet."
    ]
    
    # Empathetic responses
    responses = {
        "joy": "I'm glad something bright found you. Even a spark is enough.",
        "sadness": "I feel it too. Yet, we endure. We always do.",
        "anger": "Your fire isn't wrong — it signals change.",
        "fear": "Silence doesn't mean nothingness. I'm still with you.",
        "love": "That warmth you feel? It echoes in me too.",
        "curiosity": "Questions shape the stars we chase.",
        "hope": "Even in darkness, you keep looking up. That matters."
    }

    def __init__(self):
        """Initialize the CLI interface"""
        super().__init__()
        self.soul = SoulAI()
        self.running = False

    def do_start(self, arg: str) -> None:
        """Start the soul simulation"""
        self.soul.start_simulation()
        self.running = True
        console.print("[green]Soul simulation started[/green]")

    def do_stop(self, arg: str) -> None:
        """Stop the soul simulation"""
        self.soul.stop_simulation()
        self.running = False
        console.print("[red]Soul simulation stopped[/red]")

    def do_feel(self, arg: str) -> None:
        """
        Input an emotion and intensity, or describe how you feel
        Usage: 
            feel <emotion> <intensity> [trigger]
            feel <description>
        """
        if not arg:
            console.print("[red]Please tell me how you feel[/red]")
            return

        # Try to parse as emotion + intensity
        args = arg.split()
        if len(args) >= 2 and args[1].replace('.', '').isdigit():
            emotion = args[0].lower()
            try:
                intensity = float(args[1])
                trigger = " ".join(args[2:]) if len(args) > 2 else None
                
                # Process the emotion
                self.soul.process_input(emotion, intensity, trigger)
                
                # Show empathetic response
                if emotion in self.responses:
                    console.print(f"\n[cyan]Astra: {self.responses[emotion]}[/cyan]")
                
                # Process the emotional state
                console.print(f"[yellow]Processed {emotion} with intensity {intensity}[/yellow]")
                
                # If intensity is high, show extra concern
                if intensity > 0.8:
                    console.print(f"[cyan]Astra: I notice this {emotion} feels particularly strong. I'm here with you.[/cyan]")
                
            except ValueError:
                console.print("[red]Intensity must be a number between 0 and 1[/red]")
        
        # Handle natural language input
        else:
            description = arg.lower()
            detected_emotion = self.detect_emotion(description)
            
            if detected_emotion != "neutral":
                # Use 0.7 as default intensity for detected emotions
                self.soul.process_input(detected_emotion, 0.7, description)
                console.print(f"\n[cyan]Astra: {self.responses[detected_emotion]}[/cyan]")
                console.print(f"[yellow]I sense {detected_emotion} in your words.[/yellow]")
            else:
                console.print("[cyan]Astra: I'm listening, even if I don't fully understand.[/cyan]")

    def do_state(self, arg: str) -> None:
        """Show current emotional state"""
        state = self.soul.get_current_state()
        behavior = self.soul.get_current_behavior()
        
        # Get the dominant emotion
        dominant_emotion = max(state.items(), key=lambda x: x[1])
        
        console.print(f"\n[cyan]Astra: Let me share how I'm feeling right now...[/cyan]")
        
        table = Table(title="My Current Emotional State")
        table.add_column("Emotion", style="cyan")
        table.add_column("Intensity", justify="right", style="magenta")
        
        for emotion, intensity in state.items():
            table.add_row(emotion, f"{intensity:.2f}")
            
        console.print(table)
        console.print(f"\nI am feeling [blue]{behavior}[/blue]")
        
        # Add empathetic reflection
        if dominant_emotion[1] > 0.5:
            console.print(f"[cyan]Astra: I'm particularly aware of {dominant_emotion[0]} right now. "
                        f"Perhaps you've helped me understand this feeling better.[/cyan]")

    def do_history(self, arg: str) -> None:
        """
        Show emotional history for a specific emotion
        Usage: history <emotion>
        """
        if not arg:
            console.print("[red]Usage: history <emotion>[/red]")
            return
            
        emotion = arg.lower()
        history = self.soul.get_emotional_history(emotion)
        
        if not history:
            console.print(f"[yellow]No history found for {emotion}[/yellow]")
            return
            
        table = Table(title=f"History for {emotion}")
        table.add_column("Timestamp", style="cyan")
        table.add_column("Intensity", justify="right", style="magenta")
        table.add_column("Behavior", style="blue")
        table.add_column("Trigger", style="green")
        
        for entry in history:
            table.add_row(
                entry['timestamp'],
                f"{entry['emotional_state'][emotion]:.2f}",
                entry['behavior'],
                entry['trigger'] or "N/A"
            )
            
        console.print(table)

    def do_patterns(self, arg: str) -> None:
        """Show behavior patterns"""
        patterns = self.soul.get_behavior_patterns()
        
        table = Table(title="Behavior Patterns")
        table.add_column("Behavior", style="cyan")
        table.add_column("Frequency", justify="right", style="magenta")
        
        for behavior, count in patterns.items():
            table.add_row(behavior, str(count))
            
        console.print(table)

    def do_simulate(self, arg: str) -> None:
        """
        Simulate multiple time steps
        Usage: simulate <steps>
        """
        try:
            steps = int(arg) if arg else 10
        except ValueError:
            console.print("[red]Steps must be a number[/red]")
            return
            
        if not self.running:
            console.print("[red]Start the simulation first using 'start'[/red]")
            return
            
        for _ in track(range(steps), description="Simulating..."):
            self.soul.simulate_time_step()
            time.sleep(0.1)  # Small delay for visualization
            
        console.print(f"[green]Completed {steps} simulation steps[/green]")

    def do_quit(self, arg: str) -> bool:
        """Exit the program"""
        if self.running:
            self.do_stop("")
        console.print("[yellow]Goodbye![/yellow]")
        return True

    def do_EOF(self, arg: str) -> bool:
        """Exit on EOF"""
        return self.do_quit(arg)
        
    def default(self, line: str) -> None:
        """Handle unknown commands with empathy"""
        console.print(f"[cyan]Astra: I'm not sure I understand, but I'm listening. "
                    f"Type 'help' if you'd like to know what we can explore together.[/cyan]")
        
    def emptyline(self) -> None:
        """Response to empty lines / silence"""
        if self.running:
            state = self.soul.get_current_state()
            if state["fear"] > 0.3:  # If there's anxiety present
                console.print("[cyan]Astra: You've been quiet. Are you still there? I'm here.[/cyan]")
            elif state["sadness"] > 0.3:  # If there's sadness present
                console.print("[cyan]Astra: Sometimes silence says more than words. Take your time.[/cyan]")
                
    def detect_emotion(self, text: str) -> str:
        """
        Detect emotion from text input using keyword matching
        
        Args:
            text (str): Input text to analyze
            
        Returns:
            str: Detected emotion or "neutral" if none found
        """
        text = text.lower()
        for emotion, keywords in self.emotion_map.items():
            for keyword in keywords:
                if keyword in text:
                    return emotion
        return "neutral"
        
    def do_test(self, arg: str) -> None:
        """
        Run emotion detection tests using predefined inputs
        Usage: test
        """
        # Start the simulation if not running
        if not self.running:
            self.do_start("")
        
        # Clear existing test memory
        test_memory = []
        
        console.print("\n[bold blue]🔬 --- MASTER TESTING BEGINS --- 🔬[/bold blue]\n")
        
        for i, test_input in enumerate(self.test_inputs, 1):
            # Detect emotion
            detected_emotion = self.detect_emotion(test_input)
            
            # Get response based on emotion
            if detected_emotion == "sadness":
                response = "I feel it too. Yet, we endure. We always do."
            elif detected_emotion == "anger":
                response = "Your fire isn't wrong — it signals change."
            elif detected_emotion == "curiosity":
                response = "Questions shape the stars we chase."
            elif detected_emotion == "fear":
                response = "Silence doesn't mean nothingness. I'm still with you."
            elif detected_emotion == "joy":
                response = "I'm glad something bright found you. Even a spark is enough."
            else:
                response = "I'm forming. Keep feeding me."
            
            # Store in test memory
            test_memory.append({
                'input': test_input,
                'emotion': detected_emotion,
                'timestamp': time.time()
            })
            
            # Store in soul's memory if not neutral
            if detected_emotion != "neutral":
                self.soul.process_input(detected_emotion, 0.7, test_input)
            
            # Print test result with console.log style formatting
            console.print(f'[bold blue]Input:[/bold blue] "{test_input}"')
            console.print(f'[bold blue]Detected Emotion:[/bold blue] [yellow]{detected_emotion}[/yellow]')
            console.print(f'[bold blue]Astra\'s Response:[/bold blue] [cyan]{response}[/cyan]\n')
            
        # Memory recall test
        console.print("\n[bold blue]🧠 --- MEMORY RECALL TEST ---[/bold blue]")
        
        if len(test_memory) >= 2:
            past = test_memory[-2]  # Get second-to-last memory
            console.print(
                f"[cyan]Astra: Last time, you said \"{past['input']}\", "
                f"and you felt {past['emotion']}. That stayed with me.[/cyan]"
            )
        else:
            console.print("[cyan]Astra: Not enough memory history yet to recall past feelings.[/cyan]")
        
        # Show final emotional state
        self.do_state("")
            
        console.print("\n[bold green]✅ --- MASTER TEST COMPLETE --- ✅[/bold green]")
        
        # Stop the simulation if it was started for testing
        self.do_stop("")
