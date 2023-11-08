import pandas as pd


def read_data_files(frugal:bool=True):
    """
    Frugal option to read only the main necessary dataset
    """

    cox_violent_parsed_filt = pd.read_csv("../data/raw/archive/cox-violent-parsed_filt.csv")

    if not frugal:
        compas_scores_raw = pd.read_csv("../data/raw/archive/compas-scores-raw.csv")
        cox_violent_parsed  = pd.read_csv("../data/raw/archive/cox-violent-parsed.csv")

        return compas_scores_raw, cox_violent_parsed_filt, cox_violent_parsed
    
    return cox_violent_parsed_filt