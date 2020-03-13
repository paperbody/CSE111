select count(distinct(s_name))
from supplier, partsupp, part
where s_suppkey = ps_suppkey and
p_partkey = ps_partkey and p_retailprice = (select min(p_retailprice) as cnt
from part, partsupp
where p_partkey = ps_partkey
);


