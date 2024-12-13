#! python
# %%
import rivt.rivtapi as rv
# %%
rv.R("""Overview | 80 

    This report describes the structural design of a solar canopy covering a
    residential patio located in the City of Larkspur, California. It includes
    the design of a concrete slab and stem wall, steel tube frame, and
    attachments of solar panels to the frame. The report is divided into the
    following divisions and subdivisions::
    
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

    || pages | config | rivt-config.ini | pdf-style2.sty | 1
    || project | resource | proj-info.txt | 30,C
 
    """)
# %%
rv.I("""Governing Codes 


    || image | resource | fig1.png | 20
    Wind load 1 _[f]
    
    || image | resource | fig2.png | 45 
    Wind load 2 _[f]

    The permit approval is under the jurisdiction of the City of Larkspur,
    California which adopted the 2019 California Building Code [CBC] and the
    2019 California Residential Code [CRC] as the basis for permiting
    construction work. The canopy is designed for compliance with the
    requirements of the CBC.

    Standards _[t]
    || table | data | cbc2019_stds.xlsx | 53,l | [:]
 
    Basic loads and load combinations are derived from the California Building
    and Residential Codes.

    Load Types _[t]
    || table | data | load_types01.csv | 35,l | [:]

    Load Combinations _[t]
    || table | data | asce7_load_comb.csv | 55,c | [:]

    """)
# %%
rv.V("""Gravity Loads and Seismic Mass | sub
    
    Some filler text

    Roof unit dead loads _[t]
    || values | data | dlroof0.csv

    Floor unit dead loads _[t]
    || values | data | dlfloor0.csv

    Interior wall unit dead loads _[t]
    || values | data | dlintwall0.csv

    Exterior wall unit dead loads _[t]
    || values | data | dlextwall0.csv
    
    Areas _[t]
    arearf1 := 1700             |SF,SM| roof area 
    areaflr1 := 1200            |SF,SM| floor area
    htwall1 := 9                |FT, M| wall height   
    lenwall1 := 110             |FT, M| interior wall length 
    lenwall2 := 155             |FT, M| exterior wall length 2

    
  
    Roof weight _[e]                    
    rfwt1 = arearf1 * roofdl1                           |KIP,KN|2,2
    Floor weight _[e]
    flrwt1 = areaflr1 * floordl1                        |KIP,KN|2,2   
    Partition weight _[e]
    partwt1 =  htwall1 * lenwall1 * intwalldl1          |KIP,KN|2,2
    Exterior wall weight _[e]                               
    exwallwt1 = htwall1 * lenwall2 * extwalldl1         |KIP,KN|2,2
    Total building weight _[e]
    totwt1 = rfwt1 + flrwt1 + partwt1 + exwallwt1       |KIP,KN|2,2
    Weights _[t]  

      
    """)
# %%
rv.V("""Material Densities and Seismic Models | sub

    Because the T&G roof is relatively more flexible, the effective floor load
    for seismic models is calculated as the sum of the floor and all of the
    partition weight.


    Effective model floor load  _[e]  
    eflrdl1 = (flrwt1 + partwt1)/(areaflr1)                     |PSF, KPA|2,2
    Effective model floor density _[e]  
    eflrdens1 = eflrdl1/(0.5*IN)                                |PCI, KNCM|2,2
    Effective model roof density _[e]  
    erfdens1 = roofdl1/(1.5*IN)                                 |PCI, KNCM|2,2
    Effective model wall density _[e]  
    ewalldens1 = extwalldl1/(0.5*IN)                            |PCI, KNCM|2,2
    Model loads _[t]
   
    
    """)
# %%
rv.I("""Abbreviations and References
 
    References _[c]
    || text | data | references.txt | literal | noshade
    """)

rv.I("""--Drawing List 
    _[page]

    Drawings _[c]
    || text | data | drawing_list.txt | literal | noshade
    """)

rv.I("""--Abbreviations
     _[page]

    Abbreviations - Terms _[c]
    || text | data | abbrev_terms.tex | raw | noshade

    _[page]
    Abbreviations - Math _[c]
    || text | data | abbrev_math.tex | raw | noshade
    """)

rv.writedoc("utf, pdf")
