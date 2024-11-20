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
    for i in range(6):
        while True:
            fila = input(f"Ingrese la fila {i + 1} (6 caracteres): ").strip().upper()
            if len(fila) == 6 and all(char in "ATCG" for char in fila):
                matriz.append(fila)
                break
            else:
                print("Entrada inválida. Asegúrese de ingresar exactamente 6 caracteres válidos (A, T, C, G).")

def main():
    print("Bienvenido al programa de análisis y modificación de ADN")
    #matriz = ingresar_matriz()
    matriz = ["AGTGGA","ATGATC","AAGAAT","GATGAT","ATCCGC","CGAACA"]
    
    while True:
        print("\nMatriz actual:")
        for fila in matriz:
            print(fila)
        
        print("\nOpciones:")
        print("1. Detectar mutaciones")
        print("2. Crear una mutación")
        print("3. Sanar el ADN")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            detector = Detector(matriz)
            es_mutante = detector.detectar_mutantes()
            print("¿El ADN es mutante?", "Sí" if es_mutante else "No")
            input("Presione enter para continuar")
            os.system('cls')
        
        elif opcion == "2":
            base = input("Ingrese la base nitrogenada para mutar (A, T, C, G): ").upper()
            tipo = input("Tipo de mutación: (R) Radiación o (V) Virus: ").upper()
            if tipo == "R":
                orientacion = input("Orientación (H para horizontal, V para vertical): ").upper()
                pos_fila = int(input("Fila inicial: (Va desde 1 a 6): "))-1
                pos_col = int(input("Columna inicial: (Va desde 1 a 6): "))-1
                radiacion = Radiacion(base,(pos_fila,pos_col),orientacion)
                matriz = radiacion.crear_mutante(matriz, base,(pos_fila, pos_col), orientacion)
            elif tipo == "V":
                orientacion = input("Orientación (I para de derecha a izquierda, D para de derecha a izquierda): ").upper()
                pos_fila = int(input("Fila inicial: (Va desde 1 a 6): "))-1
                pos_col = int(input("Columna inicial: (Va desde 1 a 6): "))-1
                virus = Virus(base,(pos_fila,pos_col),orientacion)
                matriz = virus.crear_mutante(matriz,base,(pos_fila,pos_col),orientacion)
            else:
                print("Opción inválida.")
                input("Presione enter para continuar")
                os.system('cls')
        
        elif opcion == "3":
            sanador = Sanador()
            matriz = sanador.sanar_mutantes(matriz)
            input("Presione enter para continuar")
            os.system('cls')
        
        elif opcion == "4":
            print("¡Hasta luego!")
            time.sleep(2.5)
            break
        
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()