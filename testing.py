import pandas as pd
import numpy as np 

# Trying to play around with the data, get familiar with VS studio, 
# and trying to figure out everything to do within the pandas module

# Pull in the data frame
df = pd.read_table('causes_of_death.tsv')

# Get a list of all Males from Alabama
males_alabama_df = df.loc(
    (df['State'] == 'Alabama') 
    & (df['Gender Code'] == 'M')
    )

