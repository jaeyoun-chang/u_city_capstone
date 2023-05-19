def vlookup (df_main, df_val, col_key, col_val, nan_val = False):
    '''
    function like vlookup of Excel
    df_main: df to receive vlookup value
    df_val: df to give vlookup value
    col_key: str, column of vlookup key (both 2 dataframes must have this column)
    col_val: str, column of vlookup value
    nan_val: value when vlookup result is np.nan, default as np.nan
    '''
    map_dict = df_val[[col_key, col_val]].set_index(col_key)[col_val].to_dict()

    df_mapped = df_main.copy()
    df_mapped[col_val] = df_mapped[col_key].map(map_dict)
    
    if nan_val:
        df_mapped[col_val] = df_mapped[col_val].fillna(nan_val)
    
    return df_mapped