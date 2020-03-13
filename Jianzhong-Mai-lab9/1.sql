select c_name,sum(o_totalprice), c_nation
from orders, Q1
where c_custkey = o_custkey and c_nation = "FRANCE"
group by c_name

