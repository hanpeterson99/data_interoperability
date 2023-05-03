#Hannah Peterson
#Plot for 9_2.py

import pandas as pd
import matplotlib.pyplot as plt

count = pd.read_csv('tagcount.csv',index_col=0)

count.plot.bar()
plt.title("Tag Count")
plt.ylabel("Count")
plt.xlabel("Tag Title")
plt.show()
