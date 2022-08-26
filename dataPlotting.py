import matplotlib.pyplot as plt
import pandas as pd

#df = pd.read_csv (r'E:\College_Notes\PG\Sem-3\DesignWork\DATA(s)\forestfires.csv')
#print (df)



data = pd.read_csv (r'E:\College_Notes\PG\Sem-3\DesignWork\DATA(s)\forestfires.csv')   
print(data)
df = pd.DataFrame(data, columns= ['x','y','FFMC','DMC','DC','ISI',"temp",'RH','wind','area','rain'])
print (df)

plt.scatter(df['FFMC'],df['DMC'],df['DC'],df['ISI'])
plt.show()