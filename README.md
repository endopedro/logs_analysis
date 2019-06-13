# Log Analysis

This project prints reports (in plain format) based on the data in a **Postgres** database using the package **psycopg2**.

## Requisites
- [Python 2.7](https://www.python.org/downloads)
- [VirtualBox](https://www.virtualbox.org/)
- [Vagrant](https://www.vagrantup.com/)

## Instructions

- In a **Terminal**, **Shell** or **Command Prompt**, go to **Vagrant** directory.
- Use the command `vagrant up` to start the virtual machine.
- Then, use `vagrant ssh` and import the database using the command ` psql -d news -f newsdata.sql`  
- Navigate to where the project folder is.
- Compile the **python** file `python news.py` and press **enter**.
- The program will run in the **Terminal** or **Prompt**.

## Views
This project use some **views** that you should create in the **postgres** database.

You can create these **views** automatically from the **sql file** using the command `psql -d news -f create_views.sql`.

##### clicks

```
CREATE VIEW clicks AS
    SELECT DATE(time) as date, count(DATE(time)) as ok
        FROM log
        GROUP BY date
        ORDER BY date;
```

##### errors
```
CREATE VIEW errors AS
    SELECT DATE(time) as date, count(DATE(time)) as not_found
    FROM log WHERE status = '404 NOT FOUND'
    GROUP BY date
    ORDER BY date;
```

##### daily_error
```
CREATE VIEW daily_error AS
    SELECT clicks.date, round((100.0*errors.not_found)/clicks.ok,2) AS percentage
    FROM clicks, errors
    WHERE errors.date = clicks.date;
```
