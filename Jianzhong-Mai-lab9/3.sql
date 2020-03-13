select c_nation, count(c_name)
from Q1, orders
where c_region = "EUROPE" and o_custkey = c_custkey
group by c_nation

