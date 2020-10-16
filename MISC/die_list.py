from dieclass import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create 1 D6 instance
# die = Die()
# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.

results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

# analyze
frequencies = []
maxresult = die_1.roll() + die_2.roll()
for value in range(2, maxresult + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)


# Visualize the results.
x_values = list(range(2, maxresult+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 10000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
