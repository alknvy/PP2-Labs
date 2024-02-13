# task 1. convert grams to ounces
def grams_to_ounces(x):
    return 28.3495231 * x


grams = 10
ounces = grams_to_ounces(grams)
print(ounces)

# task 2. Read in Farenheit temperature
def f_to_c(f):
    return (5.0/9.0) * (f - 32)


f = 99
c = f_to_c(f)

print(c)

# task 3. Create a func that solves puzzle
def solve(numheads, numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns
numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print(solutions)

# task 4. Function which will take only prime numbers from the list.
def filter_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_primes(lst):
    return [num for num in lst if filter_prime(num)]


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_primes(my_list)
print(prime_numbers)

def print_permutations():
    string = input("Enter a string: ")
    perms = print_permutations(string)
    print("All permutations of the string:")
    for perm in perms:
        print(''.join(perm))
print_permutations()
#6
def reverse_sentence():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
reversed_sentence = reverse_sentence()
print("Reversed sentence:", reversed_sentence)
#7
def has_adjacent_3(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
nums1 = [1, 3, 3, 5, 6]
print(has_adjacent_3(nums1))
#8
def contains_007(nums):
    pos_0 = -1
    pos_1 = -1
    pos_2 = -1

    for i, num in enumerate(nums):
        if num == 0:
            if pos_0 == -1:
                pos_0 = i
            elif pos_1 == -1:
                pos_1 = i
            elif pos_2 == -1:
                pos_2 = i
        elif num == 7:
            if pos_2 != -1 and pos_1 != -1 and pos_0 != -1:
                return True
    
    return False
spy_game=[1,2,4,0,0,7,5]
print(contains_007(spy_game))
#9
import math
def volume(r):
    return pow(r,3)*(4/3)*math.pi
r=float(input())
print(volume(r))
#10
def unique_elements(input_list):
    # Create an empty list to store unique elements
    unique_list = []
    # Iterate through the input list
    for item in input_list:
        # Check if the element is not already in the unique list
        if item not in unique_list:
            # Add the element to the unique list
            unique_list.append(item)

    return unique_list
original_list = [1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 7]
unique_list = unique_elements(original_list)
print("Original List:", original_list)
print("Unique Elements List:", unique_list)
#11
def is_palindrome(word):
    # Remove spaces and convert to lowercase
    word = word.replace(" ", "").lower()
    # Check if the word is equal to its reverse
    return word == word[::-1]
word=input()
print(is_palindrome(word))
#12
def histogram(numbers):
    for num in numbers:
        # Print '*' num times to represent the value
        print('*' * num)
#13
import random

def guess_the_number():
    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)

    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    num_guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        num_guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break

# Run the game
if __name__ == "__main__":
    guess_the_number()
