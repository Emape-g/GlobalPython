from clases import Detector, Radiacion, Virus, Sanador
import time, os

def ingresar_matriz():
    """
    Permite al usuario ingresar una matriz de ADN de 6x6, asegurándose de que
    contiene únicamente las bases nitrogenadas válidas ('A', 'T', 'C', 'G').
    """
    print("Ingrese una matriz de ADN (6 filas de 6 caracteres cada una).")
    print("Solo se permiten los caracteres: A, T, C, G.")
    
    matriz = []
    for i in range(6): # Recorremos las 6 filas de la matriz
        while True:
            # Solicitamos al usuario que ingrese una fila de ADN
            fila = input(f"Ingrese la fila {i + 1} (6 caracteres): ").strip().upper()
            
            # Verificamos que la fila tenga exactamente 6 caracteres y solo contenga A, T, C o G
            if len(fila) == 6 and all(char in "ATCG" for char in fila):
                matriz.append(fila) # Si es válida, la agregamos a la matriz
                break # Salimos del bucle para pedir la siguiente fila
            else:
                # Si la fila es inválida, mostramos un mensaje de error y pedimos la fila nuevamente
                print("Entrada inválida. Asegúrese de ingresar exactamente 6 caracteres válidos (A, T, C, G).")
                
    return matriz # Retornamos la matriz de ADN ingresada por el usuario

def main():
    print("Bienvenido al programa de análisis y modificación de ADN")
    matriz = ingresar_matriz()
    
    #Matriz de prueba
    #matriz = ["AGTGGA","ATGATC","AAGAAT","GATGAT","ATCCGC","CGAACA"]
    
    while True:
        # Mostramos la matriz de ADN actual
        print("\nMatriz actual:")
        for fila in matriz:
            print(fila)
        
        # Opciones disponibles para el usuario
        print("\nOpciones:")
        print("1. Detectar mutaciones")
        print("2. Crear una mutación")
        print("3. Sanar el ADN")
        print("4. Salir")
        
        # Solicita al usuario que elija una opción
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            detector = Detector(matriz)
            es_mutante = detector.detectar_mutantes() # Verificamos si hay mutantes
            print("¿El ADN es mutante?", "Sí" if es_mutante else "No")
            input("Presione enter para continuar")# Pausa hasta que el usuario presione enter
            
            #Vaciamos la pantalla de la consola
            if os.name == 'nt':  # Si es Windows
                os.system('cls')
            else:  # Si es Linux/MacOS
                os.system('clear')
        
        elif opcion == "2":
            base = input("Ingrese la base nitrogenada para mutar (A, T, C, G): ").upper()
            while base not in ['A', 'T', 'C', 'G']:
                base = input("Base nitrogenada inválida. Ingrese A, T, C o G: ").upper()
            tipo = input("Tipo de mutación: (R) Radiación o (V) Virus: ").upper()
            if tipo == "R":
                # Si el tipo de mutación es Radiación, solicitamos la orientación y posición
                orientacion = input("Orientación (H para horizontal, V para vertical): ").upper()
                pos_fila = int(input("Fila inicial: (Va desde 1 a 6): "))-1
                pos_col = int(input("Columna inicial: (Va desde 1 a 6): "))-1
                # Creamos un objeto Radiacion y aplicamos la mutación
                radiacion = Radiacion(base,(pos_fila,pos_col),orientacion)
                matriz = radiacion.crear_mutante(matriz, base,(pos_fila, pos_col), orientacion)
            elif tipo == "V":
                # Si el tipo de mutación es Virus, solicitamos la orientación y posición
                orientacion = input("Orientación (I para de izquierda a derecha, D para de derecha a izquierda): ").upper()
                pos_fila = int(input("Fila inicial: (Va desde 1 a 6): "))-1
                pos_col = int(input("Columna inicial: (Va desde 1 a 6): "))-1
                # Creamos un objeto Virus y aplicamos la mutación
                virus = Virus(base,(pos_fila,pos_col),orientacion)
                matriz = virus.crear_mutante(matriz,base,(pos_fila,pos_col),orientacion)
            else:
                # Si el tipo de mutación es inválido
                print("Opción de mutación no válida. Por favor vuelva a intentar con 'R' para Radiación o 'V' para Virus.")
                input("Presione enter para continuar")
                #Vaciamos la pantalla de la consola
                if os.name == 'nt':  # Si es Windows
                    os.system('cls')
                else:  # Si es Linux/MacOS
                    os.system('clear')
        
        elif opcion == "3":
            # Opción para sanar mutaciones en el ADN
            sanador = Sanador()
            matriz = sanador.sanar_mutantes(matriz) # Llamamos al método para sanar el ADN
            input("Presione enter para continuar")
            #Vaciamos la pantalla de la consola
            if os.name == 'nt':  # Si es Windows
                os.system('cls')
            else:  # Si es Linux/MacOS
                os.system('clear')
        
        elif opcion == "4":
            print("¡Hasta luego!")
            time.sleep(2.5) # Pausa de 2.5 segundos antes de finalizar
            break  # Salir del bucle principal y terminar el programa
        
        else:
            # Si la opción elegida no es válida
            print("Opción no válida.")

if __name__ == "__main__":
    main()