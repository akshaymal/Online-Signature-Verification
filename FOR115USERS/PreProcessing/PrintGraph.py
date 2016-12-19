import matplotlib.pyplot as plt 
import pandas as pd 

df_ = pd.read_table('001_1_1.sig', sep=' ', header=None)
df_orig = pd.read_table('1Dataset/VisualSubCorpus/GENUINE/SESSION1/001_1_1.sig', sep=' ', skiprows=[1])

plt.subplot(2,1,1)
plt.plot(df_orig['X,'], df_orig['Y,'])
plt.subplot(2,1,2)
plt.plot(df_[[0]], df_[[1]])
plt.show()