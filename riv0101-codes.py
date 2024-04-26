#! python\"ctrl+["
# %%
import rivtlib.rivtapi as rv
# %%
rv.I("""Overview and Codes | pass | none

    This document is a solar canopy structural design for a residence located
    in Larkspur, California. The design includes a concrete slab and stem wall,
    a steel welded tube frame, and solar panel clips.

    || image | 2x1 | bw
    Wind load 1 | /images/im02/kitchen.png | 50 
    Wind load 2 | /images/im02/as_built1.jpg | 50
    ----- 

    ||| latex | text/te02/tex-aci318-05.txt:10 | 4
    [ACI 318-12.2] Shear Friction Capacity
    wt1 = area1 * udl1
    wt2 = area2 * udl1
    -----

    ||| sympy | text/te02/sym-aci318-05.txt:10 | 4
    [ACI 318-12.2] Shear Friction Capacity
    wt1 = area1 * udl1
    wt2 = area2 * udl1
    -----

    | sympy | Shear Friction Capacity | c
    wt2 = area2 * floordl1 
    -----

    || latex | Shear Friction Capacity | l
    wt2 = area2 * floordl1 
    -----

    """)

rv.I("""--project info | redact | none 
  
    | Project Information | text/te01/project-data.csv | 35, l
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

    ||| Engineering Standards  | insert/ta02/cbc2019_stds.csv | 53, l
    Category,                                            Standard,  Year
    Loading,                                             ASCE-7,    2016
    Concrete,                                            ACI-318,   2014
    Wood-National Design Specifications,                 AWC-NDS,   2018
    Wood-Special Design Provisions for Wind and Seismic, AWC-SDPWS, 2015
    Wood Frame Construction Manual,                      AWC-WFCM,  2018    
    ----------

    Design loads for the project are from the California Building and
    Residential Codes and are summarized in the following tables.

    | Load Types | insert/ta02/load_types01.csv | 40, l 
    --------

    |-| Load Combinations | insert/ta02/asce7_load_comb.csv | 55, c
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
rv.V("""Gravity Loads and Seismic Mass | none | pass

    Check declare command

    **Areas **
    area1 := 1700*SF | SM | roof area
    area2 := 1200*SF | SM | floor area
    ht1 := 9*FT | M | wall height
    len1 := 110*FT | M | interior wall length
    len2 := 155*FT | M | exterior wall length


    ||| Exterior wall unit dead loads | insert/ta01/dlextwall0.csv |
    ld1,        2.,    PSF,   KPA,   1/2 in plywood sheathing
    ld2,        2.,    PSF,   KPA,   2x4 studs at 16 in o.c.
    ld3,        3.,    PSF,   KPA,   5/8 in sheet rock
    ld4,        1.5,   PSF,   KPA,   fixtures
    -----

    udl1 := sum(col2L)*PSF | KPA | exterior wall total area load

    ||| equation | values/va02/eq-aci318-05.txt:10 | 4
    [ACI 318-12.2] Shear Friction Capacity | KIPS, KN | 2, 2
    wt1 = area1 * udl1
    wt2 = area2 * udl1
    ----------

    || eq | Shear Friction Capacity | KIPS, KN, 2, 2
    wt2 = area2 * floordl1 
    -----------

    || image | 2x1 | none
    Wind load 1 | image/im01/fig1.png | 75 |
    Wind load 2 | image/im01/fig2.png | 75 |
    -------------

    """)

# %%
rv.I("""Abbreviations and References | pass | none
    References _[bc]

    | references | data/references.txt | plain


    Drawings _[bc]

    | text | data/drawing_list.txt | plain


    Abbreviations - Terms _[bc]

    | text | data/abbrev_terms.tex | plain


    Abbreviations - Math _[bc]

    | text | data/abbrev_math.tex | plain
    """)

rv.W("txt, pdf:pdf-style4.sty")
