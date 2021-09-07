
def main():
    #escribe tu código abajo de esta línea
    num = int(input("Enter a number: "))
    x=0
    y=1
    z=int()
    a=1
    if num==0:
        print(x)
    while a<num:
        z=y+x
        x=y
        y=z
        a=a+1
        if a>=num:
            print(z)

if __name__=='__main__':
    main()
