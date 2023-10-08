-- Check if the table already exists before creating it
IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'users') THEN
    -- Create the 'users' table
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255),
        country VARCHAR(255) NOT NULL DEFAULT 'US'
    );

    -- Add a check constraint to enforce the allowed values for the 'country' column
    ALTER TABLE users
    ADD CONSTRAINT check_country
    CHECK (country IN ('US', 'CO', 'TN'));
END IF;
