from qiskit import QuantumCircuit, Aer, transpile
from QKDFunctions import *

if __name__ == "__main__":
    # qc = QuantumCircuit(3)
    # qc.x(0)
    # qc.draw()

    key_list = gen_key(100)
    print(''.join(map(str, key_list)))
