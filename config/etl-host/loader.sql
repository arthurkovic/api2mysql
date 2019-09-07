set sql_mode=PIPES_AS_CONCAT;

INSERT INTO sample.edw_data(ID,FIRSTNAME, LASTNAME, EMAIL)
SELECT json_data.*
FROM sample.stage_data,
     JSON_TABLE(doc, '$.content[*]' COLUMNS (
         id VARCHAR(100) PATH '$.id',
         firstname VARCHAR(40)  PATH '$.firstname',
         lastname VARCHAR(100) PATH '$.lastname',
         email VARCHAR(100) PATH '$.email'
         )
         ) json_data
left join edw_data x on x.id = json_data.id COLLATE utf8mb4_unicode_ci
where x.id is null
or    MD5(TRIM(x.FIRSTNAME || ';'|| x.LASTNAME ||';' || x.EMAIL))
   <> MD5(TRIM(json_data.FIRSTNAME || ';'|| json_data.LASTNAME ||';' || json_data.EMAIL));