SELECT Name FROM Students
WHERE Marks > 75
ORDER BY SUBSTR(Name, -3, Length(Name)) asc, Id asc