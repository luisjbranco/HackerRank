SELECT DISTINCT(CITY) FROM STATION
WHERE SUBSTR(CITY, LENGTH(CITY), LENGTH(CITY)) NOT IN ('a', 'e', 'i', 'o', 'u')