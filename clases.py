import random

class Detector:
    # Constructor
    def __init__(self, matriz_adn):
        self.matriz_adn = matriz_adn
        self.bases_nitrogenadas = ['A', 'T', 'C', 'G']

    # Verificar si hay mutación en cualquier dirección
    def detectar_mutantes(self):
        return (
            self.detectar_horizontal() or
            self.detectar_vertical() or 
            self.diagonal_primaria() or
            self.diagonal_secundaria() or
            self.diagonal_primaria_inversa() or
            self.diagonal_secundaria_inversa()
        )

    def detectar_horizontal(self):
        for fila in self.matriz_adn:
            if self.analizar_secuencia(fila):
                return True
        return False
    
    def detectar_vertical(self):
        for col in range(6):
            columna = ''.join([self.matriz_adn[fila][col] for fila in range(6)])
            if self.analizar_secuencia(columna):
                return True
        return False

    #Verificar si hay alguna mutacion de manera diagonal de izquierda a derecha
    def diagonal_primaria(self):
        #Diagonales que empiezan en (0,0)(1,0)(2,0)
        for i in range(3):
            diagonal_principal =''.join([self.matriz_adn[i+j][j] for j in range(6-i)])
            if self.analizar_secuencia(diagonal_principal):
                return True
        return False
    
    #Verificar si hay alguna mutacion de manera diagonal de izquierda a derecha
    def diagonal_secundaria(self):
        #Diagonales que empiezan en (0,1) y (0,2)
        for i in range(3):
            diagonal_secundaria = ''.join([self.matriz_adn[j][i+j] for j in range(6-i)])
            if self.analizar_secuencia(diagonal_secundaria):
                return True
        return False
    
    #Verificar si hay alguna mutacion de manera diagonal de derecha a izquierda
    def diagonal_primaria_inversa(self):
        #Diagonales que empiezan en (0,5)(1,5)(2,5)
        for i in range(3):
            diagonal_inversa_principal = ''.join([self.matriz_adn[i+j][5-j] for j in range(6-i)])
            if self.analizar_secuencia(diagonal_inversa_principal):
                return True
        return False
    
    #Verificar si hay alguna mutacion de manera diagonal de derecha a izquierda
    def diagonal_secundaria_inversa(self):
        #Diagonales que empiezan en (0,4) y (0,3)
        for i in range(3):
            diagonal_inversa_secundaria = ''.join([self.matriz_adn[j][5-i-j] for j in range(6-i)])
            if self.analizar_secuencia(diagonal_inversa_secundaria):
                return True
        return False
        
    def analizar_secuencia(self, secuencia):
        #Verificar si la secuencia de caracteres tiene 4 bases nitrogenadas seguidas de una misma
        for base in self.bases_nitrogenadas:
            if  base * 4 in ''.join(secuencia):
                    return True
        return False

class Mutador:
    def __init__(self, base_nitrogenada,posicion_inicial):
        self.base_nitrogenada = base_nitrogenada
        self.posicion_inicial = posicion_inicial
    
    def crear_mutante(self):
        pass
    
class Radiacion(Mutador):
    def __init__(self, base_nitrogenada,posicion_inicial,orientacion):
        super().__init__(base_nitrogenada,posicion_inicial)
        #La orientacion puede ser horizontal o vertical ('H'/'V')
        self.orientacion = orientacion
    

    def crear_mutante(self,matriz,base_nitrogenada,posicion_inicial,orientacion):
        try:
            if base_nitrogenada not in ['A', 'T', 'C', 'G']:
                raise Exception("La base nitrogenada no es parte de ('A', 'T', 'C', 'G').")
            #Debido a que las cadenas de caracteres son inmutables en python
            #Convertirmos las mismas en listas de caracteres para poder modificarlas
            matriz = [list(fila) for fila in matriz]  
            if(orientacion == 'H'):
                if(posicion_inicial[1]<=2):
                    for i in range(4):
                        matriz[posicion_inicial[0]][posicion_inicial[1]+i] = base_nitrogenada   
                else:
                    print("No se puede empezar una mutacion en esta posicion")
            elif(orientacion == 'V'):
                if(posicion_inicial[0]<=2):
                    for i in range(4):
                        matriz[posicion_inicial[0]+i][posicion_inicial[1]]= base_nitrogenada   
                else:
                    print("No se puede empezar una mutacion en esta posicion")
            else:
                raise ValueError("Orientación de la mutación no válida. Use 'H' para horizontal o 'V' para vertical.")
        except Exception as e:
            print(f"Error al crear mutante: {e}")
        finally:
            matriz = ["".join(fila) for fila in matriz]
            return matriz

class Virus(Mutador):
    def __init__(self, base_nitrogenada,posicion_inicial,orientacion):
        super().__init__(base_nitrogenada,posicion_inicial)
        #La orientacion puede ser diagonal de izquieda a derecha o de derecha a izquierda ('D'/'I')
        self.orientacion = orientacion
        
    def crear_mutante(self,matriz,base_nitrogenada,posicion_inicial,orientacion):
        
        try:  
            if base_nitrogenada not in ['A', 'T', 'C', 'G']:
                raise Exception("La base nitrogenada no es parte de ('A', 'T', 'C', 'G').")
            #Debido a que las cadenas de caracteres son inmutables en python
            #Convertirmos las mismas en listas de caracteres para poder modificarlas
            matriz = [list(fila) for fila in matriz]
            if(orientacion == 'D'):
                if(posicion_inicial[0]<=2 and posicion_inicial[1]>2):
                    for i in range(4):
                        matriz[posicion_inicial[0]+i][posicion_inicial[1]-i]= base_nitrogenada   
                else:
                    print("No se puede empezar una mutacion en esta posicion")
            elif(orientacion == 'I'):
                if((posicion_inicial[0]<=2) and (posicion_inicial[1]<=2)):
                    for i in range(4):
                        matriz[posicion_inicial[0]+i][posicion_inicial[1]+i]= base_nitrogenada   
                else:
                    print("No se puede empezar una mutacion en esta posicion")
            else:
                raise ValueError("Orientación de la mutación no válida. Use 'H' para horizontal o 'V' para vertical.")
        except Exception as e:
            print(f"Error al crear mutante: {e}")
        finally:
            matriz = ["".join(fila) for fila in matriz]
            return matriz


class Sanador:
    def __init__(self):
        self.bases_nitrogenadas = ['A', 'T', 'C', 'G']
                
    def sanar_mutantes(self, matriz):
        detector = Detector(matriz)
        if detector.detectar_mutantes():
            print("Se detectaron mutaciones. Generando nuevo ADN...")
            return self.generar_matriz_sin_mutaciones()
        else:
            print("No se detectaron mutaciones. El ADN es válido.")
            return matriz

    def generar_matriz_sin_mutaciones(self):
        while True:
            nuevo_adn = self.generar_matriz_aleatoria()
            detector = Detector(nuevo_adn)
            if not detector.detectar_mutantes():
                return nuevo_adn

    def generar_matriz_aleatoria(self):
        nuevo_adn = []
        for _ in range(6):
            fila = ''.join(random.choices(self.bases_nitrogenadas, k=6))
            nuevo_adn.append(fila)
        return nuevo_adn




