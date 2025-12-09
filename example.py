import pandas as pd
df=pd.read_csv("C:\\Pandas\\sample.csv")
df.info()
df.describe()
mean_values =df.mean(numeric_only=True)
print("mean:\n",mean_values)

median_values=df.median(numeric_only=True)
print("median:\n",median_values)

mode_values=df.mode(numeric_only=True)
print("mode:\n",mode_values)

import numpy as np
persentiles=np.percentile(df['price'],[25,50,75])
print("price percentitles(25%,50%,75%):",persentiles)
      