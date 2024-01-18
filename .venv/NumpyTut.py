import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# a1=np.array([[1,2],[4,5]])
# a2=np.array([[1,2],[4,5]])
# print(a1*a2)
# print(a1.shape)
# print(a1[1,1])
# print(np.matmul(a1,a2))

dic1={
    "name":['Neel','Naman','Varana','Kevin'],
    "marks":[89,78,72,56]
}
# df1=pd.DataFrame(dic1)
# # df1.to_csv('marks.csv')
# print(df1)
# print(df1.marks.describe())
# # print(df1)

df2 = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])
df2.plot.bar()
plt.show()
