select count(c_name)
from customer, region, nation
where c_nationkey = n_nationkey and
 n_regionkey = r_regionkey and 
 r_name != "EUROPE" and
 r_name != "AFRICA"
