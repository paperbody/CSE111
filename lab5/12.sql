select sum(ps_supplycost)
from part, partsupp
where p_partkey == ps_partkey and
p_retailprice < 1000 and
p_partkey inS( select l_partkey 
from lineitem, partsupp 
where ps_suppkey = l_suppkey and
 l_shipdate >="1996-01-01" and
 l_shipdate <="1996-12-31") and 
ps_suppkey not in
( select distinct ps_suppkey 
from partsupp, lineitem, part 
where ps_partkey == p_partkey 
and p_partkey == l_partkey and 
ps_suppkey = l_suppkey and
l_extendedprice < 1000 and
l_shipdate >= "1995-01-01" and
l_shipdate <= "1995-12-31")
