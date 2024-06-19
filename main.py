import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data1.csv')

# print(data)

def loss_function(m,b,points):
    total_error = 0

    for i in range(len(points)):
        x = points.iloc[i].x
        y = points.iloc[i].y
        total_error += (y - (m*x + b)) ** 2
    total_error = total_error/float(len(points))

def gradient_descent(m_now, b_now, points, lr):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(len(points)):
        x = points.iloc[i].x
        y = points.iloc[i].y
   
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * lr
    b = b_now - b_gradient * lr

    return m,b



m = 0
b = 0
lr = 0.0001
epochs = 1000

for i in range(epochs):
    m,b = gradient_descent(m,b,data,lr)

print(m,b)

plt.scatter(data.x, data.y, color="black")
plt.plot((list(range(0,50))), [m * x + b for x in range(0,50)], color = "red")
plt.show()
