# this is the code for the fizz buzz challange


def main():

    x=1

    while (x < 101):
        if(x % 15 == 0):
            print("fizzbuzz")
            x+=1
            continue
        elif(x % 5 == 0):
            print("buzz")
            x+=1
            continue
        elif(x % 3 == 0):
            print("fizz")
            x+=1
            continue
        else:
            print(x)
            x+=1


main()

# program works sucessfully, time to improve efficiency