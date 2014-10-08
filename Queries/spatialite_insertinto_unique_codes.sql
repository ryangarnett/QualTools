INSERT INTO uniq_doc_codes (docid, code, grouptype, groupid, codecnt)
SELECT docid, code, grouptype, groupid, Count(code) AS codecnt
FROM codes
GROUP BY code
ORDER BY codecnt