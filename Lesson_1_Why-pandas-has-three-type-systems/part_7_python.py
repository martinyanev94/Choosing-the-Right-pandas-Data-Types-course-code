pd.Series([0, None, 2]).fillna(0).astype(int).mean()

pd.Series([0, None, 2], dtype=pd.Int64Dtype()).mean()
