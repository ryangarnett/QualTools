UPDATE codes
SET grouptype = 
( SELECT uniq_doc_codes.grouptype
	FROM uniq_doc_codes
WHERE uniq_doc_codes.code = codes.code)