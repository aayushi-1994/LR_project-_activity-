#plotting the TOEFL as X-Coordinate and Chances of admit as Y-Coordinate on the scatter plot

import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("main.csv")

TOEFL_Score = df["TOEFL Score"].tolist()
Chances_of_admit = df["Chance of Admit "].tolist()

fig = px.scatter(x=TOEFL_Score, y=Chances_of_admit)
fig.show()

#Adding a line using the line equation on the plot.

m = 0.018
c = -1.27
y = []
for x in TOEFL_Score:
  y_value = m*x + c
  y.append(y_value)

#Plotting the points
fig = px.scatter(x=TOEFL_Score, y=Chances_of_admit)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(TOEFL_Score), x1= max(TOEFL_Score)
    )
])
fig.show()

#to predict the chances of admit based on the TOEFL score
x = 250
y = m * x + c
print(f"Chances of admit if the TOEFL score {x} is {y}")

TOEFL_array = np.array(TOEFL_Score)
Chances_array = np.array(Chances_of_admit)

#Slope and intercept using pre-built function of Numpy
m, c = np.polyfit(TOEFL_array, Chances_array, 1)
y = []
for x in TOEFL_array:
  y_value = m*x + c
  y.append(y_value)

#Plotting the points
fig = px.scatter(x=TOEFL_array, y=Chances_array)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(TOEFL_array), x1= max(TOEFL_array)
    )
])
fig.show()

#Now using the values found let's predict the chances of a person to admit.
x = 250
y = m * x + c
print(f"Chances of admit if the TOEFL score {x} is {y}")
