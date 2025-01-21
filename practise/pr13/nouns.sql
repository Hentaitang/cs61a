CREATE TABLE nouns AS
  SELECT "dog" as phrase UNION
  SELECT "cat"           UNION
  SELECT "bird";

SELECT subject.phrase || " chase " || object.phrase
  from nouns as subject, nouns as object
  where subject.phrase != object.phrase;