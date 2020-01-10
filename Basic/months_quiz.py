#Self exercise using list, loops, and conditional statement
"Ask the users to type any big months, which has 31days. If she gets wrong, the question will be keep repeated."

def main():

    while(True):
        a = input("Enter any big Months: ")

        bigMonths = ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]
        smallMonths = ["Feb", "Apr", "Jun", "Sep", "Nov"]

        if a in bigMonths:
            print("Correct!")
            break
        else:
            print("Try again!")


if __name__ == "__main__":
    main()