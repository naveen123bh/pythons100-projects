import random 
print("hii you have 7 chances to guess.\n lets start")
low = int(input("inter the lower bound: "))
high = int(input("inter the higher bound: "))
print(f"you have 7 chances to guess the number between {low} and {high}")
num = random.randint(low, high)
ch = 7
gc = 0
while gc < ch:
    gc += 1
    guess = int(input("inter your guess"))
    if guess==num:
        print(f'correct! the number is {num}.you guess it in {gc}attempts')
        break

    elif gc >= ch and guess != num:
        print(f'sorry better luck next time. the number was {num}')
    elif guess > num:
        print('too high inter a lower number ')
    elif guess<num:
        print('too low try higher number')
        

