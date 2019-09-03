# Summary Report
**Summary Report** is a reporting tool used to extract usage summaries from the news database based on the entries in the articles, authors and log tables.

**The generated report will provide the following information**:
- most popular articles based on user visits, as sorted list, with highest on top 
- most popular article author based on user visits, as sorted list, with highest on top
- days in which the user requests error-ed with a rate higher than 1% 


### Command Line

**Use the following command to launch the program:**
`user@domain:/summary_report$ /usr/bin/python3 summary_report.py`

### Generated Report Example
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

