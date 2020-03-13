select c_name, count(o_orderkey)
from customer, nation, orders
where c_custkey = o_custkey and n_nationkey = c_nationkey and n_name = "GERMANY" and o_orderdate <= "1995-12-31" and  o_orderdate>="1995-01-01"
group by c_name