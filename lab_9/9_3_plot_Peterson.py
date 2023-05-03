#Hannah Peterson
#Plot for 9_3.py

import pandas as pd
import matplotlib.pyplot as plt

count = pd.read_csv('doctypesCount.csv',index_col=0)

count.plot.bar()
plt.title("Count of Doctypes")
plt.ylabel("Count")
plt.xlabel("Doctype")
plt.show()
