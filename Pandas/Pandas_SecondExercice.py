import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

web_stats = {'Day': [1,2,3,4,5,6],
             'Visitors':[43,53,34,45,64,34],
             'Bounce_Rate': [65,72,62,64,54,66]}

df = pd.DataFrame(web_stats)

#print(df)
#print(df.head())
#print(df.tail())
#print(df.tail(2))


#print(df.set_index('Day'))
#print(df.head())

#df2 = df.set_index('Day')
#print(df2.head())

#print(df.head())
#set an index in the same dataset
#df.set_index('Day', inplace=True)
#print(df.head())

#print(df['Visitors'])
#print(df.Visitors)

print(df.Visitors.tolist())

#using numpy
print(np.array(df[['Bounce_Rate', 'Visitors']]))
