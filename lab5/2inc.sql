select r_name, count(s_name)
from region, nation, supplier, 
(
select  r_name, count(s_name) as number
from region, nation, supplier
where r_regionkey = n_regionkey and 
n_nationkey = s_nationkey 
) As NewTable
where r_regionkey = n_regionkey and n_nationkey = s_nationkey
group by NewTable.r_name
having s_acctbal > avg(number)
