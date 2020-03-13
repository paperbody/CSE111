select c_name, count(o_orderkey)
from Q1, Q5
where c_custkey = o_custkey and c_nation = "GERMANY" and o_orderyear = "1995" 
group by c_name
