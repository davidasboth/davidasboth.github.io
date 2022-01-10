Title: Pandas: Thinking in Vectors
Date: 2016-11-04 20:35
Author: david
Tags: pandas, python
Slug: pandas-thinking-in-vectors
Status: published
Summary: Often when using pandas it pays to think about a faster, but perhaps less intuitive, vectorised way of doing things.
Alias: /2016/11/04/pandas-thinking-in-vectors

The more you use pandas to wrangle your data the more likely you'll come
across something complicated that you won't be sure how to do. I found
this quite quickly when trying to calculate metrics with time series
data for example.

In these cases quite often the first solution that pops into my head
will be the naive, brute force one. Something like "well we can loop
through all the rows and perform a computation on each row one by one".

That is almost never the right approach, because it will be *slow*.

The better solution is almost always to make use of vectorisation.

Pandas is built on top of numpy, which is built with vectors in mind -
that is, manipulating entire arrays at once rather than the individual
elements.

That way of thinking can be a hard to adjust to when the temptation is
to use loops.

Sometimes it's not a bad idea to start with the brute force approach to
be confident of the answer, and then move to a vectorised solution. For
large datasets though, this move can easily be the difference between
the script taking seconds or hours to run.

# Examples

## Date Methods

Applying methods to a column of date values is a common data
manipulation task, for example when extracting the day as a new feature.
There are (at least) two functionally identical ways of doing this:

    :::python
    # Method 1 - row by row
    days = []
    for s in my_dataframe["my_date_column"]:
        days.append(s.day)
    my_dataframe["day"] = days

    # Method 2 - using the inbuilt and vectorised date functionality
    my_dataframe["day"] = my_dataframe["my_date_column"].dt.day

They'll do exactly the same thing, but the second will be orders of
magnitude faster.

## Subtracting Consecutive Values

This is one of those problems where, if you don't know the pandas way to
do it, it's easy to start thinking row by row.

Again, here are two functionally identical ways of doing it:

    :::python
    # Method 1 - a function to loop through the elements one by one
    def naive_diff(series):
        diff_values = []
        for i in range(len(series)):
            # first value needs to be NaN
            if i == 0:
                diff_values.append(np.NaN)
            else:
                diff_values.append(series[i] - series[i-1])
        return diff_values

    df["diff"] = naive_diff(df["measurement"])

    # Method 2 - using the pandas shift() function
    df["diff_2"] = df["measurement"] - df["measurement"].shift()

As well as being shorter, the second method is again much faster.

# Conclusion

This was just a *very* brief introduction into thinking in vectors when
using pandas.

The code is available [as a Jupyter notebook](https://github.com/davidasboth/blog-notebooks/blob/master/pandas-thinking-in-vectors/pandas-vector-examples.ipynb).

The take away message is that whenever you need to do something to each
row, it's worth spending time doing some research to look for an
appropriate, in built function, and thinking a bit harder about how to
solve it in a vectorised way.

## Footnote: Apply and Itertuples

If you absolutely must loop through the dataframe row by row, you should
consider using apply and itertuples. They are two pandas functions that
let you perform elementwise computation, but are faster than manually
looping through the row indices.

There are further good tips [under this StackOverflow question](http://stackoverflow.com/questions/7837722/what-is-the-most-efficient-way-to-loop-through-dataframes-with-pandas).

## Further Reading

When doing some research for this post I came across [this blog post](https://www.datascience.com/blog/straightening-loops-how-to-vectorize-data-aggregation-with-pandas-and-numpy/),
which is worth a read on the subject.
