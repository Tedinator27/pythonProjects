'''
This program is supposed to simulate multiple coin flips. The user will be able to input the
amount of times that the coin will be flipped. The program will then be able to print out the
possible outputs of this coin flipping simulation/ It will also tell the user how many times
heads and tails are produced
'''

import random

def coinFlips():
    randomNum = random.randint(0, 1)
    if randomNum == 0:
        return "H"
    else:
        return "T"

def main():
    print("Welcome to Ted's Coin Flipping Simulator!")
    print("")
    numFlips = int(input("Please enter the number of times you want the coin to flip: "))

    heads_count = 0
    tails_count = 0

    for i in range(numFlips):
        result = coinFlips()
        if result == "H":
            heads_count += 1
        else:
            tails_count += 1
        print(result)

    print(f"Total Heads: {heads_count}")
    print(f"Total Tails: {tails_count}")

if __name__ == "__main__":
    main()

