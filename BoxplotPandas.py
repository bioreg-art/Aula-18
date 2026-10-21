import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\regina.alvarenga\Downloads\funcionarios.csv")


print(df)

lucro = df["lucro"].to_numpy()

print(lucro)

q1 = np.percentile(lucro, 25)
q2 = np.percentile(lucro, 50)
q3 = np.percentile(lucro, 75)

print("Primeiro Quartil\n")
print(q1)
print("\nMediana\n")
print(q2)
print("\nTerceiro Quartil\n")
print(q3)




