#! python"ctrl+alt+]"fold
# %%
import rivtlib.rivtapi as rv
# %%
rv.I("""Overview and Codes | pass | none

    This is a structural design calculation document for a residential solar
    canopy in Larkspur, California. The design includes a concrete slab, stem
    wall, steel welded tube frame, and solar panel clips.

    | Wind Load 1 _[f] | images/img02/kitchen.png | 50, bw, 1 
    | Wind Load 2 _[f] | images/img02/as_built1.jpg |  50, none, 0 

    || title | text/txt02/example1.txt:2-5 |  plain
    Some text
    that is used 
    regularly
    -----

    || title | /text/txt02/aci318-05.tex:10-13  | latex
    [ACI 318-12.2] Shear Friction Capacity
    wt1 = area1 * udl1
    wt2 = area2 * udl1
    -----

    Label 1 _[s]
    wt2 = a2 * dl2/2 

    Label 2 _[m]
    a1 = \frac{1}{z}

    """)

rv.I("""--project info | redact | none 
  
    | /csv/tab01/project-data.csv:1-0 | Project Information | 35, l 
    Client, Aaron Kahn
    Address, 10 Fairfield Ave 
    City, Corte Madera
    State, California
    Zip, 94947
    County, Marin
    Project Name, Solar Canopy
    Project Number, 24-001
    Contract Amount, "$1,000" 
    Total Amount, "$1,000"
    Building Code, 2015 CRC
    Date Started, 01-01-2020
    Date Completed, 01-01-2021
    Construction Started, 06-01-2022
    Construction Completed, 06-01-2023
    Materials, "steel, concrete"
    -----------

    """)

rv.I("""--code tables | pass | none 
  
    **Building Codes and Jurisdiction**

    - City of Larkspur, California
    - 2019 California Building Code[CBC]
    - 2019 California Residential Code[CRC]

    || Engineering Standards | tables/tbl02/cbc2019_stds.csv:1-0 |  53, l
    Category,                                            Standard,  Year
    Loading,                                             ASCE-7,    2016
    Concrete,                                            ACI-318,   2014
    Wood-National Design Specifications,                 AWC-NDS,   2018
    Wood-Special Design Provisions for Wind and Seismic, AWC-SDPWS, 2015
    Wood Frame Construction Manual,                      AWC-WFCM,  2018    
    ----------

    Design loads for the project are from the California Building and
    Residential Codes and are summarized in the following tables.

    | Load Types _[t] | tables/tbl02/load_types01.csv:1-0 |  40, l 

    || Load Combinations | insert/ta02/asce7_load_comb.csv:1-0 |  55, c
    CBC 2019 reference, Equation                                             
    Equation 16-1,      1.4(D +F)                                            
    Equation 16-2,      1.2(D + F) + l.6(L + H) + 0.5(L or S or R)
    Equation 16-3,      1.2(D + F) + l.6(Lr or S or R) + l.6H + (f1L or 0.5W)
    Equation 16-4,      1.2(D + F) + 1.0W + f1L +1.6H + 0.5(Lr or S or R)    
    Equation 16-5,      1.2(D + F) + 1.0E + f1L + l.6H + f2S                 
    Equation 16-6,      0.9D+ l.0W + l.6H                                     
    Equation 16-7,      0.9(D + F) + 1.0E+ l.6H                              
    -----------

    """)

# %%
rv.V("""Gravity Loads and Seismic Mass | pass | none

    area1 :=, 10700, SF, SM, roof area           
    area2 :=, 10200, SF, SM, floor area          
    ht1 :=,   9.0,   FT, M,  wall height         
    len1 :=,  110,   FT, M,  interior wall length
    len2 :=,  155,   FT, M,  exterior wall length

    || aisc shapes _[o] | values/dat02/aisc-16.0.csv:75-80 | [1,3:7] 

    || first floor _[v] | values/val01/dlextwall0.csv:2-4 | ref
    Wall Assembly Dead Loads
    t1_f :=,   .5,  IN,  MM,  flange thickness       
    ld2 :=,    2.,  PSF, KPA, 2x4 studs at 16 in o.c.
    ld3 :=,    3.,  PSF, KPA, 5/8 in sheet rock
    ld4 :=,    1.5, PSF, KPA, fixtures             
    totdl1 :=, 7.0, PSF, KPA, total load                          
    ------

    Exterior wall - total area load _[v]
    udl1 :=, 12.2,PSF,KPA,description 

    || Beam 1 _[e] | text/equ02/equation1.txt:2-4 | ref
    [ACI 318-12.2] Shear Friction Capacity 
    wt1 = area1 * udl1 | KIPS, KN, 2, 2
    wt2 = area2 * udl1 | KIPS, KN, 2, 2
    ------

    wt2 = area2 * floordl1 | KIPS,KN,2,2

    | Wind Load 1 _[f] | images/img02/fig1.png | 50, bw, 0  
    | Wind Load 2 _[f] | images/img02/fig2.png | 70, none, 0

    """)

# %%
rv.I("""Abbreviations and References | pass | none

    | Reference Standards _[bc] | text/txt02/references.txt:1-0 |  plain
    
    | Drawing List _[bc] | text/txt02/drawing_list.txt:1-0 | plain
    
    | Abbreviations - Terms _[bc] | text/tex02/abbrev_terms.tex:1-0 | plain

    | Abbreviations - Math _[bc] | text/tex02/abbrev_math.tex:1-0 | math
    
    """)

# %%
rv.W("""docs

    | docs | text, html, pdf | page #; auto


    """)
