a=int(input("Enter a number : "))
match a:
    case 0:
        print("You entered 0")
    
    case 1:
        print("You entered 1")

    case _ if(a>100):
        print("Default case entered. greater than 100")

    case _:
        print("Default")