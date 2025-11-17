import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=2)

def normalize(v):
    v = np.array(v, dtype=float)
    return v / (np.linalg.norm(v) + 1e-9)

@qml.qnode(dev)
def sim(a, b):
    a = normalize(a)
    b = normalize(b)

    qml.RY(np.pi*a[0], wires=0)
    qml.RY(np.pi*a[1], wires=1)
    qml.CNOT(wires=[0,1])
    qml.RY(np.pi*b[0], wires=0)
    qml.RY(np.pi*b[1], wires=1)
    return qml.expval(qml.PauliZ(0))

def quantum_similarity(a, b):
    return float(0.5*(sim(a,b) + 1))
