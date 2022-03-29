SELECT City.name
FROM City 
INNER JOIN Country
ON City.countrycode = Country.code
WHERE Country.continent = "Africa";