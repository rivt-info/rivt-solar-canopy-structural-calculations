#! python

from rivtlib.rwrite import Report

Report.repx("rivt-report.ini")

""" generate a rivt report

This run file contains settings for generating a rivt report. Instructions and
examples are provided in the docstrings for each function. Different report
versions can be saved by saving and renaming copies of this file.

There 10 settings:

    1 - publish_types
    2 - background_images
    3 - reruns_specified
    4 - override_distribution
    5 - exclude_divisions
    6 - exclude_documents
    7 - rename_parts
    8 - append_end
    9 - prepend_start

After completing settings run this file to generate the report. Output will be
written to

"""

# ============================================================================ #
# 5 - exclude divisions
# ============================================================================ #


def exclude_divisions():
    """
    list of divisions to be excluded from the report

    Each division folder starts with a two digit number. List the numbers in
    quotes for each division to be excluded from the report, separated by
    commas.

    Example:
    To exclude divisions 02 and 05 provide the following entry:

        return exclude_div := ["02", "05"]

    To include all divisions leave the list empty.
    """

    return exclude_divs := []

# ============================================================================ #
# 6 - exclude documents
# ============================================================================ #


def exclude_documents():
    """
    list of documents to be excluded from the report

    Each document starts with a four digit number. List the numbers in quotes
    for each document to be excluded from the report, separated by commas.

    Example:
    To exclude documents 02 and 03 from division 01 and document 04
    from division 02 provide the following entry:

        return exclude_docs = ["0102", "0103", "0204"]

    To include all documents leave the list empty.

    """

    return exclude_docs := []

# ============================================================================ #
# rename divisions
# ============================================================================ #


def rename_divisions():
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


s1 = exclude_documents()
s2 = exclude_divisions()
s3 = rename_divisions()


genreport.run(s1, s2, s3, s4, s5, s6, s7, s8, s9)
