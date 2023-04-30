DROP database covid_effects;
CREATE DATABASE covid_effects;

USE covid_effects;

CREATE TABLE IF NOT EXISTS monthly_profit(
	Month CHAR(10),
    year YEAR,
    value INT
);

CREATE TABLE IF NOT EXISTS country_profit(
    country VARCHAR(20),
    Measure VARCHAR(5),
    value INT
);

CREATE TABLE IF NOT EXISTS transport_profit(
    Transport_Mode VARCHAR(20),
    Measure VARCHAR(5),
    value INT
);

CREATE TABLE IF NOT EXISTS profit_per_day(
    Day VARCHAR(20),
    Measure VARCHAR(5),
    value INT
);

CREATE TABLE IF NOT EXISTS commodity_profit(
    Commodity VARCHAR(20),
    Measure VARCHAR(5),
    value INT
);

CREATE TABLE IF NOT EXISTS top5_months(
    date DATE,
    value INT
);

CREATE TABLE IF NOT EXISTS top5_products(
    country VARCHAR(20),
    commodity VARCHAR(10),
    value INT
);

CREATE TABLE IF NOT EXISTS best_days_per_product(
    country VARCHAR(20),
    commodity VARCHAR(10),
    value INT
);