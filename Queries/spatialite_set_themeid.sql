UPDATE groups SET themeid = CASE 
WHEN grouptype = 'Access' THEN 2002
WHEN grouptype = 'Active' THEN 2004
WHEN grouptype = 'Air Quality' THEN 2003
WHEN grouptype = 'Alternative Energy' THEN 2003
WHEN grouptype = 'Automobile' THEN 2004
WHEN grouptype = 'Climate Change' THEN 2003
WHEN grouptype = 'Comfort' THEN 2002
WHEN grouptype = 'Community' THEN 2002
WHEN grouptype = 'Conservation' THEN 2003
WHEN grouptype = 'Design' THEN 2001
WHEN grouptype = 'Expenditures' THEN 2001
WHEN grouptype = 'Facilities' THEN 2004
WHEN grouptype = 'Health' THEN 2002
WHEN grouptype = 'Heavy Truck' THEN 2004
WHEN grouptype = 'Mass Transit' THEN 2004
WHEN grouptype = 'Nature' THEN 2003
WHEN grouptype = 'Pollution' THEN 2003
WHEN grouptype = 'Product Flow' THEN 2001
WHEN grouptype = 'Revenue' THEN 2001
WHEN grouptype = 'Safety' THEN 2002
WHEN grouptype = 'Stresses' THEN 2002
WHEN grouptype = 'Sustainable' THEN 2003
WHEN grouptype = 'Technology' THEN 2001
WHEN grouptype = 'Visually Pleasing' THEN 2002
ELSE 9999
END