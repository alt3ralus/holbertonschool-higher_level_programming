-- advance
SELECT city, AVG(value) AS avg_temp FROM temperatures.sql GROUP BY city ORDER BY avg_temp DESC;

