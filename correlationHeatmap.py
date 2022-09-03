
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import seaborn as sns

data=pd.read_csv(r'E:\College_Notes\PG\Sem-3\DesignWork\DATA_sets\forestfires.csv')
data.head(10)
#df=pd.DataFrame(data, columns=['x','y'])
datacorr=data.corr()
print(datacorr)



plt.scatter(data['ISI'],data['DMC'],color='red')
plt.xlabel('ISI')
plt.ylabel('DMC')
plt.title('ISI vs DMC')
plt.show()


axis_corr = sns.heatmap(
datacorr,
vmin=-1, vmax=1, center=0,
cmap=sns.diverging_palette(50, 500, n=500),
square=True
)

plt.show()







