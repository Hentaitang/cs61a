CREATE TABLE ingredients AS
  SELECT "chili" AS dish, "beans" AS part UNION
  SELECT "chili" , "onions" UNION
  SELECT "soup" , "broth" UNION
  SELECT "soup" , "onions" UNION
  SELECT "beans" , "beans";

CREATE TABLE shops AS
  SELECT "beans" AS food, "A" AS shop, 2 AS price UNION
  SELECT "beans" , "B" , 2 AS price UNION
  SELECT "onions" , "A" , 3 UNION
  SELECT "onions" , "B" , 2 UNION
  SELECT "broth" , "A" , 3 UNION
  SELECT "broth" , "B" , 5;

SELECT food, MIN(price) FROM shops group by food;

SELECT dish, SUM(price) FROM ingredients, shops
  WHERE shop="A" and part=food group by dish;

SELECT a.food FROM shops as a, shops as b
  WHERE a.food = b.food and a.price > b.price;

SELECT food FROM shops GROUP BY food having MAX(price) > MIN(price);