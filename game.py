# guess a number
import numpy as np

number = np.random.randint(1,101) # generate a number
count = 0

while True:
    count += 1
    predict_number = int(input("guess a number in a range from 1 to 100"))
    
    if predict_number > number:
        print("number should be less")
        
    elif predict_number < number:
        print("number should be geater")
    
    else:
        print(f"Your guessed the number {number} for {count} tries")
        break