# this is where I will increase efficiency for program
def main():

    x = 1
    while x < 101:
        if(x % 3 == 0):
            print("fizz")
        elif(x % 5 == 0):
            print("buzz")
        elif(x % 5 == 0 and x % 3 == 0):
            print("fizzbuzz")
        else:
            print(x)
        x += 1


main()