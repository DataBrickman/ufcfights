import pandas as pd

def read_data(csv_file):
    data = pd.read_csv(csv_file, sep='\t', header=None)
    return data
