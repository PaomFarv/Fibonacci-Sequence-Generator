def fibo_seq(n):
    base1 = 0
    base2 = 1

    for _ in range(n):
        print(base1)
        next_num = base1 + base2
        base1 = base2
        base2 = next_num

print("Welcome to the Fibonacci Sequence Generator.")
print("Written by PaomFarv.")
print("\nEnter 'S' to Start.")
print("Enter 'Q' to Quit.")

while True:
    user_response = input("Type in your response here (S,Q): ").upper().strip()
    if user_response == 'S':
        n = int(input("Fibonacci numbers upto: "))   
        print("Here they are: ")
        fibo_seq(n)

    elif user_response == 'Q':
        print("You have exited the program.")
        break

    else:
        print("Invalid Input.Please try again.")