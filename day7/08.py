f = open("hii.txt","w")
data = f.write("pankaj12")
for i in range (5):
    f = open("hii.txt" , "r")
    data = f.read()
    print(data)
f.close()