import sys
import time
import threading

class Loader:
    def __init__(self, message):
        self.message = message
        # Sequence of Unicode characters for a circular spinner
        self.symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
        self.running = False
        self.thread = None

    def start(self):
        """Starts the loading animation in a separate thread."""
        self.running = True
        self.thread = threading.Thread(target=self._animate)
        self.thread.daemon = True # Allows program to exit even if thread is running
        self.thread.start()

    def stop(self, final_message="Done!"):
        """Stops the animation and prints a final message."""
        self.running = False
        if self.thread is not None:
            self.thread.join() # Wait for the thread to finish its current loop iteration
        # Clear the current line and print the final message
        sys.stdout.write('\r' + ' ' * (len(self.message) + 5) + '\r')
        sys.stdout.write(f'\r{final_message}\n')
        sys.stdout.flush()

    def _animate(self):
        """The core animation loop."""
        i = 0
        while self.running:
            # The '\r' character moves the cursor to the beginning of the line
            sys.stdout.write(f'\r{self.symbols[i]} {self.message}')
            sys.stdout.flush() # Ensure the output is immediately displayed
            i = (i + 1) % len(self.symbols) # Cycle through the symbols
            time.sleep(0.1) # Control animation speed

# Example Usage
if __name__ == '__main__':
    # 1. Initialize the loader
    loader = Loader("Loading data...")
    loader.start()

    # 2. Simulate a long-running process (replace with your actual task)
    try:
        time.sleep(5) # Your actual function or code goes here
    except KeyboardInterrupt:
        pass
    finally:
        # 3. Stop the loader when the task is complete
        loader.stop("Process complete!")
