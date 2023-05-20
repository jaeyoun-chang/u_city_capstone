def vlookup (df_main, df_val, col_key, col_val = None, nan_val = False):
    '''
    function like vlookup of Excel
    df_main: df to receive vlookup value
    df_val: df to give vlookup value
    col_key: str or list, column(s) of vlookup key (both of 2 dataframes must have this column(s))
    col_val: str or list, column(s) of vlookup value
    nan_val: value when vlookup result is np.nan, default as np.nan
    '''

    col_key = col_key if type(col_key) == list else [col_key]
    
    if col_val is None:
        col_val = list(filter(lambda x: x not in col_key, df_val.columns))
        # col_val = list(set(df_val.columns) - set(col_key))
    else:    
        col_val = col_val if type(col_val) == list else [col_val]
    col_val = col_val.drop(list(set(df_main.columns).intersection(col_val)))
    
    df_map = df_val[col_key + col_val].copy()
    df_result = df_main.copy()
    
    df_result = df_result.merge(
        df_map,
        on = col_key,
        how = 'left',
        # suffixes=('', '_')
        )
    
    if nan_val:
        df_result[col_val] = df_result[col_val].fillna(nan_val)
    
    return df_result

    # map_dict = df_val[[col_key, col_val]].set_index(col_key)[col_val].to_dict()

    # df_mapped = df_main.copy()
    # df_mapped[col_val] = df_mapped[col_key].map(map_dict)
    
    # if nan_val:
    #     df_mapped[col_val] = df_mapped[col_val].fillna(nan_val)
    
    # return df_mapped

