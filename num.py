import pandas as pd
def num_to_df(num):
    """
    Convert a number to a DataFrame with a single column 'num'.
    
    Parameters:
    num (int or float): The number to convert.
    
    Returns:
    pd.DataFrame: A DataFrame with one column 'num' containing the input number.
    """
    return pd.DataFrame({'num': [num]}) 