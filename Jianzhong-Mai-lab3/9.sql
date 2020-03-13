SELECT  n_name,COUNT(s_suppkey), AVG(s_acctbal)
FROM supplier,nation
WHERE n_nationkey = s_nationkey
GROUP BY n_name
HAVING 5 <= COUNT(s_suppkey);

