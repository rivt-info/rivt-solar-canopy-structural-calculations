#! python
# %%
import rivtlib.rivtapi as rv
# %%
rv.I("""Overview and Codes | template | nocolor

    The structural design is for a residential solar canopy located in
    Larkspur, California. It includes the design of a concrete slab and stem
    wall foundation, welded steel tube frame, and solar panel clips.

    || text | project-data.txt | plain 

    || image | data01/fig1.png | 75
    Wind load 1 _[f]

    || image | data01/fig2.png | 75 
    Wind load 2 _[f]

    Building Codes and Jurisdiction _[b]
     
    The canopy is designed using CBC-2019. 
    
    - City of Larkspur, California 
    - 2019 California Building Code [CBC]
    - 2019 California Residential Code [CRC] 
    
    Table of Project Engineering Standards _[t]
    || table | insert01/cbc2019_stds.xlsx | 53,l 
 
    
    Basic loads and load combinations for the project are from the California
    Building and Residential Codes and are shown in the following tables.

    
    Table of Load Types _[t]
    || table | insert/load_types01.csv | 40,l 
    
    
    Table of Load Combinations _[t]
    || table | data/asce7_load_comb.csv | 55,c 

    """)
# %%
rv.V("""Gravity Loads and Seismic Mass | template | nocolor
    
    Some filler text

    Roof unit dead loads _[t]
    variable,value,unit,[unit],description
    ld1,2.,PSF,KPA,Urethane foam (4 inch thick)
    ld2,1.,PSF,KPA,Three-ply roofing
    ld3,5.,PSF,KPA,Doug Fir decking 2-in.
    ld4,1.,PSF,KPA,Doug Fir beams 4x12 at 12 ft o.c.
    roofdl1,9.,PSF,KPA,Total roof unit load

    Floor unit dead loads _[t]
    || declare | data/dlfloor0.csv

    Interior wall unit dead loads _[t]
    || declare | data/dlintwall0.csv

    Exterior wall unit dead loads _[t]
    || declare | data/dlextwall0.csv

    Areas _[t]
    area1 := 1700*SF | SM, roof area 
    area2 := 1200*SF |SM| floor area
    ht1 := 9*FT |M| wall height   
    len1 := 110*FT |M| interior wall length 
    len2 := 155*FT |M| exterior wall 2 length 

    
    Roof weight _[e]                    
    wt1 = area1 * udl1 | KIP,KN,2
    
    Floor weight _[e]
    wt2 = area2 * floordl1 | KIP,KN,2   
    
    Partition weight _[e]
    wtpart1 =  htwall1 * lenwall1 * intwalldl1 |KIP,KN|2|nosub
    
    Exterior wall weight _[e]                               
    wtexwall1 = htwall1 * lenwall2 * extwalldl1 |KIP,KN|2|nosub

    Total building weight _[e]
    wttot1 = rfwt1 + flrwt1 + partwt1 + exwallwt1 |KIP,KN|2|nosub
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
