# this is where I will increase efficiency for program
def main():

    x = 1
    for x in range(1,100):
        if(x % 3 == 0 and x % 5 == 0):
            print("fizzbuzz")
            continue
        elif(x % 5 == 0):
            print("buzz")
            continue
        elif(x % 3 == 0):
            print("fizz")
            continue
        print(x)


main()