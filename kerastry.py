import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

def P(x):
    return 2.5 * x ** 5 - 2.9 * x ** 4 + 1.4 * x ** 3 - 1.3 * x ** 2 + 2.1 * x - 3
def g(x):
    return 5 / np.cos(x ** 3 / 2)

x_P = np.linspace(1, 1.4, 1000).reshape(-1, 1)
y_P = P(x_P)
x_g = np.linspace(-1.2, 1.2, 1000).reshape(-1, 1)
y_g = g(x_g)

def create_model(hidden_units, layers):
    model = Sequential()
    model.add(Dense(hidden_units, input_dim=1, activation='tanh'))
    for _ in range(layers - 1):
        model.add(Dense(hidden_units, activation='tanh'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

model_P = create_model(128, 3)
history_P = model_P.fit(x_P, y_P, epochs=500, batch_size=32, verbose=0)
y_pred_P = model_P.predict(x_P)

model_g = create_model(128, 3)
history_g = model_g.fit(x_g, y_g, epochs=500, batch_size=32, verbose=0)
y_pred_g = model_g.predict(x_g)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x_P, y_P, label='P(x)', color='blue')
plt.plot(x_P, y_pred_P, label='Нейросеть', color='red', linestyle='--')
plt.title('P(x) и его аппроксимация')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_g, y_g, label='g(x)', color='blue')
plt.plot(x_g, y_pred_g, label='Нейросеть', color='red', linestyle='--')
plt.title('g(x) и его аппроксимация')
plt.legend()
plt.show()

print("Пример предсказания P(2.0):", model_P.predict(np.array([[2.0]])))
print("Реальное значение P(2.0):", P(2.0))
print("Пример предсказания g(0.5):", model_g.predict(np.array([[0.5]])))
print("Реальное значение g(0.5):", g(0.5))

print("\nВеса модели P(x)")
print("Значения внутренних переменных слоя L0_P:")
print(model_P.layers[0].get_weights())
print("Значения внутренних переменных слоя L1_P:")
print(model_P.layers[1].get_weights())
print("Значения внутренних переменных слоя L2_P:")
print(model_P.layers[2].get_weights())

print("\nВеса модели g(x)")
print("Значения внутренних переменных слоя L0_g:")
print(model_g.layers[0].get_weights())
print("Значения внутренних переменных слоя L1_g:")
print(model_g.layers[1].get_weights())
print("Значения внутренних переменных слоя L2_g:")
print(model_g.layers[2].get_weights())
