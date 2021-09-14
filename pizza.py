#Nemo van de velde, opdracht pizza calculator.
print('Welcome to the pizzaria')
def myChoice(): # de function for the choice
    choice = input('In this pizza house we sell Small , Meduim, Large pizza\'s please select it with either number 1-3: ')
    # Choice = the variable which will select which one will be chosen

    if choice == "1":
        print('The small pizza will be 9 inches, and it will cost you 3$')
        global a
        a = int(3)
    elif choice == "2":
        print('The medium pizza wil be 12 inches, and it will cost you 5$')
        global a
        a = int(5)
    elif choice == "3":
        print('The large pizza is 14 inches, and it will cost you 8$')
        global a
        a = int(8)
        # The choices that are possible 1,2,3. and changes the value of A which will be used to calculate the price of more than 1 pizza

    else:
        print('Please input a number between 1 and 3')
        myChoice() # If it is something > 3 it will run the function again
myChoice() 
    #Als het niet een van deze nummers is word de klant gevraagd om een keuze tussen 1 en 3 te maken
b = input('How many pizza\'s would you like to order? ')
#----------------------------------------------------------------------------
c = ((int(b)) * (a))
print (int(c))
print (str(c) + '$ will be your total amount')
# De prijs uitrekenen voor de hoeveelheid pizza's ^
Confirm = input('are you sure? Y/N: ')
if Confirm =="y":
    price = True
    print('Your order has been completed')
elif Confirm =="n":
    price = False
    print('Your order has been canceled')
else:
    print('Please enter y or n')
    # It will give the user the last chance to cancel their order.
