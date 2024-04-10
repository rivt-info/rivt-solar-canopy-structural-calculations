#! python
# %%
import rivtlib.rivtapi as rv
rv.R("""Overview and Codes | notoc | 1

    This report provides a structural design for a residential solar canopy
    located in Larkspur, California. It includes the design of a concrete slab
    and stem wall foundation, welded steel tube frame, and solar panel clips.

    || text | project-data.txt | plain 

    """)
# %%
rv.I("""Governing Codes | default

    || image | data01/fig1.png | 75
    Wind load 1 _[f]

    
    || image | data01/fig2.png | 75 
    Wind load 2 _[f]

    
    Building Codes and Jurisdiction _[b]
     
    - City of Larkspur, California 
    - 2019 California Building Code [CBC]
    - 2019 California Residential Code [CRC] 
    
    The canopy is designed for compliance with the CBC.

    
    Table of Project Engineering Standards _[t]
    || table | data0101/cbc2019_stds.xlsx | 53,l 
 
    
    Basic loads and load combinations for the project are from the California
    Building and Residential Codes and are shown in the following tables.

    
    Table of Load Types _[t]
    || table | data/load_types01.csv | 40,l 
    
    
    Table of Load Combinations _[t]
    || table | data/asce7_load_comb.csv | 55,c 

    """)
# %%
rv.V("""Gravity Loads and Seismic Mass | sub
    
    Some filler text

    Roof unit dead loads _[t]
    || declare | data/dlroof0.csv

    Floor unit dead loads _[t]
    || declare | data/dlfloor0.csv

    Interior wall unit dead loads _[t]
    || declare | data/dlintwall0.csv

    Exterior wall unit dead loads _[t]
    || declare | data/dlextwall0.csv

    Areas _[t]
    arearf1 := 1700*SF           |SM| roof area 
    areaflr1 := 1200*SF          |SM| floor area
    htwall1 := 9*FT              |M| wall height   
    lenwall1 := 110*FT           |M| interior wall length 
    lenwall2 := 155*FT           |M| exterior wall 2 length 

    
    Roof weight _[e]                    
    rfwt1 = arearf1 * roofdl1                           |KIP,KN|2
    Floor weight _[e]
    flrwt1 = areaflr1 * floordl1                        |KIP,KN|2   
    Partition weight _[e]
    partwt1 =  htwall1 * lenwall1 * intwalldl1          |KIP,KN|2
    Exterior wall weight _[e]                               
    exwallwt1 = htwall1 * lenwall2 * extwalldl1         |KIP,KN|2
    Total building weight _[e]
    totwt1 = rfwt1 + flrwt1 + partwt1 + exwallwt1       |KIP,KN|2
    Weights _[t]  

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

    || text | data/references.txt | plain

    
    Drawings _[cb]

    || text | data/drawing_list.txt | plain

        
    Abbreviations - Terms _[cb]

    || text | data/abbrev_terms.tex | plain

    
    Abbreviations - Math _[bc]

    || text | data/abbrev_math.tex | plain
    """)

# rv.writedoc("md, pdf:pdf-style4.sty")
# rv.writedoc("md")
