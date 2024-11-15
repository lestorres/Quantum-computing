## Generador de numeros aleatorios cuanticos
import numpy as np
from matplotlib import pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def generador_aleatorio_cuantico(n):
    circuito = QuantumCircuit(n, n)

    # ENSAMBLO EL CIRCUITO
    for qubit in range(n):
        # Se aplica la compuerta Hadamard a los qubits asociados
        circuito.h(qubit) 
        
    # Se mide el circuito        
    circuito.measure(range(n), range(n))

    # Simulación del circuito
    simulador = AerSimulator()
    job = simulador.run(circuito, shots=1000)  # Si aumentas los shots, la distribución será más uniforme
    resultado = job.result()
    conteos = resultado.get_counts(circuito)

    # Obtener un número aleatorio
    numero_aleatorio_binario = list(conteos.keys())[0]
    numero_aleatorio_decimal = int(numero_aleatorio_binario, 2)  # Convertir de binario a decimal

    return numero_aleatorio_decimal, circuito

# Genera una lista de números aleatorios cuánticos
lista_n, circuito = zip(*[generador_aleatorio_cuantico(3) for i in range(500)])

# circuito cuántico
circuito[0].draw('mpl')  # Dibuja el primer circuito
plt.show()

# Histograma 
plt.hist(lista_n, bins=15, edgecolor='black')  # Histograma con 15 categorías
plt.title("Histograma de Números Aleatorios Cuánticos Generados")
plt.xlabel("Valor del Número Aleatorio")
plt.ylabel("Frecuencia")
plt.show()
