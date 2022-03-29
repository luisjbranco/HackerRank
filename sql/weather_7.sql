SELECT DISTINCT(CITY) FROM STATION 
WHERE  lower(substr(city,length(city),length(city))) in ('a','e','i','o','u')