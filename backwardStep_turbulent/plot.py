import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns
# sns.set_theme(style="ticks")

df = pd.read_csv('validation_data/coeffs_validation.csv')
df1 = pd.read_csv('validation_data/of_wall_data.csv')
df1 = df1.sort_values(by=['Points:0'])

# cf = -df1['wallShearStress:0'] / (0.5 * 1 * 42**2)

fig, ax = plt.subplots(tight_layout=True,figsize=(8, 6), dpi=90)
ax.scatter(df['x:cp'],df['cp'], c='r', label='experimental')
ax.plot(df1['Points:0']/0.0127,df1['cp'], label='OpenFOAM')
ax.set_xlim([-5.0, 30])
ax.set_xlabel('x/h [m]')
ax.set_ylabel('Cp [-]')
ax.legend()
plt.savefig('cp.pdf')
# plt.show()

fig, ax = plt.subplots(tight_layout=True,figsize=(8, 6), dpi=90)
ax.scatter(df['x:cf'],df['cf'], c='r', label='experimental')
ax.plot(df1['Points:0']/0.0127, -df1['cf:0'], label='OpenFOAM')
ax.set_xlim([-5.0, 30])
ax.set_xlabel('x/h [m]')
ax.set_ylabel('Cf [-]')
ax.legend()
plt.savefig('cf.pdf')

plt.show()