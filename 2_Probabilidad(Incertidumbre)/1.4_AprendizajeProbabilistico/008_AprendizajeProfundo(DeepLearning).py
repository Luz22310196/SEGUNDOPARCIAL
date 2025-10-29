import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Datos de ejemplo: XOR
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

# Crear modelo
model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))  # capa oculta
model.add(Dense(1, activation='sigmoid'))  # capa de salida

# Compilar modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar modelo
model.fit(X, y, epochs=500, verbose=0)

# Predicciones
pred = model.predict(X)
print("Predicciones:", np.round(pred).astype(int))