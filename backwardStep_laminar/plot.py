import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
import seaborn as sns
sns.set_theme(style="ticks")

df = pd.read_csv('step2D_Cp.csv')

fig, ax = plt.subplots(tight_layout=True,figsize=(8, 6), dpi=90)
ax.plot(df['xOF'],df['cpOF'], label='OpenFOAM')
ax.scatter(df['xExp'],df['cpExp'], c='r', label='experimental')
ax.set_xlim([-5.0, 30])
ax.set_xlabel('x/h [m]')
ax.set_ylabel('Cp [-]')
ax.legend()