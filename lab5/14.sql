SELECT r2.r_name, r1.r_name, substr(l_shipdate,1,4), SUM(l_extendedprice * (1 - l_discount))
FROM region r1, region r2, lineitem, customer, nation n1, nation n2, supplier, orders
WHERE
l_orderkey = o_orderkey and
o_custkey = c_custkey and
l_suppkey = s_suppkey and
c_nationkey = n1.n_nationkey and 
s_nationkey = n2.n_nationkey and
n1.n_regionkey = r1.r_regionkey and 
n2.n_regionkey = r2.r_regionkey and
l_shipdate >= "1995-01-01" and
l_shipdate <= "1996-12-31"
group by r2.r_name, r1.r_name, substr(l_shipdate,1,4)
