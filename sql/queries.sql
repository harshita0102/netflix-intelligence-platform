-- ===================================
-- Total Titles
-- ===================================

SELECT COUNT(*)
FROM netflix;

-- ===================================
-- Movies vs TV Shows
-- ===================================

SELECT
type,
COUNT(*)
FROM netflix
GROUP BY type;

-- ===================================
-- Top 10 Countries
-- ===================================

SELECT
country,
COUNT(*) AS Total
FROM netflix
GROUP BY country
ORDER BY Total DESC
LIMIT 10;

-- ===================================
-- Top Ratings
-- ===================================

SELECT
rating,
COUNT(*)
FROM netflix
GROUP BY rating
ORDER BY COUNT(*) DESC;

-- ===================================
-- Top Directors
-- ===================================

SELECT
director,
COUNT(*)
FROM netflix
WHERE director<>'Unknown'
GROUP BY director
ORDER BY COUNT(*) DESC
LIMIT 10;

-- ===================================
-- Latest Releases
-- ===================================

SELECT
title,
release_year
FROM netflix
ORDER BY release_year DESC
LIMIT 20;

-- ===================================
-- Oldest Releases
-- ===================================

SELECT
title,
release_year
FROM netflix
ORDER BY release_year
LIMIT 20;

-- ===================================
-- Average Release Year
-- ===================================

SELECT
AVG(release_year)
FROM netflix;

-- ===================================
-- Movies Longer Than 150 Minutes
-- ===================================

SELECT
title,
duration
FROM netflix
WHERE
type='Movie'
AND
"Movie Duration">150;

-- ===================================
-- TV Shows With More Than 5 Seasons
-- ===================================

SELECT
title,
"TV Seasons"
FROM netflix
WHERE
type='TV Show'
AND
"TV Seasons">5;

-- ===================================
-- Titles Added After 2020
-- ===================================

SELECT
title,
"Year Added"
FROM netflix
WHERE
"Year Added">2020;

-- ===================================
-- Content From India
-- ===================================

SELECT
title,
type
FROM netflix
WHERE
country LIKE '%India%';

-- ===================================
-- Content From United States
-- ===================================

SELECT
title,
type
FROM netflix
WHERE
country LIKE '%United States%';

-- ===================================
-- Movies Only
-- ===================================

SELECT *
FROM netflix
WHERE type='Movie';

-- ===================================
-- TV Shows Only
-- ===================================

SELECT *
FROM netflix
WHERE type='TV Show';