import numpy as np
import pandas as pd

data= pd.read_csv("./data/entries.csv")
X=data[["x1","x2"]]
Y=data["y"]

print(X)
print(Y)