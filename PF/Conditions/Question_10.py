# ATM Menu (match-case + if-else)
# Suppose a user has Rs. 50,000 in their account.
# Display this menu:
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
# Requirements:
# Use match-case for the menu.
# Use if-else to:
# Prevent withdrawing more than the available balance.
# Reject negative deposits.
# Update the balance correctly.
# Example:
# Choice: 3
# Amount: 60000
#
# Output:
# Insufficient Balance

money = 50000
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")
menu = int(input("Enter your Choice: "))
match menu:
    case 1:
        print(f"The Remaining balance in Account is: {money}")
    case 2:
        dep = int(input("Enter money you want to deposit: "))
        print(f"Your updated money is: {money + dep}")
    case 3:
        withd = int(input("Enter money you want to Withdraw: "))
        if withd > money:
            print("Insufficent Balance")
        else:
            print(f"Remaining balance is: {money - withd}")
    case 4:
        pass