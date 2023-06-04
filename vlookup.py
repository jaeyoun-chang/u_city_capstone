def vlookup (
    df_main, df_lookup, left_key = None, lookup_col = None, 
    right_key = None, org_key = False, 
    fill_na = False, intsec = 'replace'
    ):
    '''
    function for processing like Excel's vlookup

    df_main: df to receive vlookup values
    df_lookup: df to give vlookup values

    left_key: str / list, mapping column(s) in df_main, default as 1st column of df_lookup
    right_key: str / list, mapping column(s) in df_lookup, default as left_key
    org_key : boolean, selection of using original key(s) or not, default as False
    * default value (org_key = False) 
    enables using modified left/right_keys by fillna('').astype(str).str.strip().str.upper()

    lookup_col = str / list, column(s) of lookup values in df_lookup, default as all columns except right_key

    col_key: str / list, column(s) of vlookup key (both of 2 dataframes must have this column(s))
    col_val: str / list, column(s) of vlookup value
    fill_na: value when vlookup result is null, default as null

    # update: str, update added to lookup_col to keep intersection columns in df_main and df_lookup, default as blank
    # * default value (update = '')
    # *
    # *
    '''
    ### create df_output
    df_output = df_main.copy()



    ### left_key
    # default as 1st column of df_lookup
    if left_key is None:
        left_key = df_lookup.columns[0]
    
    # enlist left_key
    left_key = left_key if type(left_key) == list else [left_key]

    
    
    ### right_key
    # default as left_key
    if right_key is None:
        right_key = left_key
    
    # enlist right_key
    right_key = right_key if type(right_key) == list else [right_key]
    
    
    
    ### lookup_col and modify df_lookup
    # default as none-key columns of df_lookup
    if lookup_col is None:
        lookup_col = [x for x in df_lookup.columns if x not in right_key]

    # enlist lookup_col
    lookup_col = lookup_col if type(lookup_col) == list else [lookup_col]
    
    # modify df_lookup to contain unique right_key and lookup_col
    df_lookup = df_lookup[right_key + lookup_col]
    df_lookup = df_lookup.drop_duplicates(subset = right_key)   
    
    
    
    ### columns of df_output:
    # 1) left_key
    # 1-1) left_key (original)
    # 1-2) left_key modified
    # 2) none-key columns: output_col
    # 2-1) output_col exclusively in df_output: output_col_excl
    # 2-2) output_col intersection with df_lookup: intsec_col
    #
    # categorize columns
    output_col = [x for x in df_output.columns if x not in left_key]
    # output_col_excl = list(x for x in output_col if x not in lookup_col)
    intsec_col = [x for x in output_col if x in lookup_col]
    # df_output_col_excl = list(x for x in df_output.columns if x not in intsec_col)
    
    
    
    ### columns of df_lookup:
    # 3) right_key
    # 3-1) right_key (original)
    # 3-2) right_key modified
    # 4) none-key columns: lookup_col
    # 4-1) lookup_col exclusively in df_lookup: lookup_col_excl
    # 4-2 == 2-2) lookup_col intersection with df_output: intsec_col
    # 5) other columns not belonging to both of right_key and lookup_col in case lookup_col is designated
    # 
    # categorize columns
    lookup_col_excl = [x for x in lookup_col if x not in intsec_col]

    
            
    ### org_key
    # with default False create modified key columns
    if org_key is False:
       
        left_key_modified = list()
        for i in left_key:
            df_lookup = df_lookup.copy() # to avoid SettingWithCopyWarning
            df_output.loc[:, i + '_'] = df_output.loc[:, i].fillna('').astype(str).str.strip().str.upper()
            left_key_modified.append(i + '_')
        left_key = left_key_modified
        # df_output columns:    1-1) left_key (original), 1-2) left_key_modified,
        #                       2-1) output_col_excl, 2-2) intsec_col
        
        right_key_modified = list()
        for i in right_key:
            df_lookup = df_lookup.copy() # to avoid SettingWithCopyWarning
            df_lookup.loc[:, i + '_'] = df_lookup.loc[:, i].fillna('').astype(str).str.strip().str.upper()
            right_key_modified.append(i + '_')
        # drop unnecessary right_key (original)
        df_lookup = df_lookup.drop(right_key, axis = 1)
        right_key = right_key_modified
        # df_lookup columns:    3-2) right_key_modified, 
        #                       4-1) lookup_col_excl, 2-2) intsec_col

    # in case using original columns as keys, create empty lists for dropping after merge
    else:
        left_key_modified = list()
        right_key_modified = list()
        # df_output columns:    1-1) left_key (original), 2-1) output_col_excl, 2-2) intsec_col
        # df_lookup columns:    3-1) right_key (original), 3-1) lookup_col_excl, 2-2) intsec_col


        
    ### merge conditions based on intsec
    if intsec == 'update':
        suffix = '_'
        # after merge:  
        # - on df_output with 1-1) left_key (original), 2-1) output_col_excl and without 2-2) intsec_col 
        #   new values of 4-1) lookup_col_excl from df_lookup to be added
        #   and values of 2-2) intsec_col to be updated
        # - updated values of 2-2) intsec_col to contain new values of lookup_col if they are provided
        #   and original values of df_output if lookup_col values are not provided
        # - columns except intsec_col to keep original order 

    elif intsec == 'copy':
        suffix = '_'
        # after merge:  
        # - on df_output of its original shape with 1-1) left_key (original), 2-1) output_col_excl, 2-2) intsec_col 
        #   new values of 4-1) lookup_col_excl, 2-2) intsec_col with '_' suffix from df_lookup to be added
        # - all columns to keep original order
        
    else:
        df_output = df_output.drop(intsec_col, axis = 1)    
        suffix = ''
        # after merge:  
        # - on df_output with 1-1) left_key (original), 2-1) output_col_excl and without 2-2) intsec_col 
        #   new values of 4) lookup_col from df_lookup to be added
        # - columns except intsec_col to keep original order


    
    ### merge
    df_output = df_output.merge(
        df_lookup,
        left_on = left_key,
        right_on = right_key,
        how = 'left',
        suffixes = ('', suffix)
        ).drop(left_key_modified,axis = 1)
    
    
    
    ### fill_na and reshape based on intsec
    # modify lookup_col for update and copy
    lookup_col_modified = [x if x in lookup_col_excl else x + '_' for x in lookup_col]  
    
    # apply fill_na and reshape for update
    if intsec == 'update':

        for i, j in zip(lookup_col_modified, lookup_col):
            df_output[i] = df_output[i].fillna(df_output[j])
        
        print(df_output.columns)
        df_output_col = [x for x in df_output.columns if x not in intsec_col]
        print(df_output.columns)        
        df_output = df_output[df_output_col]
        
        df_output_col = [x.replace('_', '') for x in df_output.columns]
        print(df_output.columns)
        df_output.columns = df_output_col   
    

    if fill_na:
        # enlist fill_na designated for copy and replace 
        fill_na = fill_na if type(fill_na) == list else [fill_na] * len(lookup_col)          
        
        # apply fill_na for copy
        if intsec == 'copy':    
            lookup_col_modified = [x if x in lookup_col_excl else x + '_' for x in lookup_col]
            for i, j in zip(lookup_col_modified, fill_na):
                df_output[i] = df_output[i].fillna(j)
        
        # apply fill_na for replace
        else:
            # apply fill_na and reshape based on intsec 
            for i, j in zip(lookup_col, fill_na):
                df_output[i] = df_output[i].fillna(j)
        
    return df_output