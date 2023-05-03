
import pandas as pd
import matplotlib.pyplot as plt

degrees =pd.read_csv('CS_degrees.csv',index_col=0)

degrees.plot.bar()
plt.show()
