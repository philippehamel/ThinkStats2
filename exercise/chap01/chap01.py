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
import nsfg


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


def ValidatePregnum(resp):
    """Validate pregnum in the respondent file.

    resp: respondent DataFrame
    """
    # read the pregnancy frame
    preg = nsfg.ReadFemPreg()

    # make the map from caseid to list of pregnancy indices
    preg_map = nsfg.MakePregMap(preg)

    # iterate through the respondent pregnum series
    for index, pregnum in resp.pregnum.items():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]

        # check that pregnum from the respondent file equals
        # the number of records in the pregnancy file
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = ReadFemResp()

    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    assert(ValidatePregnum(resp))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)

