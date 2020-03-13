select p_mfgr, o_orderpriority, count( p_name)
from partsupp, part, customer, supplier, nation, orders
where c_custkey = o_custkey and n_nationkey = c_nationkey and s_nationkey = c_nationkey and s_suppkey = ps_suppkey and p_partkey = ps_partkey
group by p_mfgr, o_orderpriority
