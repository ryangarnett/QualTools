INSERT INTO groups (grouptype, groupid, groupcnt)
SELECT grouptype, groupid, Count(grouptype) AS groupcnt
FROM codes
GROUP BY grouptype
ORDER BY grouptype;