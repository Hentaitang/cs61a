CREATE TABLE cities AS
  SELECT 38 as latitude, 122 as longitude, "Berkeley" as name UNION
  SELECT 45,             93,               "Minneapolis"      UNION
  SELECT 42,             71,               "Cambridge"        UNION
  SELECT 33,             117,              "San Diego"        UNION
  SELECT 34,             118,              "Los Angeles"      UNION
  SELECT 26,             80,               "Miami"            UNION
  SELECT 40,             105,              "Denver";

CREATE TABLE cold AS
  SELECT name FROM cities WHERE latitude >= 43;

CREATE TABLE distances AS
  SELECT a.name as first, b.name as second,
    60 * (b.latitude - a.latitude) as distance
    from cities as a, cities as b;