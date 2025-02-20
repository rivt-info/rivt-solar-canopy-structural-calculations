#! python
# %%
import rivtlib.api as rv

rv.I(""" Project Summary | xos | none

some text  asdfas

center this text _[C]
  
# | TABLE | ins01/project-data.csv | 35, l, [] 

""")

rv.I(""" Overview and Codes | xos | none

This report describes the structural design of a solar canopy covering a
residential patio located in the City of Larkspur, California. It includes the
design of a concrete slab and stem wall, steel tube frame, and clip attachments
of solar panels to the frame.


| IMG | ins01/rivt01.png | Wind Load 1, 30
     
| IMG | ins01/site01.png | Wind Load 2, 30
     
wt2 = a2 * dl2/2   _[S]

# | TEXT | ins01/example1.txt | plain, []
""")

# %%
rv.I(""" --code tables | xos | none 

**Building Codes and Jurisdiction**

- City of Larkspur, California
- 2019 California Building Code [CBC]
- 2019 California Residential Code [CRC]

Loading _[T]
| TABLE | ins01/cbc2019A_stds.csv | 53, l, []

Design loads for the project are from the California Building and
Residential Codes and are summarized in the following tables.

| TABLE | ins01/load_types01.csv | 40, l, [] 


Load Combinations _[T]
| TABLE | ins01/asce7_load_comb.csv | 55, c, []                        

""")

# %%
rv.V("""Gravity Loads and Seismic Mass | os | none

First floor dimensions _[E]
_[[V]]   
area1 = 10700*SF | roof area | SF, SM | 2,2       

area2 = 10000*FT * 10*FT | floor area | SF, SM | 2,2         

area3 = 5*FT * 5*FT | floor area | SF, SM | 2,2         

ht1 = 9.0*FT | wall height  | FT, M | 2,2       

len1 = 110*FT | interior wall length | FT, M | 2,2

len2 = 155*FT | exterior wall length | FT, M | 2,2 

udl1 = 12.2*PSF | description | PSF, PA | 2,2 
_[[Q]]

A line of text extended text - not formatted    

| VALREAD | v01/test1.csv | noprint


Equation for floor area _[E]    
wt2 = area2 * floordl1 | ACI-315-05 | KIPS, N | 2,2



Equation for wall area _[E]
wt3 = area3 * (floordl2 * .1) | ACI-315-05 | LBF, N | 1,2



Exterior wall - total area load _[E]
| VALREAD | v01/test2.csv | noprint

""")

# %%
rv.X(""" Abbreviations and References | os | none

**Reference Standards**

| TEXT | text/txt02/references.txt |  plain

**Drawing List**
     
| TEXT | text/txt02/drawing_list.txt | plain

**Abbreviations**

| TEXT | ins01/abbrev_terms.tex | latex

**Abbreviations - Math**

| TEXT | ins01/abbrev_math.tex | latex

""")

# %%
rv.X(""" Write | os | none

|| DOC | docs | pdf

""")

rv.Q()
