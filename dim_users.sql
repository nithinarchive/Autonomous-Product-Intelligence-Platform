CREATE TABLE IF NOT EXISTS dim_users (
    user_id INT PRIMARY KEY,
    signup_date DATE,
    country VARCHAR(50)
);
