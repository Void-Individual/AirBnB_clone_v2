-- Create a database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Give all priviledges of the db to the user created
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant select priviledges for this db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
