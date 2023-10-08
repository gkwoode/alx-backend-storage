DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE total_weighted_score DECIMAL(10, 2); -- Adjust precision and scale as needed
    DECLARE total_weight DECIMAL(10, 2); -- Adjust precision and scale as needed;

    -- Declare cursor to iterate through unique user_ids
    DECLARE users_cursor CURSOR FOR
    SELECT DISTINCT user_id FROM corrections;

    -- Declare continue handler for cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN users_cursor;

    -- Start processing each user
    user_loop: LOOP
        FETCH users_cursor INTO user_id;
        IF done = 1 THEN
            LEAVE user_loop;
        END IF;

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
    END LOOP;

    CLOSE users_cursor;
END;
//
DELIMITER ;
