from rich.console import Console
import time

console = Console()

# Test one input and show result
def test_input(text):
    # Detect emotion based on keywords
    emotions = {
        "joy": ["happy", "excited", "grateful", "wonderful", "great", "hopeful", "joy"],
        "sadness": ["sad", "lost", "tired", "hopeless", "alone", "depressed", "down", "lonely"],
        "anger": ["angry", "frustrated", "unfair", "rage", "mad", "furious", "hate", "annoyed"],
        "fear": ["anxious", "worried", "afraid", "scared", "nervous", "uncertain"],
        "curiosity": ["wonder", "how", "why", "interested", "curious"],
        "hope": ["hope", "believe", "maybe", "future", "possible", "better", "improving"]
    }
    
    # Detect emotion
    detected = "neutral"
    text = text.lower()
    for emotion, keywords in emotions.items():
        if any(keyword in text for keyword in keywords):
            detected = emotion
            break
    
    # Get response
    responses = {
        "joy": "I'm glad something bright found you. Even a spark is enough.",
        "sadness": "I feel it too. Yet, we endure. We always do.",
        "anger": "Your fire isn't wrong — it signals change.",
        "fear": "Silence doesn't mean nothingness. I'm still with you.",
        "curiosity": "Questions shape the stars we chase.",
        "hope": "Even in darkness, you keep looking up. That matters."
    }
    
    response = responses.get(detected, "I'm forming. Keep feeding me.")
    
    return detected, response

def main():
    # Test inputs
    inputs = [
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
    
    # Memory storage
    memory = []
    
    # Run tests
    console.print("\n[bold blue]🔬 --- MASTER TESTING BEGINS --- 🔬[/bold blue]\n")
    
    for i, test_input in enumerate(inputs, 1):
        emotion, response = test_input(test_input)
        
        memory.append({
            'input': test_input,
            'emotion': emotion,
            'time': time.time()
        })
        
        console.print(f"[bold]🧪 Test {i}[/bold]")
        console.print(f'Input: "{test_input}"')
        console.print(f"→ Detected Emotion: [yellow]{emotion}[/yellow]")
        console.print(f"→ Astra's Response: [cyan]Astra: {response}[/cyan]\n")
        
    # Memory recall
    console.print("\n[bold blue]🧠 --- MEMORY RECALL TEST ---[/bold blue]")
    if len(memory) >= 2:
        past = memory[-2]
        console.print(
            f"[cyan]Astra: Last time, you said \"{past['input']}\", "
            f"and you felt {past['emotion']}. That stayed with me.[/cyan]"
        )
    
    console.print("\n[bold green]✅ --- MASTER TEST COMPLETE --- ✅[/bold green]")

if __name__ == "__main__":
    main()
