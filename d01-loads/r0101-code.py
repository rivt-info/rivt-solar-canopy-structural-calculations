#! python

import rivtlib.api as rv

rv.S(""" Write | |

| | COVER | My Report 1 | written by R Holland | bottom text | rivt01.png

| | DOC | docs / pdf / | pdf, cover, rivt01

# ||REPORT| docs/pdf2/ | pdf2

# ||APPEND| docs/pdf2/ | file.pdf

# ||PREPEND| docs/pdf2/ | file.pdf
""")

# %% Project
rv.I(""" Project Summary | | oss

This report ** describes ** the structural design of a solar canopy that covers a
residential patio located in the City of Larkspur, California. It includes the
design of a concrete slab and *stem * wall, steel tube frame, and clip
attachments of solar panels to the frame.

center this text _[C]

|TABLE | ins / i01 / project - data.csv | Title of table, 35, l, [], _[T]
""")

# %% Overview
rv.I(""" Overview and Codes | |

This report ** describes ** the structural design of a solar canopy * covering * a
residential patio located in the City of Larkspur, California. It includes the
design of a concrete slab and *stem * wall, steel tube frame, and clip
attachments of solar panels to the frame.xxxx

|IMG | ins / i01 / rivt01.png | Wind Load 1, 30, _[F]

some text between

|IMG | ins / i01 / site01.png | Wind Load 2, 30, _[F]

some more text

wt2 = 4 + a2 * dl2 / 2   _[S]

New Table _[T]

======= ======== =====
col1     col2    col3
======= ======== =====
 A1       23     10
 B1      11.1    15.0
======= ======== =====

# |TEXT| ins/i01/example1.txt | preformat

""")

# %% code
rv.I(""" -- code tables | |

**Building Codes and Jurisdiction**

- City of Larkspur, California
- 2019 California Building Code[CBC]
- 2019 California Residential Code[CRC]

|TABLE | ins / i01 / cbc2019A_stds.csv | My Table, 53, l, [], _[T]

Design load combinations are from *California Building and Residential Codes*
and are summarized in the following tables.

|TABLE | ins / i01 / load_types01.csv | Another Table Title, 40, l, [], _[T]


|TABLE | ins / i01 / asce7_load_comb.csv | xxx, 55, c, [], _[T]
""")

# %% Gravity
rv.V("""Gravity Loads and Seismic Mass | |

Dimensions for the first floor structural layout are as follows.

First Floor Dimensions _[[V]]
area1 := 10700 * SF | roof area | SF, SM | 2, 2
area2 := 10000 * FT * 10 * FT | floor area | SF, SM | 2, 2
area3 := 5 * FT * 5 * FT | floor area | SF, SM | 2, 2
ht1 := 9.0 * FT | wall height | FT, M | 2, 2
len1 := 110 * FT | interior wall length | FT, M | 2, 2
len2 := 155 * FT | exterior wall length | FT, M | 2, 2
udl1 := 12.2 * PSF | description | PSF, PA | 2, 2
_[[Q]]

Additional values from a file.

|VALUES | vls / v01 / test1.csv | Another values table _[T]

Equation for floor area _[E]

wt2 := area2 * floordl1 | ACI - 315 - 05 | KIPS, N | 2, 2

Equation for wall area _[E]

wt3 := area3 * (floordl2 * .1) | ACI - 315 - 05 | LBF, N | 1, 2

|VALUES | vls / v01 / test2.csv | Exterior wall - total area load _[T]

""")

# %% Abbreviations
rv.S(""" Abbreviations and References | yes | none

**Reference Standards**

|TEXT | ins / i02 / references.txt | plain

**Drawing List**

|TEXT | ins / i02 / drawing_list.txt | plain

**Abbreviations**

|TEXT | ins / i01 / abbrev_terms.tex | latex

**Abbreviations - Math**

|TEXT | ins / i01 / abbrev_math.tex | latex

""")
