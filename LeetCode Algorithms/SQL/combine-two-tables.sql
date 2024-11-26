""" https://leetcode.com/problems/combine-two-tables/ """

-- LEFT JOIN
-- İlk tablodaki tüm veriler gelir.
-- İkinci tabloda ilk tablo ile ilgili kayıt yoksa NULL koyulur, kayıt varsa o değer koyulur.

SELECT 
    P.firstName, P.lastName, A.city, A.state
FROM 
    Person AS P
LEFT JOIN 
    Address AS A
ON 
    P.personId = A.personId
