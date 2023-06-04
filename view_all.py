import pandas as pd
import numpy as np
from IPython.display import display
import sys
from contextlib import ExitStack

def view_all (data):
    '''
    function to display all contents of data
    '''
    # with ExitStack() as stack:
    #     stack.enter_context(pd.option_context(
    #     'display.max_rows', None,
    #     'display.max_colwidth', None,
    #     'display.max_seq_items', None
    #     ))
    #     stack.enter_context(np.printoptions(threshold=np.inf))
    
    # np.set_printoptions(threshold = sys.maxsize)
    
    with pd.option_context(
    'display.max_rows', None, 
    'display.max_colwidth', None,
    'display.max_seq_items', None,
    ):
        display(data)