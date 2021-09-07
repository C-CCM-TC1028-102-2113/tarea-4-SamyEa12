def main():
    #escribe tu código abajo de esta línea
    num=float()
    suma=0
    n=0
    while num>=0:
        num=float(input())
        if num>0:
            suma=suma+num
            n=n+1
        elif num<=0:
            promedio=suma/n
            print(promedio)
    pass
if __name__=='__main__':
    main()
