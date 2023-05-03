#Hannah Peterson
#Plot for 9_1.py

import pandas as pd
import matplotlib.pyplot as plt

amount = pd.read_csv('booksPerYear.csv',index_col=0)

amount.plot.bar()
plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Books Per Year")
plt.show()
