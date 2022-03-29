SELECT Country.continent as Continents, ROUND(AVG(City.population)-0.5) as average_population
FROM Country
INNER JOIN City 
ON Country.code = City.countrycode
GROUP BY Country.continent
ORDER BY average_population;