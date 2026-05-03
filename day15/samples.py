# Chapter 15 — Generating Data
# Install first: pip install matplotlib

# --- Basic matplotlib plot ---
# import matplotlib.pyplot as plt
#
# squares = [1, 4, 9, 16, 25]
# fig, ax = plt.subplots()
# ax.plot(squares, linewidth=3)
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# ax.tick_params(labelsize=14)
# plt.show()

# --- Scatter plot ---
# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]
#
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# ax.axis([0, 1100, 0, 1100000])
# plt.savefig('squares_plot.png', bbox_inches='tight')   # save instead of show

# --- Random Walk class ---
# from random import choice
#
# class RandomWalk:
#     def __init__(self, num_points=5000):
#         self.num_points = num_points
#         self.x_values = [0]
#         self.y_values = [0]
#
#     def fill_walk(self):
#         while len(self.x_values) < self.num_points:
#             x_direction = choice([1, -1])
#             x_distance = choice([0, 1, 2, 3, 4])
#             x_step = x_direction * x_distance
#             y_direction = choice([1, -1])
#             y_distance = choice([0, 1, 2, 3, 4])
#             y_step = y_direction * y_distance
#             if x_step == 0 and y_step == 0:
#                 continue
#             self.x_values.append(self.x_values[-1] + x_step)
#             self.y_values.append(self.y_values[-1] + y_step)

# --- Plotting a random walk with color gradient ---
# rw = RandomWalk()
# rw.fill_walk()
# point_numbers = range(rw.num_points)
# ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)
# ax.scatter(0, 0, c='green', s=100)           # start
# ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)  # end

# --- Simulating dice rolls with plotly ---
# from plotly.graph_objs import Bar, Layout
# from plotly import offline
#
# class Die:
#     def __init__(self, num_sides=6):
#         self.num_sides = num_sides
#
#     def roll(self):
#         return randint(1, self.num_sides)
#
# die = Die()
# results = [die.roll() for _ in range(1000)]
# frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]
#
# x_values = list(range(1, die.num_sides + 1))
# data = [Bar(x=x_values, y=frequencies)]
# my_layout = Layout(title="Results of rolling one D6 1000 times")
# offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

# --- Key ideas ---
# 1. ax.plot() = line chart, ax.scatter() = dot chart
# 2. c= sets dot colors; cmap= maps values to a color range
# 3. plt.show() → interactive window; plt.savefig() → saves to file
# 4. Random walk: each step builds on the LAST position (cumulative, not random)
# 5. plotly produces interactive HTML charts; matplotlib produces static images

print("Chapter 15: See the comments above for matplotlib and plotly patterns.")
print("Install: pip install matplotlib plotly")
