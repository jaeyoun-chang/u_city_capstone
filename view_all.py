import pandas as pd
from IPython.display import display

def view_all (df):
    '''
    function to display all contents of a dataframe
    '''
        
    with pd.option_context(
    'display.max_rows', None, 'display.max_colwidth', None):
        display(df)