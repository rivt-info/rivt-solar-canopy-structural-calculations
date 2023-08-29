0101 | 2023-06-19 | 04:38AM


## Overview and Codes

This report covers the structural design of a residential solar canopy located
in Larkspur, California. It includes the design of a concrete slab and stem
wall foundation, a welded steel tube frame, and solar panel clips.

...for project data see PDF output...

### [ 1 ]  Governing Codes
------------
<br>

<p align="center">
    <img src=data/fig2.png width=50% alt=data/fig1.png><br>
    <h4 align="center"><b>Fig. 1 - Wind load A</b></h4>
</p>


<p align="center">
    <img src=data/fig2.png width=50% alt=data/fig2.png><br>
    <h4 align="center"><b>Fig. 2 - Wind load B</b></h4>
</p>


**Building Codes and Jurisdiction**
- City of Larkspur, California
- 2019 California Building Code [CBC]
- 2019 California Residential Code [CRC]

The canopy is designed for compliance with the requirements of the CBC including the standards in the table below.        


**Table 1 - Building Standards**
<table>
<thead>
<tr><th>Category                                           </th><th>Standard  </th><th style="text-align: right;">  Year</th></tr>
</thead>
<tbody>
<tr><td>Loading                                            </td><td>ASCE-7    </td><td style="text-align: right;">  2016</td></tr>
<tr><td>Concrete                                           </td><td>ACI-318   </td><td style="text-align: right;">  2014</td></tr>
<tr><td>Wood-National Design Specifications                </td><td>AWC-NDS   </td><td style="text-align: right;">  2018</td></tr>
<tr><td>Wood-Special Design Provisions for Wind and Seismic</td><td>AWC-SDPWS </td><td style="text-align: right;">  2015</td></tr>
<tr><td>Wood Frame Construction Manual                     </td><td>AWC-WFCM  </td><td style="text-align: right;">  2018</td></tr>
</tbody>
</table>


Basic loads and load combinations are from the California Building and
Residential Codes summarized in the tables below.


[1] Table 02 - Notation and Loads
<table>
<thead>
<tr><th>Sym  </th><th>Load Effect              </th><th>Notes
            </th></tr>
</thead>
<tbody>
<tr><td>D    </td><td>Dead load                </td><td>See IBC 1606 and Chapter 3 of this
publication                                    </td></tr>
<tr><td>E    </td><td>Combined effect of horizontal and
vertical earthquake-induced forces as
defined in ASCE/SEI 12.4.2                          </td><td>See IBC 1613, ASCE/SEI 12.4.2 and
Chapter 6 of this publication                                    </td></tr>    
<tr><td>Em   </td><td>Maximum seismic load effect of
horizontal and vertical forces as set
forth in ASCE/SEI 12.4.3                          </td><td>See IBC 1613, ASCE/SEI 12.4.3 and
Chapter 6 of this publication                                    </td></tr>    
<tr><td>H    </td><td>Load due to lateral earth pressures,
ground water pressure or pressure of
bulk materials                          </td><td>See IBC 1610 for soil lateral 
loads</td></tr>
<tr><td>L    </td><td>Live load, except roof live load,
including any permitted live load
reduction                          </td><td>See IBC 1607 and Chapter 3 of this 
publication                                    </td></tr>
<tr><td>Li   </td><td>Roof live load including any permitted
live load reduction                          </td><td>See IBC 1607 and Chapter 
3 of this
publication                                    </td></tr>
<tr><td>R    </td><td>Rain load                </td><td>See IBC 1611 and Chapter 3 of this
publication                                    </td></tr>
<tr><td>W    </td><td>Load due to wind pressure</td><td>See IBC 1609 and Chapter 5 of this
publication                                    </td></tr>
</tbody>
</table>


[1] Table 03 - Table of Load Combinations
<table>
<thead>
<tr><th style="text-align: center;"> CBC 2019 reference </th><th style="text-align: center;">                      Equation                       </th></tr>  
</thead>
<tbody>
<tr><td style="text-align: center;">   Equation 16-1    </td><td style="text-align: center;">                      1.4(D +F)                      </td></tr>  
<tr><td style="text-align: center;">   Equation 16-2    </td><td style="text-align: center;">           1.2(D + F) + l.6(L + H) + 0.5(L           </td></tr>  
<tr><td style="text-align: center;">   Equation 16-3    </td><td style="text-align: center;">1.2(D + F) + l.6(Lr or S or R) + l.6H + (f1L or 0.5W)</td></tr>  
<tr><td style="text-align: center;">   Equation 16-4    </td><td style="text-align: center;">  1.2(D + F) + 1.0W + f1L +1.6H + 0.5(Lr or S or R)  </td></tr>  
<tr><td style="text-align: center;">   Equation 16-5    </td><td style="text-align: center;">        1.2(D + F) + 1.0E + f1L + l.6H + f2S         </td></tr>  
<tr><td style="text-align: center;">   Equation 16-6    </td><td style="text-align: center;">                  0.9D+ l.0W+ l.6H                   </td></tr>  
<tr><td style="text-align: center;">   Equation 16-7    </td><td style="text-align: center;">               0.9(D + F) + 1.0E+ l.6H               </td></tr>  
</tbody>
</table>



### 0101-[2] Gravity Loads and Seismic Mass


Some filler text
