
num=(1,4,9,16,25,36,49,64,81,100)

x=int(input("enter a number: "))

i=0
while i<len(num):
    if(num[i]==x):
        print("Found at idx", i)
    else:
        print("finding...")
    i+=1