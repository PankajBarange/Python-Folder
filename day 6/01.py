def authenticate(pw):
    if pw == 1234:
     print("correct")

    else:
     print("invalid")


def main():
       pw=int(input("enter the password"))
       result=authenticate(pw)
       print(f"the password:{result}")
main() 