ls=[]
texto=True
contador=0

def prom (mensaje: str):
    global contador
    if mensaje!='0':
        for letra in mensaje:
            if letra.isnumeric() and letra!='0':
                ls.append(int(letra))
                contador+=1
        
        if mensaje=='0':
            print(f"El promedio es: {sum(ls)/contador}")

