import pandas as pd
Data = pd.read_csv('Penguins.csv', delimiter=';')
print(Data[Data['species']=="Adelie"])