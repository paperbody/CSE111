select r_name, count( distinct(c_custkey))
from customer, orders, region, nation
where c_nationkey == n_nationkey and
n_regionkey == r_regionkey and 
not exists 
(select c_name
 FROM orders
 where o_custkey = c_custkey) and
c_acctbal > (select AVG(c_acctbal) from customer)
group by r_name
