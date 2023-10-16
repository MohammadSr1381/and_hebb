import matplotlib.pyplot as plt
import numpy as np

class Perceptron:
    def __init__(self):
        self.dataset = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        self.weights = [0, 0, 0]

    def learn(self, outputs):
        for i in range(len(self.dataset)):
            if i < len(self.weights):
                delta_bias = outputs[i]
                delta_weight1 = self.dataset[i][0] * outputs[i]
                delta_weight2 = self.dataset[i][1] * outputs[i]
                self.weights[0] += delta_bias
                self.weights[1] += delta_weight1
                self.weights[2] += delta_weight2

    def test(self, test_input):
        predictions = []
        for i in test_input:
            if self.predict(i) >= 0:
                predictions.append(1)
            else:
                predictions.append(-1)
        return predictions

    def predict(self, input):
        return self.weights[0] + input[0] * self.weights[1] + input[1] * self.weights[2]

    def draw(self, input):
        x1_scatter = np.linspace(-10, 10, 100)
        x2_scatter = np.linspace(-10, 10, 100)
        var1_grid, var2_grid = np.meshgrid(x1_scatter, x2_scatter)
        x_grid = np.vstack((np.ones_like(var1_grid), var1_grid, var2_grid))
        y = np.dot(self.weights, x_grid)

        plt.contour(x1_scatter, x2_scatter, y, levels=[0], colors='g')
        plt.xlabel('x1')
        plt.ylabel('x2')
        plt.xlim(-4, 4)
        plt.ylim(-4, 4)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)

        for i in input:
            if self.predict(i) > 0:
                plt.scatter(i[0], i[1], color='green', label='x1, x2')
            else:
                plt.scatter(i[0], i[1], color='red', label='x1, x2')

        plt.legend()
        plt.show()

if __name__ == "__main__":
    perceptron = Perceptron()
    outputs = [1, -1, -1, -1]
    test_input = [[1, 1], [-1, 1], [2, 1], [1, -6], [3, 2], [-1, -4], [-2, 3], [-1, -1], [5, -4], [-1, -3]]

    perceptron.learn(outputs)
    predictions = perceptron.test(test_input)
    print("Predictions:", predictions)
    perceptron.draw(test_input)