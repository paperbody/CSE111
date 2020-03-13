select o_orderpriority, count(distinct (o_orderkey))
from orders, lineitem
where (julianday(l_receiptdate) - julianday(l_commitdate)) > 0 AND
o_orderdate >= '1996-10-01' and
o_orderdate <= '1996-12-31' and
l_orderkey == o_orderkey
group by o_orderpriority
