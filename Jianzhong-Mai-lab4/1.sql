select c_name,sum(o_totalprice), n_name
from orders, customer, nation, region
where c_custkey = o_custkey and n_nationkey = c_nationkey and r_regionkey = n_regionkey and n_name = "FRANCE"
group by c_name

