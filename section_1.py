def msno_overview (data, chunk_size = 100):
    '''
    function to display missing value using missingno library
    data: dataframe
    chunk_size: int, size of column chunk, 100 as default  
    '''
    # split data columns into chunks
    chunk_size = chunk_size
    column_chunks = [data.iloc[:, i : i + chunk_size] for i in range(0, data.shape[1], chunk_size)]

    # generate and display missingno plots for each chunk
    for i, j in enumerate(column_chunks):
        msno.matrix(j, figsize = (10, 3), fontsize = 8, labels = False, sparkline = False)
        plt.title(
            f'{data.name}: missing value overview - column {i * 100} to {min (i * chunk_size + chunk_size - 1, data.shape[1] - 1)}',
            fontsize = 10);