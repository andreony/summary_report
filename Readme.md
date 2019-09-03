## Summary Report
**Summary Report** is a reporting tool used to extract usage summaries from the news database based on the entries in the articles, authors and log tables.

### Generated Report Example

#### Command Line

`/usr/bin/python3 summary_report.py`

```
2019-09-03 03:12:04.533050

    ########################
    ** Most Popular Articles **
    ########################

        Article Name     -->    Number ov Views
--------------------------------------------------
Candidate is jerk, alleges rival  --->  338647
Bears love berries, alleges bear  --->  253801


    ########################
    ** Most Popular Author **
    ########################

        Author   -->    Number ov Views
--------------------------------------------------
Ursula La Multa  --->  507594
Rudolf von Treppenwitz  --->  423457


    ########################
    ** Request Errors **
    ########################

        Day      -->    Over 1% Errored Requests
--------------------------------------------------
2016-07-17 00:00:00+00:00  --->  2.26
--------------------------------------------------
```

### Dependencies 
The program is python3+ compatible and requires psycopg2 as DB-API

### Todos
- Add tabelar printout using prettyprinting lib
- Use Flask to create a microservice for a web based reporting tool 
