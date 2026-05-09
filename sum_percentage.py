m=list(map(int,input("Enter the Marks").split()))
n=len(m)
total=sum(m)
percentage=(total/(n*100))*100
print(total)
print(percentage)
