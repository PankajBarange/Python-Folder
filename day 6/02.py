def marks(num):
    if( num<50):
        print("below average")
        
    elif(num>50 and num<=65):
        print("average marks")

    elif(num>65 and num<=85):
        print("good")

    elif(num>85):
        print("excellent")
    return (num)

def main():
       num=int(input("enter the marks"))
       result=marks(num)
       print(f"the marks:{result}")
main()