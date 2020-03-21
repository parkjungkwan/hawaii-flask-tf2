import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import random

class Population:

    population_inc: []
    population_old: []

    @property
    def population_inc(self) -> int: return self._population_inc

    @population_inc.setter
    def population_inc(self, population_inc): self._population_inc = population_inc

    @property
    def population_old(self) -> int: return self._population_old

    @population_old.setter
    def population_old(self, population_old): self._population_old = population_old

    def initialize(self):
        """
        4.1 선형 회귀(Linear Regression)
        """
        # 4.1 지역별 인구증가율과 고령인구비율 시각화

        self.population_inc = [0.3, -0.78, 1.26, 0.03, 1.11, 15.17, 0.24, -0.24, -0.47, -0.77, -0.37, -0.85, -0.41, -0.27,
        0.02, -0.76, 2.66]
        self.population_old = [12.27, 14.44, 11.87, 18.75, 17.52, 9.29, 16.37, 19.78, 19.51, 12.65, 14.74, 10.72, 21.94,
        12.83, 15.51, 17.14, 14.42]

    def population_without_outlier(self):
        self.population_inc = self.population_inc[:5] + self.population_inc[6:]
        self.population_old = self.population_old[:5] + self.population_old[6:]

    def population_with_regression(self):
        # 4.3 최소제곱법으로 회귀선 구하기
        X = self.population_inc
        Y = self.population_old
        # X, Y의 평균
        x_bar = sum(X) / len(X)
        y_bar = sum(Y) / len(Y)

        # 최소제곱법으로 a, b를 구합니다.
        a = sum([(y - y_bar) * (x - x_bar) for y, x in list(zip(Y, X))])
        a /= sum([(x - x_bar) ** 2 for x in X])
        b = y_bar - a * x_bar
        print('a:', a, 'b:', b)

        # 그래프를 그리기 위해 회귀선의 x, y 데이터를 구합니다.
        line_x = np.arange(min(X), max(X), 0.01)
        line_y = a * line_x + b
        return {'line_x':line_x, 'line_y': line_y}


    def population_with_regression_using_tf(self):
        # tf 머신러닝 를 사용해서 회귀선 구하기
        X = self.population_inc
        Y = self.population_old
        a = tf.Variable(random.random())
        b = tf.Variable(random.random())
        # 잔차의 제곱의 평균을 반환하는 함수
        def compute_loss():
            y_pred = a * X + b
            loss = tf.reduce_mean((Y - y_pred) ** 2)
            return loss

        optimizer = tf.keras.optimizers.Adam(lr=0.07)
        for i in range(1000):
            optimizer.minimize(compute_loss, var_list=[a, b])

            if i % 100 == 99:
                print(i, 'a: ', a.numpy(), 'b: ', b.numpy(), 'loss : ', compute_loss().numpy())
        line_x = np.arange(min(X), max(X), 0.01)
        line_y = a * line_x + b
        return {'line_x': line_x, 'line_y': line_y}

    def new_model(self):
        X = instance.population_inc
        Y = instance.population_old
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(units=6, activation='tanh', input_shape=(1,)),
            tf.keras.layers.Dense(units=1)
        ])
        model.compile(optimizer=tf.keras.optimizers.SGD(lr=0.1), loss='mse')
        # mse : mean squared error
        model.fit(X, Y, epochs=10)
        model.predict(X)
        return model

    def predict(self, model):
        # deap learning 회귀선 == mlp
        X = self.population_inc
        line_x = np.arange(min(X), max(X), 0.01)
        line_y = model.predict(line_x)
        return {'line_x': line_x, 'line_y': line_y}



class View:
    @staticmethod
    def show_population(instance, dic):
        X = instance.population_inc
        Y = instance.population_old
        line_x = dic['line_x']
        line_y = dic['line_y']
        # 붉은색 실선으로 회귀선을 그립니다.
        plt.plot(line_x, line_y, 'r-')
        plt.plot(X, Y, 'bo')
        plt.xlabel('Population Growth Rate (%)')
        plt.ylabel('Elderly Population Rate (%)')
        plt.show()


if __name__ == '__main__':
    instance = Population()
    view = View()
    instance.initialize()
    instance.population_without_outlier()
    # dic = instance.population_with_regression()
    # dic = instance.population_with_regression_using_tf()
    dic = instance.predict(instance.new_model())
    view.show_population(instance, dic)