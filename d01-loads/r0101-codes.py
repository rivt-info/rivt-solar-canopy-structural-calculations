#! python

import rivtlib.api as rv

rv.I("""project info | norel | none

some text  asdfas

center this text _[C]
  
| TABLE | ins01/project-data.csv:1-0 | 35, l 

""")


rv.I("""Overview and Codes | xchange | none

This report describes the structural design of a solar canopy covering a
residential patio located in the City of Larkspur, California. It includes the
design of a concrete slab and stem wall, steel tube frame, and attachments of
solar panels to the frame. The report is divided into::

    [01] Loads
        [01] Gravity
        [02] Wind and Seismic
    [02] Frame
        [01] Steel tubes 
        [02] Connections and clips 
    [03] Foundation 
        [01] Slab
        [02] Stem wall
    [04] References and Abbreviations
        [01] Codes and Standards
        [02] Abbreviations
        [03] Symbols


This is a structural design calculation document for a residential solar canopy
in Larkspur, California. The design includes a concrete slab, stem wall, steel
welded tube frame, and solar panel clips.

| IMG | ins01/rivt01.png | Wind Load 1, .50, _[F]
| IMG | ins01/site01.png | Wind Load 2, .50, _[F]

# | TEXT | ins01/example1.txt | 1:3 | plain

# wt2 = a2 * dl2/2   _[S]

""")


rv.I("""--code tables | xchange | none 
  
**Building Codes and Jurisdiction**

- City of Larkspur, California
- 2019 California Building Code [CBC]
- 2019 California Residential Code [CRC]

# || TABLE | ins01/cbc2019_stds.csv:1-0 |  53, l

Design loads for the project are from the California Building and
Residential Codes and are summarized in the following tables.

# | TABLE | ins01/load_types01.csv:1-0 | 40, l 

# | TABLE | ins01/asce7_load_comb.csv:1-0 | 55, c                        

""")

# %%
rv.V("""Gravity Loads and Seismic Mass | pass | none

     
# | VCFG | default | default | 2,2
  
Test of values block _[E]
     
|| EVAL | default | 2     
area1 = 10700*SF | SF | roof area      
area2 = 10*FT * 10*FT | SF |  floor area       
ht1 = 9.0*FT | FT | wall height         
len1 = 110*FT | FT | interior wall length
len2 = 155*FT | FT | exterior wall length
udl1 = 12.2*PSF | PSF | description 

Equation 1 _[E]     
wt2 = area2 * floordl1 | KIPS | ACI-315-05 

Equation 2 _[E]
wt3 = area3 * floordl2 | KIPS | ACI-315-05 

|| VALS | val01/aisc-16.0.csv:75-80 | 2
     
|| VALS | val01/dlextwall0.csv:2-4 | 2

Exterior wall - total area load _[E]
|| VALS | ins01/equation1.csv:2-6 | 2

""")

# %%
rv.I("""Abbreviations and References | pass | none

| Reference Standards _[bc] | text/txt02/references.txt:1-0 |  plain

| Drawing List _[bc] | text/txt02/drawing_list.txt:1-0 | plain

| Abbreviations - Terms _[bc] | text/tex02/abbrev_terms.tex:1-0 | plain

| Abbreviations - Math _[bc] | text/tex02/abbrev_math.tex:1-0 | math

""")
# %%
rv.X("""write



""")
