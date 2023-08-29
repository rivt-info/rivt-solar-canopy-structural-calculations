#! python
# %%
import rivt.rivtapi as rv
# %%
rv.I("""Load Combinations | default
 
    Basic loads and load combinations are derived from the California Building
    and Residential Codes.

    || table | load_types01.csv | 30,L | [:]

    || table | asce7_load_comb.csv | 55,C | [:]

    [page]_
    
    """)
# %%
rv.V("""Gravity Loads and Seismic Mass | nosub
 
    Roof unit dead loads [t]_
    || declare | r0102 | dlroof0.csv

    Floor unit dead loads [t]_
    || value | r0102 | dlfloor0.csv

    Interior wall unit dead loads [t]_
    || value | r0102 | dlintwall0.csv

    Exterior wall unit dead loads [t]_
    || value | r0102| dlextwall0.csv
    
    Areas [t]_
    arearf1 = 1700             | SF, SM | roof area 
    areaflr1 = 1200            | SF, SM | floor area
    htwall1 = 9                | FT, M  | wall height   
    lenwall1 = 110             | FT, M  | interior wall length 
    lenwall2 = 155             | FT, M  | exterior wall 2 length

    Roof weight [e]_                    
    rfwt1 = arearf1 * roofdl1                           |LBF, KN|2

    Floor weight [e]_
    flrwt1 = areaflr1 * floordl1                        |LBF, KN|2   

    Partition weight [e]_
    partwt1 =  htwall1 * lenwall1 * intwalldl1          |LBF, KN|2

    Exterior wall weight [e]_                               
    exwallwt1 = htwall1 * lenwall2 * extwalldl1         |LBF, KN|2

    Total building weight [e]_
    totwt1 = rfwt1 + flrwt1 + partwt1 + exwallwt1       |LBF, KN|2
    
    """)
# %%
rv.V("""Material Densities - Seismic Models | nosub

    Because the T&G roof is relatively more flexible, the effective floor load
    for seismic models is calculated as the sum of the floor and all of the
    partition weight.

    Floor load including partitions [e]_  
    eflrdl1 = (flrwt1 + partwt1)/(areaflr1)             |PSF, KPA|2

    Effective floor, roof and wall densities [e]_  
    eflrdens1 = eflrdl1/(0.5*IN)                        |PCI, KNCM|2

    erfdens1 = roofdl1/(1.5*IN)                         |PCI, KNCM|2

    ewalldens1 = extwalldl1/(0.5*IN)                    |PCI, KNCM|2
    
    """)
