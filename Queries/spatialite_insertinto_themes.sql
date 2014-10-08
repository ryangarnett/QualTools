INSERT INTO themes (theme, themeid, themecnt)
SELECT theme, themeid, Count(grouptype) AS themecnt
FROM groups
GROUP BY theme
ORDER BY theme;