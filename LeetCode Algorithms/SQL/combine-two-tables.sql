""" https://leetcode.com/problems/combine-two-tables/ """

-- LEFT JOIN
-- İlk tablodaki tüm veriler gelir.
-- İlk tablo ile ikinci tablodaki eşleşmeyen kayıtlara NULL koyulur.
SELECT 
    P.firstName, P.lastName, A.city, A.state
FROM 
    Person AS P
LEFT JOIN 
    Address AS A
ON 
    P.personId = A.personId
