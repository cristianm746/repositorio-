def mostrar_menu():
    """Muestra el menú principal."""
    print("\nMenú de la Base de Datos de Autos")
    print("1. Mostrar todos los autos")
    print("2. Buscar autos por marca")
    print("3. Salir")

def mostrar_autos(autos):
    """Muestra la lista completa de autos."""
    print("\nLista de Autos:")
    for auto in autos:
        print(f"ID: {auto['ID']}, Marca: {auto['Marca']}, Modelo: {auto['Modelo']}, Año: {auto['Año']}, "
              f"Color: {auto['Color']}, Tipo: {auto['Tipo']}, Motor: {auto['Motor']}, "
              f"Transmisión: {auto['Transmisión']}, Kilometraje: {auto['Kilometraje']} km, Precio: ${auto['Precio']}")

def buscar_autos_por_marca(autos, marca_buscar):
    """Busca autos por una marca específica."""
    encontrados = [auto for auto in autos if auto["Marca"] == marca_buscar]
    if encontrados:
        print(f"\nAutos encontrados de la marca {marca_buscar}:")
        for auto in encontrados:
            print(f"ID: {auto['ID']}, Marca: {auto['Marca']}, Modelo: {auto['Modelo']}, Año: {auto['Año']}, "
                  f"Color: {auto['Color']}, Tipo: {auto['Tipo']}, Motor: {auto['Motor']}, "
                  f"Transmisión: {auto['Transmisión']}, Kilometraje: {auto['Kilometraje']} km, Precio: ${auto['Precio']}")
    else:
        print(f"\nNo se encontraron autos de la marca {marca_buscar}.")

def main():
    """Función principal del programa."""
    autos = [
        {"ID": 1, "Marca": "Toyota", "Modelo": "Corolla", "Año": "2023", "Color": "Blanco", "Tipo": "Sedán",
         "Motor": "1.8L", "Transmisión": "Automático", "Kilometraje": 5000, "Precio": 25000},
        {"ID": 2, "Marca": "Chevrolet", "Modelo": "Camaro", "Año": "2023", "Color": "Negro", "Tipo": "Coupé",
         "Motor": "6.2L", "Transmisión": "Manual", "Kilometraje": 3000, "Precio": 60000},
        {"ID": 3, "Marca": "Honda", "Modelo": "Civic", "Año": "2022", "Color": "Azul", "Tipo": "Sedán",
         "Motor": "1.5L", "Transmisión": "Automático", "Kilometraje": 12000, "Precio": 22000},
        {"ID": 4, "Marca": "BMW", "Modelo": "Serie 3", "Año": "2022", "Color": "Negro", "Tipo": "Sedán",
         "Motor": "2.0L", "Transmisión": "Automático", "Kilometraje": 15000, "Precio": 45000},
        {"ID": 5, "Marca": "Audi", "Modelo": "A4", "Año": "2022", "Color": "Blanco", "Tipo": "Sedán",
         "Motor": "2.0L", "Transmisión": "Manual", "Kilometraje": 18000, "Precio": 40000},
        {"ID": 6, "Marca": "Ford", "Modelo": "Mustang", "Año": "2023", "Color": "Rojo", "Tipo": "Coupé",
         "Motor": "5.0L", "Transmisión": "Manual", "Kilometraje": 8000, "Precio": 55000},
        {"ID": 7, "Marca": "Tesla", "Modelo": "Model 3", "Año": "2023", "Color": "Plateado", "Tipo": "Sedán",
         "Motor": "Eléctrico", "Transmisión": "Automático", "Kilometraje": 2000, "Precio": 45000},
        {"ID": 8, "Marca": "Volkswagen", "Modelo": "Golf", "Año": "2022", "Color": "Azul", "Tipo": "Hatchback",
         "Motor": "1.4L", "Transmisión": "Manual", "Kilometraje": 25000, "Precio": 20000},
        {"ID": 9, "Marca": "Mercedes", "Modelo": "Clase C", "Año": "2022", "Color": "Negro", "Tipo": "Sedán",
         "Motor": "2.0L", "Transmisión": "Automático", "Kilometraje": 16000, "Precio": 47000}
    ]
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            mostrar_autos(autos)
        elif opcion == "2":
            marca_buscar = input("\nIngresa la marca del auto que deseas buscar: ").capitalize()
            buscar_autos_por_marca(autos, marca_buscar)
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
