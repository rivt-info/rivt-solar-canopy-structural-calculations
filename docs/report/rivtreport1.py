#! python

from rivtlib.report import *  # noqa: F403

""" generate a rivt report

Run this Python file, after adjusting settings, to generate a report. Different
report settings can be saved by making copies and renaming this file. Output
is written to the docs/report/subfolder where subfolder is the report
type. A flag determines whether the report is assembled from existing doc
files or whether rivt files are first rerun (see "process" below).

Each rivt file is a subdivision within a rivt division (folder). Subdivision
and division titles are constructed by stripping the doc number and replacing
underscores with spaces in the file or folder name. They can be overwritten
(see "files" below).
"""

# ===========================
# process
# ===========================
rerun = False                   # flag that reruns rivt files
rtype = "rst2pdf"               # report type
yamlP = "doc/styles/"
iniP = "doc/styles"

# ===========================
# layout
# ===========================
toc = True                      # insert table of contents
append_count = False            # include append/prepend in page count
charwidth = "80"                # width for text docs
pagesize = "letter"             # page size
header = "<datetime > | Solar Canopy - Larkspur, Ca. | page < page >"
footer = "<datetime > | Solar Canopy - Larkspur, Ca. | page < page >"

# ===========================
# cover and toc
# ===========================
cover_pdf = ""                  # insert cover (overrides other cover settings)
cover_title1 = "Solar Canopy"   # first line of default cover
cover_title2 = "Larkspur, Ca."  # second line of default cover
cover_author = "rhh"            # third line of default cover
cover_image = "img.png"         # image
cover_title3 = "<datetime>"     # last line of default cover

# ===========================
# files
# ===========================
report_include = "all"          # rivt files to include e.g. "r0101, r0201"
report_exclude = ""             # rivt files to exclude e.g. "r0101, r0201"
report_title = "Solar Canopy Calculations"
d01 = "Codes and Loads"         # rename a division
r0101 = "Codes"                 # rename a subdivision (rivt file)
r0102 = "Loads"
d02 = "Frame"
r0201 = "Steel Frame"
r0202 = "Solar Panels"
d03 = "Foundation"
r0301 = "Slab"
r0302 = "Walls"

genreport()  # noqa: F405
