"""
Main entry point for the AI Soul Core simulation
"""

from interface.cli_interface import CLIInterface
import time

def run_test():
    """Run test sequence"""
    cli = CLIInterface()
    print('\nRunning test sequence...\n')
    
    cli.do_start('')
    time.sleep(1)
    
    cli.do_feel('love 0.9')
    time.sleep(1)
    
    cli.do_feel('anger 0.4')
    time.sleep(1)
    
    cli.do_feel('curiosity 0.7')
    time.sleep(1)
    
    cli.do_state('')
    time.sleep(1)
    
    cli.do_patterns('')
    time.sleep(1)
    
    cli.do_simulate('5')
    time.sleep(1)
    
    cli.do_history('love')
    time.sleep(1)
    
    cli.do_stop('')
    time.sleep(1)
    
    print('\nTest sequence completed.')

if __name__ == "__main__":
    run_test()
