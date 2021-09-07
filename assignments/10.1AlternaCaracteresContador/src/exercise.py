def main():
    #escribe tu código abajo de esta línea
    n=int(input())
    for i in range(1, n+1):
        if i%2==0:
            x="%"
        elif i%2!=0:
            x="#"
        print(str(i)+"-"+str(x))
    pass

if __name__=='__main__':   
    main()
