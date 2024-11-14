
## Generador de numeros aleatorios cuanticos
import numpy as np
from matplotlib import pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def generador_aleatorio_cuantico(n):
    circuito = QuantumCircuit(n, n)

## ENSAMBLO EL CIRCUITO
    for qubit in range(n):
# Se aplica la compuerta hadamard a los qubits asociados
        circuito.h(qubit) 
# Se mide el circuito        
    circuito.measure(range(n), range(n))
#Se simula el circuito
    simulador = AerSimulator()
    job = simulador.run(circuito, shots=1000)  #Si aumento los shots emparejo más la distribución
    resultado = job.result()

    conteos = resultado.get_counts(circuito)

    numero_aleatorio_binario = list(conteos.keys())[0]
    numero_aleatorio_decimal = int(numero_aleatorio_binario, 2)  # Convertir de binario a  decimal

    return numero_aleatorio_decimal

lista_n = [generador_aleatorio_cuantico(3) for i in range(500)]  # Ejemplo con 500 muestras
#print(lista_n)

# histograma 
plt.hist(lista_n, bins=15, edgecolor='black')  # 20 bins o categorías de la distribución
plt.title("Histograma de Números Aleatorios Cuánticos Generados")
plt.xlabel("Valor del Número Aleatorio")
plt.ylabel("Frecuencia")
plt.show()