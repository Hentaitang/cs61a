CREATE TABLE pizzas AS
  SELECT "Artichoke" AS name, 12 AS open, 15 AS close UNION
  SELECT "La Val's"         , 11        , 22          UNION
  SELECT "Sliver"           , 11        , 20          UNION
  SELECT "Cheeseboard"      , 16        , 23          UNION
  SELECT "Emilia's"         , 13        , 18;

CREATE TABLE meals AS
  SELECT "breakfast" AS meal, 11 AS time UNION
  SELECT "lunch"            , 13         UNION
  SELECT "dinner"           , 19         UNION
  SELECT "snack"            , 22;

-- Pizza places that open before 1pm in alphabetical order
CREATE TABLE opening AS
  SELECT name
  FROM pizzas
  WHERE open<13 and close>=13
  ORDER BY name DESC;

CREATE TABLE study AS
  SELECT name, MAX(14 - open, 0) as duration
  FROM pizzas
  ORDER BY duration DESC;

CREATE TABLE late AS
  SELECT name || " closes at " || close  as status
  FROM pizzas, meals
  WHERE meal="snack" AND close>=time;

CREATE TABLE double AS
  SELECT a.meal AS first, b.meal AS second, name
  FROM meals AS a, meals AS b, pizzas
  WHERE b.time-a.time>6 AND a.time>=open AND b.time<=close;