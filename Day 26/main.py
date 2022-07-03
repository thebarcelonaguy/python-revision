import pandas

dict_frame = {"student": ["riten", "messi", "pedri"], "marks": [90, 100, 99]}
new_df= pandas.DataFrame(dict_frame)

for (index,row) in new_df.iterrows():
    print(row)
