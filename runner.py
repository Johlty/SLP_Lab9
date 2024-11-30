import sys
from Class.Runner import Runner
from Functions.logging_setup import setup_logging

sys.path.append('E:/SC Python')

setup_logging()

if __name__ == "__main__":
    runner = Runner()
    while True:
        runner.show_menu()
