DELIMITER //
CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders FOR EACH ROW
BEGIN
    -- Decrease the quantity in the items table
    UPDATE items
    SET quantity = quantity - NEW.quantity_ordered
    WHERE item_id = NEW.item_id;
END;
//
DELIMITER ;
