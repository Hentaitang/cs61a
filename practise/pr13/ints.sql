CREATE TABLE ints AS
  SELECT "zero" as word, 0 as one, 0 as two, 0 as four, 0 as eight UNION
  SELECT "one"         , 1         , 0         , 0         , 0     UNION
  SELECT "two"         , 0         , 2         , 0         , 0     UNION
  SELECT "three"       , 1         , 2         , 0         , 0     UNION
  SELECT "four"        , 0         , 0         , 4         , 0     UNION
  SELECT "five"        , 1         , 0         , 4         , 0     UNION
  SELECT "six"         , 0         , 2         , 4         , 0     UNION
  SELECT "seven"       , 1         , 2         , 4         , 0     UNION
  SELECT "eight"       , 0         , 0         , 0         , 8     UNION
  SELECT "nine"        , 1         , 0         , 0         , 8;