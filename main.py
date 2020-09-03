import random as ran

global count

i=1
r_num = ran.randrange(0,10)

def randomnumber():
    count = 3
    while i<=count:
        n = int(input("Enter the number : "))

        if i<count:
            if n == r_num:
                print("YAY! you got it right.")
                print("CONGRATULATIONS...!!!!!")
                break
            elif n < r_num:
                print("OOOPS! wrong answer.. Try again.")
                print("Your guess is smaller than generated number. ")

            elif n > r_num:
                print("OOOPS! wrong answer.. Try again.")
                print("Your guess is smaller than generated number. ")
            count-=1
            print("Chances Left", count)
            print("---------------------------------------------------")
        else:
            print("LOL....Better Luck Next Time")
            print("Generated number is : ",r_num)
            break

randomnumber()