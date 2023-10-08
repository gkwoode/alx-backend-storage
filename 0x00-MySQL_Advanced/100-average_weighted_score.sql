DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_weighted_score DECIMAL(10, 2); -- Adjust precision and scale as needed
    DECLARE total_weight DECIMAL(10, 2); -- Adjust precision and scale as needed;

    -- Calculate the total weighted score and total weight for the user
    SELECT SUM(score * weight), SUM(weight) INTO total_weighted_score, total_weight
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the average weighted score for the user
    DECLARE avg_weighted_score DECIMAL(10, 2); -- Adjust precision and scale as needed
    IF total_weight > 0 THEN
        SET avg_weighted_score = total_weighted_score / total_weight;
    ELSE
        SET avg_weighted_score = 0;
    END IF;

    -- Update the user's average_weighted_score in the users table
    UPDATE users
    SET average_weighted_score = avg_weighted_score
    WHERE id = user_id;
END;
//
DELIMITER ;
