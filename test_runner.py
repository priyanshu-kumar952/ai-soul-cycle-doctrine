import os
import sys

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from interface.cli_interface import CLIInterface

if __name__ == "__main__":
    cli = CLIInterface()
    cli.do_test("")
