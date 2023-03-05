# this is where I will increase efficiency for program
def main():

    for x in range(1,101):
        if(x % 15 == 0):
            print("fizzbuzz")
            continue
        elif(x % 3 == 0):
            print("fizz")
            continue
        elif(x % 5 == 0):
            print("buzz")
            continue
        print(x)


main()