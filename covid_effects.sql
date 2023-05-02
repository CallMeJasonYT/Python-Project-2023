DROP database covid_effects;
CREATE DATABASE covid_effects;

USE covid_effects;

CREATE TABLE IF NOT EXISTS monthly_profit(
	Month CHAR(10),
    Year YEAR,
    Value INT
);

CREATE TABLE IF NOT EXISTS country_profit(
    Country VARCHAR(20),
    Measure VARCHAR(5),
    Value INT
);

CREATE TABLE IF NOT EXISTS transport_profit(
    Transport_Mode VARCHAR(20),
    Measure VARCHAR(5),
    Value INT
);

CREATE TABLE IF NOT EXISTS profit_per_day(
    Day VARCHAR(20),
    Measure VARCHAR(5),
    Value INT
);

CREATE TABLE IF NOT EXISTS commodity_profit(
    Commodity VARCHAR(20),
    Measure VARCHAR(5),
    Value INT
);

CREATE TABLE IF NOT EXISTS top5_months(
    date DATE,
    Value INT
);

CREATE TABLE IF NOT EXISTS top5_products(
    Country VARCHAR(20),
    Commodity VARCHAR(10),
    Value INT
);

CREATE TABLE IF NOT EXISTS best_days_per_product(
    Country VARCHAR(20),
    Commodity VARCHAR(10),
    Value INT
);