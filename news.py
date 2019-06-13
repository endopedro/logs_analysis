#! /usr/bin/env python
# -*- coding: utf-8 -*-
# PROJECT: LOG ANALYSIS
# UDACITY 2018

import psycopg2
import datetime

query1 = """SELECT title, count(*) AS views
    FROM log, articles
    WHERE path = CONCAT('/article/', articles.slug)
    GROUP BY title
    ORDER BY views DESC
    LIMIT 3;"""

query2 = """SELECT authors.name, count(*) AS views
    FROM authors, articles, log
    WHERE authors.id = articles.author
        AND path = CONCAT('/article/', articles.slug)
    GROUP BY authors.name
    ORDER BY views DESC
    LIMIT 4;"""

query3 = """SELECT *
    FROM daily_error
    WHERE percentage > 1;"""

DBNAME = "news"


def select(query, type):
    """Return the query result."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    # Printing results
    for i in range(len(results)):
        fst_col = results[i][0]
        scd_col = results[i][1]
        # The last question has a different treatment
        if type == 1:
            print(fst_col + " - " + str(scd_col) + " views")
        else:
            print(fst_col.strftime('%m/%d/%Y') + " - " + str(scd_col) + "%")
    db.close()

if __name__ == "__main__":
    print("1 - Quais são os três artigos mais populares de todos os tempos?")
    select(query1, 1)
    print("\n2 - Quem são os autores de artigos mais populares de todos os "
          "tempos?")
    select(query2, 1)
    print("\n3 - Em quais dias mais de 1% das requisições resultaram em "
          "erros?")
    select(query3, 2)
