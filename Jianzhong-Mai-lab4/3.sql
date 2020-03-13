select n_name, count(c_name)
from nation, region, customer, orders
where n_regionkey = r_regionkey and  c_nationkey = n_nationkey and r_name = "EUROPE" and o_custkey = c_custkey
group by n_name
