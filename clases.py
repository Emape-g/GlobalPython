import random

class Detector:
    # Constructor
    def __init__(self, matriz_adn):
        self.matriz_adn = matriz_adn
        self.bases_nitrogenadas = ['A', 'T', 'C', 'G']

    """
    Todos los metodos detectar van creando cadenas de 4 a 6 caracteres, luego la envian al metodo analizar_secuencia()
    que analiza las cadenas individualmente. En el caso de encontrar una mutación retorna un True y se deja de analizar
    la matriz.
    """

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

    #Verificar si hay alguna mutacion horizontal
    def detectar_horizontal(self):
        for fila in self.matriz_adn: #separamos cada fila de la matriz para analizarla individualmente
            if self.analizar_secuencia(fila): #
                return True
        return False
    
    #Verificar si hay alguna mutacion vertical
    def detectar_vertical(self):
        for col in range(6):
            #creamos un string con cada una de las columnas
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
        # Iterar sobre cada una de las bases nitrogenadas posibles
        for base in self.bases_nitrogenadas:
            #Verificar si la secuencia de caracteres tiene 4 bases nitrogenadas seguidas de una misma
            if  base * 4 in secuencia:
                    return True
        return False

class Mutador:
    #Constructor
    def __init__(self, base_nitrogenada,posicion_inicial):
        self.base_nitrogenada = base_nitrogenada
        self.posicion_inicial = posicion_inicial
    
    def crear_mutante(self):
        pass
    
class Radiacion(Mutador):
    #Constructor
    def __init__(self, base_nitrogenada,posicion_inicial,orientacion):
        super().__init__(base_nitrogenada,posicion_inicial)
        #La orientacion puede ser horizontal o vertical ('H'/'V')
        self.orientacion = orientacion
    

    def crear_mutante(self,matriz,base_nitrogenada,posicion_inicial,orientacion):
        try:
                        
            #Debido a que las cadenas de caracteres son inmutables en python
            #Convertirmos las mismas en listas de caracteres para poder modificarlas
            matriz = [list(fila) for fila in matriz] 
            
            # Verificar la orientación de la mutación 
            if(orientacion == 'H'): #Posicion Horizontal
                if(posicion_inicial[1]<=2):
                    # Reemplazar 4 posiciones consecutivas en la columna
                    for i in range(4):
                        matriz[posicion_inicial[0]][posicion_inicial[1]+i] = base_nitrogenada   
                else:
                    print("No se puede empezar una mutacion en esta posicion")
                    
            elif(orientacion == 'V'):#Posicion Vertical
                if(posicion_inicial[0]<=2):
                    # Reemplazar 4 posiciones consecutivas en la columna
                    for i in range(4):
                        matriz[posicion_inicial[0]+i][posicion_inicial[1]]= base_nitrogenada   
                        
                else:
                    # Si la posicion indicada no puede almacenar una cadena de 4 bases_nitrogenadas
                    print("No se puede empezar una mutacion en esta posicion")
            else:
                # Si la orientación no es válida, lanzar un error
                raise ValueError("Orientación de la mutación no válida. Use 'H' para horizontal o 'V' para vertical.")
        except Exception as e:
            # Capturar cualquier excepción y mostrar un mensaje de error
            print(f"Error al crear mutante: {e}")
        finally:
            # Convertir las filas de la matriz nuevamente a cadenas de caracteres
            matriz = ["".join(fila) for fila in matriz]
            return matriz   #Retorna la matriz ya sea modificada o no
                            #No va a estar modificada en caso de que se lance alguna excepción

class Virus(Mutador):
    #Constructor
    def __init__(self, base_nitrogenada,posicion_inicial,orientacion):
        super().__init__(base_nitrogenada,posicion_inicial)
        #La orientacion puede ser diagonal de izquieda a derecha o de derecha a izquierda ('D'/'I')
        self.orientacion = orientacion
        
    def crear_mutante(self,matriz,base_nitrogenada,posicion_inicial,orientacion):
        try:  
            
            #Debido a que las cadenas de caracteres son inmutables en python
            #Convertirmos las mismas en listas de caracteres para poder modificarlas
            matriz = [list(fila) for fila in matriz]
            
            # Verificar la orientación de la mutación 
            if(orientacion == 'D'):#De derecha a izquierda
                if(posicion_inicial[0]<=2 and posicion_inicial[1]>2):
                    # Reemplazar 4 posiciones consecutivas en la columna
                    for i in range(4):
                        matriz[posicion_inicial[0]+i][posicion_inicial[1]-i]= base_nitrogenada
                          
                else:
                    # Si la posicion indicada no puede almacenar una cadena de 4 bases_nitrogenadas
                    print("No se puede empezar una mutacion en esta posicion")
                    
            elif(orientacion == 'I'):#De izquireda a derecha
                if((posicion_inicial[0]<=2) and (posicion_inicial[1]<=2)):
                    # Reemplazar 4 posiciones consecutivas en la columna
                    for i in range(4):
                        matriz[posicion_inicial[0]+i][posicion_inicial[1]+i]= base_nitrogenada   
                
                else:
                    # Si la posicion indicada no puede almacenar una cadena de 4 bases_nitrogenadas
                    print("No se puede empezar una mutacion en esta posicion")
            else:
                # Si la orientación no es válida, lanzar un error
                raise ValueError("Orientación de la mutación no válida. Use 'H' para horizontal o 'V' para vertical.")
        
        except Exception as e:
            # Capturar cualquier excepción y mostrar un mensaje de error
            print(f"Error al crear mutante: {e}")
            
        finally:
            # Convertir las filas de la matriz nuevamente a cadenas de caracteres
            matriz = ["".join(fila) for fila in matriz]
            return matriz   #Retorna la matriz ya sea modificada o no
                            #No va a estar modificada en caso de que se lance alguna excepción

class Sanador:
    #Constructor
    def __init__(self):
        self.bases_nitrogenadas = ['A', 'T', 'C', 'G']
                
    def sanar_mutantes(self, matriz):
        # Crear una instancia del detector para verificar mutaciones en la matriz proporcionada
        detector = Detector(matriz)
        
        #Verificar si la matriz tiene mutaciones
        if detector.detectar_mutantes():
            # Si se detectan mutaciones, generar una nueva
            print("Se detectaron mutaciones. Generando nuevo ADN...")
            return self.generar_matriz_sin_mutaciones()
        else:
            print("No se detectaron mutaciones. El ADN es válido.")
            # Si no hay mutaciones, devolver la matriz original
            return matriz

    def generar_matriz_sin_mutaciones(self):
        while True:
            # Generar una nueva matriz de ADN aleatoria
            nuevo_adn = self.generar_matriz_aleatoria()
            
            # Verificar si la nueva matriz contiene mutaciones
            detector = Detector(nuevo_adn)
            
            # Si no hay mutaciones en el nuevo ADN, retornar la nueva matriz
            if not detector.detectar_mutantes():
                return nuevo_adn

    def generar_matriz_aleatoria(self):
        nuevo_adn = []
        for _ in range(6):
            # Generar una fila aleatoria de 6 bases nitrogenadas
            fila = ''.join(random.choices(self.bases_nitrogenadas, k=6)) #Uso de random para crear elecciones aleatorias
            nuevo_adn.append(fila)
        return nuevo_adn




