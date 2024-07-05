import pandas as pd
import numpy as np
# dict = {"Country": ["Brazil", "Russia", "India", "China", "South Africa"],
#         "Capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
#         "Area": [8.516, 17.10, 3.286, 9.597, 1.221],
#         "Population": [200.4, 143.5, 1252, 1357, 52.98]}
#
# brics = pd.DataFrame(dict)
# print(brics)
# brics.to_csv("fff.csv")

dates = pd.date_range("20130101", periods=6)
# print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
# print(df)
# print(df.tail(3))
# print(df.to_numpy())
# print(df.describe())
# print(df.T)
# df.sort_index(axis=1, ascending=False)
# print(df)
# print(df["A"])
# print(df.loc[dates[0]])
# print(df)
# print(df.iloc[3:5, 0:3])

# import matplotlib.pyplot as plt
# plt.close("all")
# ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
# ts = ts.cumsum()
# ts.plot()
# plt.show()


