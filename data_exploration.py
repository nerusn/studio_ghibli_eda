import json
import pandas as pd
import matplotlib.pyplot as plt

with open('ghibli_data.json') as f:
    data = json.load(f)

df = pd.DataFrame.from_dict(data, orient = 'columns')

print(df.head())

plt.hist(df['score'])
#TEST CODE
