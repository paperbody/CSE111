select o_orderpriority, count(o_orderkey)
from orders, lineitem
where o_orderkey = l_orderkey and
o_orderdate >= "1996-01-01" and
o_orderdate <= "1996-12-31" and
(julianday(l_commitdate)-julianday(l_receiptdate)) > 0
group by o_orderpriority
