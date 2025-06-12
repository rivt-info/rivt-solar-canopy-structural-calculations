#! python

import rivtlib.api as rv


# %% Project
rv.I(""" Project Summary | ros | 

    This report **describes** the structural design of a solar canopy
    *covering* a residential patio located in the City of Larkspur, California.
    It includes the design of a concrete slab and *stem* wall, steel tube
    frame, and clip attachments of solar panels to the frame.

    center this text _[C]

    |TABLE| i01/project-data.csv | Title of table, 35, l, [] _[T]

""")


# %% Overview
rv.I(""" Overview and Codes | |

    This report **describes** the structural design of a solar canopy
    *covering* a residential patio located in the City of Larkspur, California.
    It includes the design of a concrete slab and *stem* wall, steel tube
    frame, and clip attachments of solar panels to the frame.

    |IMG| i01/rivt01.png | Wind Load 1, 30

    some text between

    |IMG| i01/site01.png | Wind Load 2, 30

    some more text

    wt2 = 4+ a2 * dl2/2   _[S]

    |TEXT| i01/example1.txt | plain, []

""")


rv.I(""" -- code tables | |

    **Building Codes and Jurisdiction**

    - City of Larkspur, California
    - 2019 California Building Code [CBC]
    - 2019 California Residential Code [CRC]

    |TABLE| i01/cbc2019A_stds.csv | My Table, 53, l, []

    Design loads for the project are from the California Building and
    Residential Codes and are summarized in the following tables.

    |TABLE| i01/load_types01.csv | Another Table Title, 40, l, []

    |TABLE| i01/asce7_load_comb.csv | Load Combinations, 55, c, [] _[T]
    """)


# %% Gravity
rv.V("""Gravity Loads and Seismic Mass | |

    Some calculations


    First Floor Dimensions _[[V]]
    area1 := 10700 * SF |  SF, SM, 2 | roof area
    area2 := 10000 * FT * 10 * FT | SF, SM , 2| floor area
    area3 := 5 * FT * 5 * FT | SF, SM, 2| floor area
    ht1 := 9.0 * FT | FT, M, 2 | wall height 
    len1 := 110 * FT | FT, M, 2 | interior wall length 
    len2 := 155 * FT  | FT, M, 2| exterior wall length
    udl1 := 12.2 * PSF  | PSF, PA | 2, - | description
    _[[Q]]

    A line of text extended text - not formatted

    |VALUE| v01/test1.csv | noprint

    Equation for floor area _[E]
    wt2 := area2 * floordl1  | KIPS, N, 2, 2 | ACI-315-05
    wt3 := area3 * floordl2 * 30/40 | LBF, N, 3, 2 | ACI-315 - 05 

    Exterior wall - total area load _[E]
    |VALUE| v01/test2.csv | noprint
    """)


# %% Abbreviations
rv.S(""" Abbreviations and References | ros |

    **Reference Standards**

    | TEXT | text/txt02/references.txt |  plain

    **Drawing List**

    | TEXT | text/txt02/drawing_list.txt | plain

    **Abbreviations**

    | TEXT | ins01/abbrev_terms.tex | latex

    **Abbreviations - Math**

    | TEXT | ins01/abbrev_math.tex | latex
    """)

# %% Project
rv.S(""" Run

    |WINCMD|
    |WINFILE|

    |LINUXCMD|
    |LINUXFILE|

    |OSXCMD| 
    |OSXFILE| 

""")
# %% Write
rv.S(""" Write 

    |DOC| docrst2pdf | rst2pdf, rivtdoc1.ini

    # ||APPEND| docrst2pdf | file.pdf

    # ||PREPEND| docrst2pdf | file.pdf

""")
