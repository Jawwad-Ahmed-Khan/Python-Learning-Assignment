import random

# Define the probability of stopping early
DONE_LIKELIHOOD = 0.3  # 30% chance of stopping

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # This ends function execution early
        print(curr_num)

# Function to randomly decide whether to stop
def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
