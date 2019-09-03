#!/usr/bin/python3

'''
    The program will output a summary report based on user activity
    For more information refer to the readme.md documentation
'''

__author__ = "Alexandru Cristian Andrei"
__copyright__ = '''
    Copyright 2019,
    Udacity Full Stack Developer NanoDegree Project
'''
__version__ = "1.0.1"
__email__ = "aa459n@att.com"
__status__ = "Production"

import psycopg2
from psycopg2 import extras
from datetime import datetime


def connect_exec_and_return(query):
    conn = psycopg2.connect("dbname=news")
    try:
        cursor = conn.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor
        )
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        raise e
    finally:
        conn.close()


def header(header_string):
    print('''
    ########################
    {H}
    ########################
    '''.format(H=header_string))


def main():
    # -- get most popular articles
    q_pop_art = ''' SELECT "title", COUNT(*) AS "nr_of_views"
        FROM log a LEFT JOIN articles b
            ON ('/article/' || b."slug") LIKE a."path"
        WHERE "path" != '/'
        AND b."title" IS NOT NULL
        GROUP BY 1
        ORDER BY 2 DESC'''
    most_popular_articles = connect_exec_and_return(q_pop_art)
    # -- get most popular authors
    q_pop_auth = '''SELECT c."name", COUNT(*) AS "nr_of_views"
        FROM
            log a LEFT JOIN articles b
                ON ('/article/' || b."slug") LIKE a."path"
        INNER JOIN authors c
                ON b."author" = c."id"
        WHERE "path" != '/'
        GROUP BY 1
        ORDER BY 2 DESC'''
    most_popular_author = connect_exec_and_return(q_pop_auth)
    # -- get the days with over 1% errors on requests
    errors_by_day = connect_exec_and_return('''
        SELECT date_trunc('day', "time") as "day",
        ROUND(AVG(CASE
                WHEN "status" != '200 OK'
                    THEN 1.0
                    ELSE 0.0
                END
        )* 100, 2)AS "not_ok_proc"
        FROM log
        GROUP BY 1
        /*HAVING "not_ok_proc" > 1.0 #>>> does not work <<! */
        HAVING ROUND(AVG(CASE
                WHEN "status" != '200 OK'
                    THEN 1.0
                    ELSE 0.0
                END
        )* 100, 2) > 1.0
    ORDER BY 1''')
    # -- print timestamp
    print("\033[7m{0}\033[0m".format(datetime.now()))
    #
    # --- print the most popular articles
    #
    header('** Most Popular Articles **')
    print("\tArticle Name", "\t --> \tNumber ov Views")
    print(50 * '-')
    for i in range(len(most_popular_articles)):
        print(
            most_popular_articles[i]['title'],
            ' ---> ',
            most_popular_articles[i]['nr_of_views']
        )
    print(50 * "-", "\n")
    #
    # --- print the most popular author
    #
    header('** Most Popular Author **')
    print("\tAuthor", "\t --> \tNumber ov Views")
    print(50 * '-')
    for i in range(len(most_popular_author)):
        print(
            most_popular_author[i]['name'],
            ' ---> ',
            most_popular_author[i]['nr_of_views']
        )
    print(50 * "-", "\n")
    #
    # --- print errors oveer 1%
    #
    header('** Request Errors **')
    print("\tDay", "\t --> \tOver 1% Errored Requests ")
    print(50 * '-')
    for i in range(len(errors_by_day)):
        print(
            errors_by_day[i]['day'],
            ' ---> ',
            errors_by_day[i]['not_ok_proc']
        )
    print(50 * "-", "\n")


if __name__ == '__main__':
    main()
