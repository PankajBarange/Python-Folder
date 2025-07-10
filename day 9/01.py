while True:
    a = input("Enter Your Value: ")

    if a == 'q':
        break

    try:
        a = int(a)
        if a > 5:
            print("Greater Then 5")
    except Exception as e:
        print(f"Error - {e}")


print("Thanks for playing this game!")
