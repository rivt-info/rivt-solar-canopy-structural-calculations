#! python\
# %%
import rivtlib.rivtapi as rv
# %%
rv.I("""Overview and Codes | none | pass

    This structural design is for a residential solar canopy located in
    Larkspur, California. The design includes a concrete slab and stem
    wall, a steel welded tube frame, and solar panel clips.

    || project info | data/te01/project-data.txt | plain


     **Building Codes and Jurisdiction**
     
    - City of Larkspur, California 
    - 2019 California Building Code [CBC]
    - 2019 California Residential Code [CRC]
    
    || Exterior wall unit dead loads | data/va01/dlextwall0a.csv |
    variable, value, unit1, unit2 , description                  
    ld1,      2,     PSF,   KPA,    1/2 in plywood sheathing     
    ld2,      2,     PSF,   KPA,    2x4 studs at 16 in o.c.      
    ld3,      3.0,   PSF,   KPA,    5/8 in sheet rock            
    ld4,      1.5,   PSF,   KPA,    fixtures                     
    ===,      ===,   ===,   ===,    ===                          
    exdl1,    8.5,   PSF,   KPA,    Total exterior wall unit load
    ----  
    
    || Table of Engineering Standards | in01/cbc2019_stds.xlsx | 53,l 
 
    Design loads for the project are from the California
    Building and Residential Codes and are shown in the following tables.
    
    || Load Types | data/va01/load_types01.csv | 40,l 
    
    || Load Combinations | data/va02/asce7_load_comb.csv | 55,c 

    """)

# %%
rv.V("""Gravity Loads and Seismic Mass | none | pass 
    
    Check declare command

    || Floor unit dead loads | data/va01/rv-dlfloor0.csv 

    || Interior wall unit dead loads | data/va01/rv-dlintwall0.csv

    || Exterior wall unit dead loads | data/va01/rv-dlextwall0.csv

    || Areas | data/va01/rv-area.txt |
    area1 := 1700*SF | SM | roof area 
    area2 := 1200*SF | SM | floor area 
    ht1 := 9*FT | M | wall height   
    len1 := 110*FT | M | interior wall length 
    len2 := 155*FT | M | exterior wall length 
    ----

    || Exterior wall unit dead loads | data/va01/dlextwall0.csv |    
    vars,       value, unit1, unit2, description                  
    ld1,        2.,    PSF,   KPA,   1/2 in plywood sheathing     
    ld2,        2.,    PSF,   KPA,   2x4 studs at 16 in o.c.      
    ld3,        3.,    PSF,   KPA,   5/8 in sheet rock            
    ld4,        1.5,   PSF,   KPA,   fixtures                     
    ===,        ===,   ===,   ===,   ===                          
    extwalldl1, 8.5,   PSF,   KPA,   Total exterior wall unit load
    ---- 

    || equations | rv-aci318-05.csv |
    ACI 318-12.2 Shear Friction Capacity, KIPS, KN
    a = b*c, 2, 2
    ----

    wt1 = area1 * udl1 | KIPS, KN | 2, 2
    
    Floor weight _[e]
    wt2 = area2 * floordl1 | KIP,KN,2   
    
    Partition weight | KIP,KN,2
    wtpart1 =  htwall1 * lenwall1 * intwalldl1 |
    
    Exterior wall weight _[e]                               
    wtexwall1 = htwall1 * lenwall2 * extwalldl1 |KIP,KN|2|nosub

    Total building weight _[e]
    wttot1 = rfwt1 + flrwt1 + partwt1 + exwallwt1 |KIP,KN|2|nosub
    Weights _[t]  

    """)

# %%
rv.V("""Wind Loads | none | pass 
    
    || Wind load 1 | data/im01/fig1.png | 75 |
    || Wind load 2 | data/im01/fig2.png | 75 |
    
    """)

# %%
rv.V("""Material Densities and Seismic Models | sub

    Because the T&G roof is relatively more flexible, the effective floor load
    for seismic models is calculated as the sum of the floor and all of the
    partition weight.


    Effective model floor load  _[e]  
    eflrdl1 = (flrwt1 + partwt1)/(areaflr1)                     |PSF, KPA|2
    Effective model floor density _[e]  
    eflrdens1 = eflrdl1/(0.5*IN)                                |PCI, KNCM|2
    Effective model roof density _[e]  
    erfdens1 = roofdl1/(1.5*IN)                                 |PCI, KNCM|2
    Effective model wall density _[e]  
    ewalldens1 = extwalldl1/(0.5*IN)                            |PCI, KNCM|2
    Model loads _[t]
          
    """)
# %%
rv.I("""Abbreviations and References | default
 
    References _[cb]

    || references | data/references.txt | plain

    
    Drawings _[cb]

    || text | data/drawing_list.txt | plain

        
    Abbreviations - Terms _[cb]

    || text | data/abbrev_terms.tex | plain

    
    Abbreviations - Math _[bc]

    || text | data/abbrev_math.tex | plain
    """)

# rv.write("txt, pdf:pdf-style4.sty")
