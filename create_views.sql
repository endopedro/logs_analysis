CREATE VIEW clicks AS
    SELECT DATE(time) as date, count(DATE(time)) as ok
        FROM log
        GROUP BY date
        ORDER BY date;

CREATE VIEW errors AS
    SELECT DATE(time) as date, count(DATE(time)) as not_found
    FROM log WHERE status = '404 NOT FOUND'
    GROUP BY date
    ORDER BY date;

CREATE VIEW daily_error AS
    SELECT clicks.date, round((100.0*errors.not_found)/clicks.ok,2) AS percentage
    FROM clicks, errors
    WHERE errors.date = clicks.date;
