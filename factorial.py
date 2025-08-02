
def factorial(number):
    if (number < 0):
        return("Value should not be negative")

    elif (0 <= number <= 1):
        return (1)
    
    else :
        fact = 1
        for i in range(1, number+1):
            fact *= i
        return(fact)


if __name__ == "__main__":
    try: 

        number = int(input("Enter number:"))
        result = factorial(number)
        print(result)



    except ValueError:
        print("Please enter valid integer.")




        

    

