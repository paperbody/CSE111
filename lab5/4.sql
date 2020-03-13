select n_name, count(distinct(c_name)), count(distinct(s_name))
from nation, region, customer, supplier 
where n_regionkey = r_regionkey and
n_nationkey = c_nationkey and
s_nationkey = n_nationkey and
r_name = "EUROPE" 
group by n_name
