SELECT docid, code, Count(code) AS codecnt, grouptype, groupid
FROM codes
GROUP BY code, docid
ORDER BY docid