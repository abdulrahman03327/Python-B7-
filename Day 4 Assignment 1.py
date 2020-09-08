lower =1042000
upper =702648265
for i in range(lower,upper+1):
    num =i
    result=0
    n=len(str(i))
    while(i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10
    if num==result:
        print(num)
        break
