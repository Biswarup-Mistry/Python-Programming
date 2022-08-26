import pandas as pd

#df = pd.read_csv (r'E:\College_Notes\PG\Sem-3\DesignWork\DATA(s)\forestfires.csv')
#print (df)



data = pd.read_csv (r'E:\College_Notes\PG\Sem-3\DesignWork\DATA(s)\forestfires.csv')   
print(data)
df = pd.DataFrame(data, columns= ['month','rain'])
print (df)