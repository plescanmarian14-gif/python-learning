def fibonaci(lim):
    a,b=0,1
    while a<=lim:
        yield a
        a,b=b,a+b
for num in fibonaci(50):
    print(num,end=" ")