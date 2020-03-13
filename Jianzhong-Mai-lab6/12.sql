select n_name
from (select n_name, max(newtotal) 
from(select n_name, sum(o_totalprice) as newtotal
from  customer, orders, nation,
where o_custkey = c_custkey and
n_nationkey = c_nationkey
group by n_name)
);
