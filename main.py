import json
import matplotlib.pyplot as plt

class Graph:
    x_data = []
    y_data = []

    def __init__(self, x_data, y_data):
        self.x_data = x_data
        self.y_data = y_data

    def add_labels(self, x_label, y_label, title):
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

    def show_graph(self):
        plt.plot(self.x_data, self.y_data)
        plt.show()

#getting data from the user
num_x = int(input("How many x points do you have: "))
num_y = int(input("How many y points do you have: "))

x_points = [0] * num_x
y_points = [0] * num_y

for i in range(num_x):
    x_points[i] += int(input(f"Input x value {i + 1}: "))

for i in range(num_y):
    y_points[i] += int(input(f"Input y vlaue {i + 1}: "))

#getting user input for labels and title
graph_title = input("Input graph title: ")
x_label = input("Label x-axis: ")
y_label = input("Label y-axis: ")

#creating an instance of the graph
graph = Graph(x_points, y_points)
graph.add_labels(x_label=x_label, y_label=y_label, title=graph_title)
graph.show_graph()