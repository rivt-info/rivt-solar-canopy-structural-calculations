#! python

from rivtlib.rvreport import *  # noqa: F403

""" generate rivt report

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

cover_pdf = "path"
cover_title1 = "Solar Canopy"
cover_title2 = "Larkspur, Ca."
cover_title3 = "<datetime>"
cover_image = "img.png"
cover_author = "rhh"
header = "<datetime > | Solar Canopy - Larkspur, Ca. | page < page >"
footer = "<datetime > | Solar Canopy - Larkspur, Ca. | page < page >"
charwidth = "80"
pagesize = "letter"

report_include = "all"
report_exclude = ""
toc = True
attach_num = True


genreport("rst2pdf")  # noqa: F405
