
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np


# In[27]:


# NIM = 1301204031
print("Input your NIM")
NIM = input(":")

try:
    NIM = int(NIM)
    np.random.seed(NIM)
    x1 = np.random.randint(1, high=50, size=10)
    x2 = np.random.randint(2, high=50, size=10)
    tmp_dict = {"x1": x1, "x2": x2}
    df = pd.DataFrame(tmp_dict)
    df["class (1 or 2)"] = ""

    tmp_dict = {"iteration": list(np.arange(5))}

    np.random.seed(NIM)
    x1 = np.random.randint(1, high=50, size=2)
    x2 = np.random.randint(2, high=50, size=2)

    tmp_dict["x1-centroid-1"] = x1[0]
    tmp_dict["x2-centroid-1"] = x1[1]
    tmp_dict["x1-centroid-2"] = x2[0]
    tmp_dict["x2-centroid-2"] = x2[1]

    cent_df = pd.DataFrame(tmp_dict)

    for i in range(4):
        cent_df.loc[i+1, "x1-centroid-1"] = ""
        cent_df.loc[i+1, "x2-centroid-1"] = ""
        cent_df.loc[i+1, "x1-centroid-2"] = ""
        cent_df.loc[i+1, "x2-centroid-2"] = ""

    with pd.ExcelWriter('Data_Set_{}.xlsx'.format(NIM)) as writer:
        df.to_excel(writer, sheet_name='Data Set', index=None)
        cent_df.to_excel(writer, sheet_name='Centroid', index=None)

except:
    print("Error: input is invalid: value is not a number")
