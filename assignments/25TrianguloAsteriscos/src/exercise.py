
def main():
    #Escribe tu código debajo de esta línea
        height = int(input("Enter triangle height: "))
        for i in range(1, height+1):
            y="*"
            x=" "
            s=height-i
            print(str(s*x)+str(y*i))
    pass
if __name__=='__main__':
    main()
