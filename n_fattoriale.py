def n_fattoriale(n):
    c=1; k=n-c ; g=[]; b=1
    while k>1:
        k=n-c
        c=c+1
        g.append(k)
    for x in g:
        x=int(x)
        b=x*b
    return b*n 

print(n_fattoriale(6))




        

            
