"""
Think Stats 2
Chapter 1 exercise 2
Cleaning and importing module
"""

from __future__ import print_function, division
from collections import defaultdict

import numpy as np
import thinkstats2 as ts
import sys


def ReadFemResp(dct_file = '2002FemResp.dct',
                dta_file = '2002FemResp.dat.gz',
                nrows = None):
    """
    Read the NSFG data

    :param dct_file: string
    :param dta_file: string
    :param nrows:
    :return: dataframe
    """
    dct = ts.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dta_file, compression = 'gzip', nrows = nrows)
    CleanFemResp(df)
    return df

def CleanFemResp(df):
    """
    Clean the FemResp Data

    :param df: dataframe
    :return: dataframe
    """
    #TODO

def main():
    """
    Test the fonction in the module
    :return: nothing
    """
    #TODO


if __name__ == "__main__":
    main()
    df = ReadFemResp()
    print(df.head())
