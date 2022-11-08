Title: SQL For Data Scientists
Date: 2016-11-26 20:08
Author: david
Tags: featured
Slug: sql-for-data-scientists
Status: published
Summary: SQL is a useful part of a data scientist's toolkit and it can feel like an intimidatingly big area to try and learn alongside all the other data science concepts. I want to present a few key concepts that are enough to get you up and running with SQL!

From what I can tell, the biggest difference between data science
curricula and data science job postings is usually knowledge of SQL. I
assume most businesses want a data scientist who knows SQL because a lot
of corporate data is stored in some sort of relational database. For
some reason though, data science courses don't always tend to teach it
explicitly.

I wanted to collect some of the concepts which I think are useful for
aspiring data scientists to learn about databases and SQL. I'll also
link to appropriate parts of the [w3schools SQL tutorials](http://www.w3schools.com/sql/) along the way.


## Query Syntax

Obviously the first step is to understand how to write a SQL query.

SQL is a [declarative language](https://en.wikipedia.org/wiki/Declarative_programming). All
that means is that when you write a SQL query, you're expressing **what the result should look like, rather than how to achieve it**.

Let's look at a basic SQL query and see how that's the case.

    :::sql
    SELECT
        name, age, height
    FROM
        people
    WHERE
        job = "data scientist"

SQL is not case sensitive, but I capitalised the keywords (which is a
typical thing to do anyway).

If you know that you have a table of data, called **people**, you can
pretty much work out what this query will do. The declarative syntax
means you can specify the data source (the people table), what you want
to extract (name, age and height) and any filters you want to apply
(only get the data for people who are data scientists).

There is a lot going on under the hood in terms of the computer deciding
how best to store and index the data, but when you write queries you
don't want to have to care about that, you just want your results.

The main keywords you need to know are:

-   [SELECT...FROM](http://www.w3schools.com/sql/sql_select.asp) (to select rows from a specific table)
-   [WHERE](http://www.w3schools.com/sql/sql_where.asp) (to filter
    rows - *optional*)
-   [INSERT](http://www.w3schools.com/sql/sql_insert.asp) (to insert new
    rows)
-   [UPDATE](http://www.w3schools.com/sql/sql_update.asp) (to update
    existing rows)
-   [DELETE](http://www.w3schools.com/sql/sql_delete.asp) (to remove
    rows)
-   [GROUP BY](http://www.w3schools.com/sql/sql_groupby.asp) (to group
    data into... well, groups)
-   [CREATE TABLE](http://www.w3schools.com/sql/sql_create_table.asp)
    (to create new tables)
-   [ALTER TABLE](http://www.w3schools.com/sql/sql_alter.asp) (to make
    changes to tables like adding new columns)
-   [JOIN](http://www.w3schools.com/sql/sql_join.asp) (to join multiple
    tables together)

## The JOIN keyword

I left the JOIN keyword until last in that list because it warrants its
own section.

Merging multiple data sources is a staple data science operation, and
that's no different when working with SQL. If you've used the merge
function in pandas you'll have seen this already, but let's see how they
compare.

Let's take the example of joining two data sources with pandas. One of
them is a csv of people, with names, ages, heights and jobs. The other
is a csv of phone numbers linked to people's names. The name column is
common between both data sources.

    :::python
    import pandas as pd

    df = pd.read_csv("people.csv")
    phone_numbers = pd.read_csv("phone_numbers.csv")

    merged = pd.merge(df, phone_numbers, on="name", how="inner")

That *how* keyword corresponds to the type of join in SQL. The same
operation in SQL looks like this (assuming we have a people and
phone\_numbers table in a database, rather than csv files):

    :::sql
    SELECT
      people.name, people.age, people.height, phone_numbers.phone_number
    FROM
      people
      INNER JOIN phone_numbers ON people.name = phone_numbers.name

I've specifically stated in the SELECT clause where the columns come
from, because both tables have a name column and SQL would have gotten
confused otherwise.

The types of SQL join correspond to the valid values of the "how"
keyword in the pandas merge function. They are:

-   [Inner Join](http://www.w3schools.com/sql/sql_join_inner.asp) - only
    rows where both tables have a value are returned
-   [Left Outer Join](http://www.w3schools.com/sql/sql_join_left.asp) -
    only rows where the table on the left of the statement has a value
    are returned
-   [Right Outer Join](http://www.w3schools.com/sql/sql_join_right.asp) - only rows
    where the table on the right of the statement has a value are
    returned
-   [Full Outer Join](http://www.w3schools.com/sql/sql_join_full.asp) -
    all rows are returned from both tables


The outer joins let you keep rows from either table if there are no
corresponding rows in the other table.

So a left join in the previous statements would have shown all people,
regardless of whether they had a phone number in the second data source.
The rows of people who don't have a phone number would have shown a NULL
value for the phone number. Using an inner join wouldn't have returned
them at all.

It can be helpful to see this visually, and the w3schools pages do that
already, but [here's another good example](https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/).

 
## SQL Tools for Data Science


If you know the basic query syntax and the various join types, you're
probably equipped enough to start pulling data out of any SQL database.
Programmers working with SQL often use specific tools to access
databases, such as Microsoft's SQL Server Management Studio.

However, as a data scientist you may want to do this straight from your
code instead. You have a few options for this.

-   You can [connect to sqlite](http://www.datacarpentry.org/python-ecology-lesson/08-working-with-sql)
-   You can use SQL queries in pandas [using pandasql](http://blog.yhat.com/posts/pandasql-sql-for-pandas-dataframes.html)
-   pandas also allows [connecting to SQL sources](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_sql.html)


Also, if you're familiar with pandas but not with SQL, the pandas
documentation has a section with [pandas commands and the associated SQL queries](http://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html).

## Conclusion

I'd argue that's all you need to get up and running.

W3schools is a great interactive resource to test your sql queries, but
there are plenty of other good learning resources like
[Codecademy](https://www.codecademy.com/learn/learn-sql).

There is more to know of course about relational databases. I haven't
covered the concepts of primary keys, foreign keys, or indexes because
these are more important for database design rather than data retrieval.
Designing a relational database has its own set of skills and required
knowledge, but if your only interaction is retrieving data, you
shouldn't have to worry about it.

I may write a post about database design in the future, but I'd strongly
argue that it's an optional skill for most data scientists.
