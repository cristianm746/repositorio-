

def generar_pascual(n):
    
    triángulo = []
    
    
    i = 0
    
   
    while i < n:
        
        fila = [1] * (i + 1)
        
        j = 1
        while j < i:
            fila[j] = triángulo[i-1][j-1] + triángulo[i-1][j]
            j += 1
        
        triángulo.append(fila)
        
       
        i += 1
    
    
    for fila in triángulo:
        print(" ".join(map(str, fila)).center(n * 2))

n = int(input("Introduce el número de filas para el Triángulo de Pascal: "))
generar_pascual(n)