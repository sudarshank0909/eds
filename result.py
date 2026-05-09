a=list(map(int,input("Enter Marks : ").split(','))) #we can use ' ' as well as the ',' for split function.
total = a[0]+a[1]+a[2]+a[3]+a[4]
p=(total/500)*100
if(a[0]>=40 and a[1]>=40 and a[2]>=40 and a[3]>=40 and a[4]>=40 ) :
    print("Pass")
    if(p>=75) :
        print("Distinction")
    elif(p<75 and p>=60) :
        print("First Division")
    elif(p<60 and p<=50) :
        print("Second Division")
    else :
        print("Third Division")
else :
    print("Fail")

    
