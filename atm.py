class Atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def checkBalance(self):
        print("Your balance is 200")

    def withdrawl(self, amount):
        newAmount = 200 - amount
        print("You have withdrawn amount " + str(amount) + ". Your remaining balance or debt is " + str(newAmount) + ".")

def main():
    cardNumber = input("Insert your card number: ")
    pinNumber  = input("Enter your pin number: ")

    newUser =  Atm(cardNumber, pinNumber)

    print("Choose your activity")
    print("1. Balance Enquriy, 2. Withdrawl")
    activity = int(input("Enter activity number : "))

    if (activity == 1):
        newUser.checkBalance()
    elif (activity == 2):
        amount = int(input("Enter the amount: "))
        newUser.withdrawl(amount)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()