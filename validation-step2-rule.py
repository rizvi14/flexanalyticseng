import sqlite3
import pandas

# Connect to database
conn = sqlite3.connect('financial_data.db')

sqlquery = (
    """
    SELECT
        'group level' AS level_of_detail_validation,
        g.name AS level_name,
        MIN(g.value) AS level_value,
        SUM(a.value) AS lower_level_sum,
        CASE
            WHEN MIN(g.value) - SUM(a.value) = 0 THEN 'Balanced'
            ELSE 'ALERT: Unbalanced'
        END AS validation_message
        
    FROM
        categories c
    JOIN
        subcategories s
        ON c.category_id = s.category_id
    JOIN
        groups g
        ON s.subcategory_id = g.subcategory_id
    JOIN
        accounts a
        ON g.group_id = a.group_id

    GROUP BY 1,2

    UNION ALL

    SELECT
        'subcategory level' AS level_of_detail_validation,
        s.name AS level_name,
        MIN(s.value) AS level_value,
        SUM(g.value) AS lower_level_sum,
        CASE
            WHEN MIN(s.value) - SUM(g.value) = 0 THEN 'Balanced'
            ELSE 'ALERT: Unbalanced'
        END AS validation_message
        
    FROM
        categories c
    JOIN
        subcategories s
        ON c.category_id = s.category_id
    JOIN
        groups g
        ON s.subcategory_id = g.subcategory_id

    GROUP BY 1,2

    UNION ALL

    SELECT
        'category level' AS level_of_detail_validation,
        c.name AS level_name,
        MIN(c.value) AS level_value,
        SUM(s.value) AS lower_level_sum,
        CASE
            WHEN MIN(c.value) - SUM(s.value) = 0 THEN 'Balanced'
            ELSE 'ALERT: Unbalanced'
        END AS validation_message
        
    FROM
        categories c
    JOIN
        subcategories s
        ON c.category_id = s.category_id

    GROUP BY 1,2

    """
)

dataframe = pandas.read_sql(sqlquery,conn)
conn.close()

print(dataframe)