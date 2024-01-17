-- lists the number of records
-- ists number of records wih the sae score
SELECT score, COUNT(score) FROM second_table GROUP BY score;
