select max(l_discount)
from lineitem, orders
where l_orderkey = o_orderkey and 
o_orderdate like "1995-05-__" and
l_discount <( 
select avg(l_discount)
from lineitem
)


