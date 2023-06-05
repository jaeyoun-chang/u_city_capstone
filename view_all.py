import pandas as pd
from IPython.display import display

def view_all (data):
    '''
    function to display all contents of data
    '''
    
    with pd.option_context(
    'display.max_rows', None, 
    'display.max_colwidth', None,
    'display.max_seq_items', None,
    ):
        display(data)