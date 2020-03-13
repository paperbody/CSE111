select distinct(p_mfgr)
from partsupp, supplier, (
select p_mfgr, min(ps_availqty) 
from partsupp, supplier, part
where s_name = 'Supplier#000000053' and
 s_suppkey = ps_suppkey and
 ps_partkey = p_partkey
 ) as hi
where p_mfgr = hi.p_mfgr
