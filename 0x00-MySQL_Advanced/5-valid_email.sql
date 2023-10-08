DELIMITER //
CREATE TRIGGER reset_valid_email_on_email_change
BEFORE UPDATE ON users FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0; -- Reset valid_email to 0 when email changes
    END IF;
END;
//
DELIMITER ;
