#! python

""" This rivt run file contains settings for generating a rivt report.
Instructions are provided in the docstrings for each function. When the
settings are complete, run the file.

Different settings can be saved by copying and renaming this file.

"""


exclude_divisions():
    """list of divisions to be excluded from the report

    Each division folder starts with a two digit number. List the numbers for
    each division to be excluded from the report, separated by commas.
    
    Example:

    To exclude divisions 02 and 05 
    
    """

    exclude_div=[]



rename_divisions():
    """_summary_

    [report]
    title = Solar Canopy Calculations
    d01 = Codes and Loads
    r0101 = Codes
    r0102 = Loads
    d02 = Frame
    r0201 = Steel Frame
    r0202 = Solar Panels
    d03 = Foundation
    r0301 = Slab
    r0302 = Walls
    """
