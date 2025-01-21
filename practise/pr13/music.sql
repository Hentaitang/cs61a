CREATE TABLE shm_tracks AS
  SELECT "360" AS track, "charli" AS artist UNION
  SELECT "cinderella",   "remi"             UNION
  SELECT "wildflower",   "billie";

INSERT INTO shm_tracks VALUES ("bad guy", "billie");
INSERT INTO shm_tracks VALUES ("apple", "charli");

CREATE TABLE anya_tracks AS
SELECT "apple" AS track, "charli" AS artist UNION
SELECT "taste",          "sabrina"          UNION
SELECT "wildflower",     "billie";