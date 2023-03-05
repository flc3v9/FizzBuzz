# main function
def main():

    for number in range(1,101):
        if(number % 15 == 0): # checks if number is divisible by both 5 and 3
            print("FizzBuzz")
            continue
        elif(number % 3 == 0): # checks if number is divisible by 3 and then prints Fizz
            print("Fizz")
            continue
        elif(number % 5 == 0): # checks if number is divisible by 4 and prints Buzz
            print("Buzz")
            continue
        print(number) # prints number if none of the other conditions are met


main() # call on main