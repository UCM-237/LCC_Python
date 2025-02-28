#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:20:07 2025
Middle Square method to generate psudo-random numbers
@author: chapgpt
@Juan: Beware: the function do not check the number of digits of the seed.
So is up to the user to introduce a seed with the proper size
"""
def middle_square(seed, num_digits, num_iterations):
    # Initialize the current number with the seed
    current_number = seed
    
    # List to store the random numbers generated
    random_numbers = []
    
    for _ in range(num_iterations):
        # Square the current number
        squared = current_number * current_number
        
        # Convert squared number to string to extract middle digits
        # Calculate the number of digits in the squared result
        squared_str = str(squared)
        
        # Calculate the start and end index for the middle digits
        mid_start = (len(squared_str) - num_digits) // 2
        mid_end = mid_start + num_digits
        
        # Extract the middle digits (as integer)
        middle_digits = int(squared_str[mid_start:mid_end])
        
        # Add the middle digits to the list of random numbers
        random_numbers.append(middle_digits)
        
        # Update current_number to the middle digits for the next iteration
        current_number = middle_digits
    
    return random_numbers

# Example usage
seed = 3708  # Initial seed
num_digits = 4  # Number of digits to extract as the random number
num_iterations = 10  # Number of iterations to generate

random_sequence = middle_square(seed, num_digits, num_iterations)
print("Random Sequence:", random_sequence)