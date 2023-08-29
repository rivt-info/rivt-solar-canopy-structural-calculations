#! python
# %%
import rivt.rivttext as rv
# %%
rv.R("""-- Overview | 80 

    || pages | config | rivt-config.ini | pdf-style4.sty | 10
 
    """)
rv.I("""Minimum Wall Sheathing CRC - First Floor
 
    The residence is sheathed in exterior 1/2" 5-ply plywood nailed with 8d
    common nails at 12" oc at edges and field. The boundary nailing capacity is
    half of the maximum spacing tabulated in the building codes. The residence
    is checked against the CRC prescriptive wall opening limits, assuming 6" oc
    (which is not the case) to assess the degree of wall continuity. A CBC
    analysis is performed in calculation 0301 which estimates the DC ratios for
    the 12" oc nailing.

    || image | resource | mv_nail1a.jpg |40
    Existing shear wall nailing - 8d at 12" OC _[f]
    
    || image | resource | mv_nail2a.jpg |56
    Existing shear wall nailing - 8d - 2-1/2" penetration _[f]

    The minimum solid wall percent is given in the following CRC table.

    || table | data | r602_3wallpercent.csv | 15,c | [:]

    The percent solid wall for each shear wall is:

    || table | data | solid_shearwall.csv | 15,r | [:]

    **Therefore, if edge nailing requirements are met the residence meets the
    prescriptive opening requirements of the CRC.**

    || image | resource | shearwalls1d.jpg | 90
    First floor shear walls - north and west sides _[f]

    || image | resource | shearwalls2d.jpg | 90
    First floor shear walls - south and east sides _[f]
    
    Check required basic fastener spacing:

    || table | data | r602_3fasten.csv | 30,l | [:]
    || text | data | fasten_notes.txt | plain

    Check code required wind governed fastener spacing:

    || table | data | r602_3wind.csv | 30,c | [:]
    || text | data | wind_notes.txt | plain 
    
    **In order to meet the code prescriptive wind and seismic requirements the
    number of nails at the exterior sheathing panel boundaries need to be
    doubled - from 12" oc to 6" oc. Refer to CBC analysis in calculation 0301
    for an analysis of DC ratios with reduced capacity**

    """)
# %%
rv.I("""Foundation - CRC Requirements 

    The existing foundation on the north and west side of the residence is a
    concrete strip footing directly supporting the floor joists. On the south
    side the floor joists are supported on 2x4 framed walls varying in height,
    up to 6 feet. The framing is clad on the outside with 1x10 planks, spaced
    1" apart for ventilation.

    The foundation has two significant seismic deficiency. The first is a
    significant torsional irregularity arising from lack of shear stiffness and
    strength on the south and east walls. The existing structure has only one
    compression brace along each wall and the spaced planks do not provide
    meaningful strength or stiffness. This irregularity is a deficiency whether
    the floor diaphragm is considered semi-rigid or flexible. The second is the
    lack of adequate anchorage of the sill plates to the foundation. Existing
    anchorage typically consists of only a single 1/2" anchor bolt and small
    washer every 3 or 4 feet. 

    **The torsional irregularities disqualify the foundation structure from
    following a CRC design process.**

    """)
# %%
rv.V("""Seismic Model Inputs - CBC Requirements | sub
    
 
    Seismic demands on the residence were analyzed using a 3D FEM model. The
    model includes the full relevant geometry, loads and stiffness of the
    walls, roof, floors and foundation.

    The in-plane stiffness of the T&G roof is taken as 300 pounds/inch/inch
    using test data from [USDA1972]. The in-plane stiffness of the plywood
    shear walls and subfloor is estimated at 1000 pounds/inch/inch after
    supplementary nailing, using values from CBC tables.

    [USDA1972] USDA Forest Products Laboratory. 1972. "Shear Stiffness Of Two-Inch 
    Wood Decks For Roof Systems", U.S.D.A. Forest  Service RESEARCH  PAPER, 
    FPL 155 1972 

    || table | data | awc4_3a.csv | 11,c | [:]
    || text | data | awc4_3a_notes.txt | plain

    The shear capacity adjustments for shear wall openings is taken from the
    AWC table below:

    || table | data | awc4_335adjust.csv | 20,c | [:]
    || text | data | awc4_335adjust.txt | plain

    || table | data | gm_values.csv | 30,l | [:]

    Base shear coefficient _[t]
    SDS := 1.0               | -,- | short period design
    R1 := 6.5                | -,- | reduction factor
    omega := 3               | -,- | overstrength factor
    
    Seismic coefficent [e]_
    C_s = SDS/R1            | -,- | 2,2

    """)
# %%
rv.writedoc("utf, pdf")
