marks1=int(input("enter marks 1"))
marks2=int(input("enter marks 2"))
marks3=int(input("enter marks 3"))

avg=(marks1+marks2+marks3)/3

if marks1>35 and marks2>35 and marks3>35:

    if avg>40 :
        print("pass")

    else:

        print("fail due to less avg")
else:   
    print("fail due to less marks")