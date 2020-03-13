SELECT s_name, s_acctbal
FROM region, supplier, nation
WHERE r_regionkey = n_regionkey AND s_nationkey = n_nationkey AND r_name = "ASIA" AND s_acctbal >= 1000 ;

