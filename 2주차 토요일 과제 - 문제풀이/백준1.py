a=int(input())
if(a>=1 and a<=1000000):
    count =1
    b=a
    x=0
    Bsum=[]
    while(int(b/10)>0):
        x+=b%10
        count+=1
        b/=10
    x+=b
    x=int(x)
    for i in range(a, int(a/2), -1):
        ans = i
        I = i
        if(x>=10):
                for j in range(count+1):
                    ans+=i%10
                    i=int(i/10)
                if ans==a:
                    Bsum.append(I)
        else:
                for j in range(count):
                    ans += i % 10
                    i=int(i/10)
                if ans == a:
                    Bsum.append(I)
    if Bsum is False:
        print(0)
    else:
        print(Bsum[-1])


