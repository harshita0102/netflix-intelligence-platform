import sqlite3
import pandas as pd

conn = sqlite3.connect("dataset/netflix.db")

queries = {

"Movies vs TV Shows":

"""
SELECT
type,
COUNT(*) AS Total
FROM netflix
GROUP BY type;
""",

"Top Directors":

"""
SELECT
director,
COUNT(*) AS Total
FROM netflix
WHERE director<>'Unknown'
GROUP BY director
ORDER BY Total DESC
LIMIT 10;
""",

"Ratings":

"""
SELECT
rating,
COUNT(*) AS Total
FROM netflix
GROUP BY rating
ORDER BY Total DESC;
""",

"Top Countries":

"""
SELECT
country,
COUNT(*) AS Total
FROM netflix
GROUP BY country
ORDER BY Total DESC
LIMIT 10;
"""

}

for name, query in queries.items():

    print("\n=========================")

    print(name)

    print("=========================")

    print(pd.read_sql(query, conn))

conn.close()