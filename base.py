"""
Base template to be followed by every code file
"""

import time


def fun():
    pass


if __name__ == "__main__":
    start_time = time.process_time()
    # Code goes here

    end_time = time.process_time()

    print(f"CPU execution time: {end_time - start_time} seconds")
