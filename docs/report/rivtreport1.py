#! python

from rivtlib.rvreport import *  # noqa: F403

""" generate rivt report

Different report settings can be saved by renaming copies of this file. After
adjusting settings run the file to generate the report.

Each rivt file is a report subdivision, where subdivisions are contained in a
division folder. Subdivision and division titles are inferred by stripping the
doc number and replacing underscores with spaces. Titels can be overridden
as shown below in the example file.

A process setting determines whether the report is assembled from existing doc
files or whether the rivt files are first rerun.

Output will be written to docs/report/subfolder where subfolder is the report
type.

"""

# ===========================
# process
# ===========================
dtype = "rst2pdf"               # doc type
rerun = False                   # rerun rivt files before assembling report

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
# cover
# ===========================
cover_pdf = ""                  # insert cover - overrides other cover settings
cover_title1 = "Solar Canopy"   # first line of std. cover
cover_title2 = "Larkspur, Ca."  # second line of std. cover
cover_author = "rhh"            # third line of std. cover
cover_image = "img.png"         # image
cover_title3 = "<datetime>"     # last line of std. cover

# ===========================
# include and rename files
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
