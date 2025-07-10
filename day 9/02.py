while True:
    n = input("Enter a number: ")

    try:
        n = int (n)
        if n / 5:
            print("You can't divide by zero!")
    except Exception as e:
        print(f"Error - {e}")
