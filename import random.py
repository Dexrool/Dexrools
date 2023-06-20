from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, Aer

# Создаем квантовый регистр
qr = QuantumRegister(1)

# Создаем классический регистр
cr = ClassicalRegister(1)

# Создаем квантовую схему
circuit = QuantumCircuit(qr, cr)

# Устанавливаем начальное значение переменной F в 2
circuit.x(qr[0])
circuit.x(qr[0])

# Прибавляем 1 к переменной F
circuit.cx(qr[0], qr[0])

# Измеряем значение переменной F и записываем его в классический регистр
circuit.measure(qr, cr)

# Запускаем схему на локальном симуляторе
backend = Aer.get_backend('qasm_simulator')
job = execute(circuit, backend, shots=1)
result = job.result()
counts = result.get_counts()

# Выводим значение переменной F в консоль
print(int(list(counts.keys())[0]))




