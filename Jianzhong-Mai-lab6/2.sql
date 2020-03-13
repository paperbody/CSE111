select count(cnt)
from(select count(c_custkey) as cnt
from customer, orders
where c_custkey = o_custkey and
o_orderdate like "1995-08%"
group by c_custkey
having count(o_custkey) <= 2);

