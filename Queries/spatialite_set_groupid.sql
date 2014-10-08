UPDATE codes SET groupid = CASE 
WHEN grouptype = 'Access' THEN 1001
WHEN grouptype = 'Active' THEN 1002
WHEN grouptype = 'Air Quality' THEN 1003
WHEN grouptype = 'Alternative Energy' THEN 1004
WHEN grouptype = 'Automobile' THEN 1005
WHEN grouptype = 'Climate Change' THEN 1006
WHEN grouptype = 'Comfort' THEN 1007
WHEN grouptype = 'Community' THEN 1008
WHEN grouptype = 'Conservation' THEN 1009
WHEN grouptype = 'Design' THEN 1010
WHEN grouptype = 'Expenditures' THEN 1011
WHEN grouptype = 'Facilities' THEN 1012
WHEN grouptype = 'Health' THEN 1013
WHEN grouptype = 'Heavy Truck' THEN 1014
WHEN grouptype = 'Mass Transit' THEN 1015
WHEN grouptype = 'Nature' THEN 1016
WHEN grouptype = 'Pollution' THEN 1017
WHEN grouptype = 'Product Flow' THEN 1018
WHEN grouptype = 'Revenue' THEN 1019
WHEN grouptype = 'Safety' THEN 1020
WHEN grouptype = 'Stresses' THEN 1021
WHEN grouptype = 'Sustainable' THEN 1022
WHEN grouptype = 'Technology' THEN 1023
WHEN grouptype = 'Visually Pleasing' THEN 1024
ELSE 9999
END