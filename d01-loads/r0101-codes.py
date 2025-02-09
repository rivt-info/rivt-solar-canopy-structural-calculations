#! python
# %%
import rivtlib.api as rv

rv.I(""" Project Summary | xoss | none

some text  asdfas

center this text _[C]
  
# | TABLE | ins01/project-data.csv:1-0 | 35, l 

""")


rv.I(""" Overview and Codes | xoss | none

This report describes the structural design of a solar canopy covering a
residential patio located in the City of Larkspur, California. It includes the
design of a concrete slab and stem wall, steel tube frame, and attachments of
solar panels to the frame. The report is divided into::


| IMG | ins01/rivt01.png | Wind Load 1, .6
     

This is a structural design calculation document for a residential solar canopy
in Larkspur, California. The design includes a concrete slab, stem wall, steel
welded tube frame, and solar panel clips.

| IMG | ins01/site01.png | Wind Load 2, .2
     
     
# | TEXT | ins01/example1.txt | 1:3 | plain

# wt2 = a2 * dl2/2   _[S]

""")

# %%
rv.I(""" --code tables | xoss | none 
  
**Building Codes and Jurisdiction**

- City of Larkspur, California
- 2019 California Building Code [CBC]
- 2019 California Residential Code [CRC]


| TABLE | ins01/cbc2019A_stds.csv:1-0 |  53, l

Design loads for the project are from the California Building and
Residential Codes and are summarized in the following tables.

| TABLE | ins01/load_types01.csv:1-0 | 40, l 

| TABLE | ins01/asce7_load_comb.csv:1-0 | 55, c                        

""")


# %%
rv.X(""" Abbreviations and References | oss | none

**Reference Standards**

| TEXT | text/txt02/references.txt:1-0 |  plain

**Drawing List**
     
| TEXT | text/txt02/drawing_list.txt:1-0 | plain

**Abbreviations**

| TEXT | ins01/abbrev_terms.tex:1-0 | latex

**Abbreviations - Math**

| TEXT | ins01/abbrev_math.tex:1-0 | latex

""")
# %%
rv.X(""" Write



""")
