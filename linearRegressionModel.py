import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


def create_data():
    num_points = 1000
    x_data = []
    y_data = []
    for i in range(num_points):
        x1 = np.random.normal(0.0, 0.55)  # 横坐标，进行随机高斯处理化，以0为均值，以0.55为标准差
        y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.03)  # 纵坐标，数据点在y1=x1*0.1+0.3上小范围浮动
        x_data.append(x1)
        y_data.append(y1)
    return x_data, y_data


def show(x_data, y_data):
    plt.scatter(x_data, y_data, c='r')
    plt.show()

def linearRegressionModel1():
    print()

def training(x_data, y_data):
    W = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name='W')  # 生成1维的W矩阵，取值是[-1,1]之间的随机数
    b = tf.Variable(tf.zeros([1]), name='b')  # 生成1维的b矩阵，初始值是0
    y = W * x_data + b  # 经过计算得出预估值y
    loss = tf.reduce_mean(tf.square(y - y_data), name='loss')  # 以预估值y和实际值y_data之间的均方误差作为损失
    optimizer = tf.train.GradientDescentOptimizer(0.5)  # 采用梯度下降法来优化参数  学习率为0.5
    train = optimizer.minimize(loss, name='train')  # 训练的过程就是最小化这个误差值
    sess = tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)
    print("W =", sess.run(W), "b =", sess.run(b), "loss =", sess.run(loss))  # 初始化的W和b是多少
    for step in range(20):  # 执行20次训练
        sess.run(train)
        print("W =", sess.run(W), "b =", sess.run(b), "loss =", sess.run(loss))  # 输出训练好的W和b


if __name__ == "__main__":
    x_data, y_data = create_data()
    show(x_data, y_data)
    training(x_data,y_data)
