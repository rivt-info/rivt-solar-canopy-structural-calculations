#! python"ctrl+alt+]"fold
# %%
import rivtlib.api as rv
# %%
rv.W("""write-settings | public  | nocolor  

# write text
# write pdf
# write html

""")

rv.I("""project info | priv | none 
  
|| /s01/ins/project-data.csv | all | Project Information | 35, l 

""")


rv.I("""Overview and Codes | pub | none

This report describes the structural design of a solar canopy covering a
residential patio located in the City of Larkspur, California. It includes the
design of a concrete slab and stem wall, steel tube frame, and attachments of
solar panels to the frame. The report is divided into the following divisions
and subdivisions::

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

|| images/img02/kitchen.png | Wind Load 1 _[f] |  50, bw, 1 
|| images/img02/as_built1.jpg | Wind Load 2 _[f] | 50, none, 0 

|| r01/ins/example1.txt | 1:3 | plain

|| /text/txt02/aci318-05.tex | latex
[ACI 318-12.2] Shear Friction Capacity
wt1 = area1 * udl1
wt2 = area2 * udl1


Label 1 _[e] 
wt2 = a2 * dl2/2   _[s]

a1 = \frac{1}{z}   _[l]

""")


rv.I("""--code tables | pass | none 
  
**Building Codes and Jurisdiction**

- City of Larkspur, California
- 2019 California Building Code[CBC]
- 2019 California Residential Code[CRC]

|| table | ins/d01/cbc2019_stds.csv:1-0 |  53, l

Design loads for the project are from the California Building and
Residential Codes and are summarized in the following tables.

| table | ins/d01/load_types01.csv:0 |  40, l 

|| table | ins/d01/asce7_load_comb.csv:1-0 |  55, c                        

""")

# %%
rv.V("""Gravity Loads and Seismic Mass | pass | none

area1 := 10700*SF 
area2 := 10200*SF          
ht1 := 9.0*FT, wall height         
len1 := 110*FT, interior wall length
len2 := 155*FT, exterior wall length
udl1 := 12.2*PSF, description 

|| eval | val/d01/aisc-16.0.csv:75-80 | [1,3:7] 

Wall Assembly Dead Loads
|| assign | values/val01/dlextwall0.csv:2-4 | ref


Exterior wall - total area load _[v]

|| eval | ins/d01/equation1.txt:2 | 1:4

Beams _[e]
wt2 = area2 * floordl1 | KIP,2 | ACI

|| image | Wind Load 1 _[f] | ins/d01/rivt01.png | 50
|| image | Wind Load 2 _[f] | ins/d01/site01.png | 70

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
