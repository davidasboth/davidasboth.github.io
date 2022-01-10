Title: Method Chaining in Pandas
Date: 2016-11-30 18:14
Author: david
Tags: featured, pandas, python
Slug: method-chaining-in-pandas
Status: published
Summary: A discussion of "method chaining" in pandas. Used for better readability, or harder debugging, depending on how you look at it.
Alias: /2016/11/30/method-chaining-in-pandas

When you work with pandas, you'll often perform multiple operations on a
DataFrame. Some data cleaning and basic plotting for example, something
like this:

    :::python
    import pandas as pd

    df = pd.read_csv("my_data.csv")
    df = df.drop("column_1", axis=1)
    df = df.rename(columns={"column_2":"name", "column_3": "address"})
    by_address = df.groupby("address")
    by_address["name"].plot(kind="bar")


That works fine, you're incrementally changing the DataFrame until
you're ready for aggregation and plotting.

There is an alternative, which you might find more readable.

    :::python
    import pandas as pd

    df = pd.read_csv("my_data.csv")
    df.drop("column_1", axis=1)  \  
     .rename(columns={"column_2":"name", "column_3": "address"})  \  
     .groupby("address")["name"]  \  
     .plot(kind="bar")

Why can we keep chaining methods together like this?

In pandas, each of those functions returns a *copy* of the modified
DataFrame, which is why we were setting it back to the df variable each
time. By chaining methods together we're just calling the next method on
the modified DataFrame until we're done.

Notice we have to break lines with a backslash character to allow the
chain to go over multiple lines. You can avoid that by putting the
entire chain in brackets:

    :::python
    (df.drop("column_1", axis=1)
      .rename(columns={"column_2":"name", "column_3": "address"})
      .groupby("address")["name"]
      .plot(kind="bar"))

Logically and computationally these examples are equivalent, so this is
mostly just a stylistic consideration.


# Benefits

## Readability

I'd argue the second method looks better, it actually reads
right-to-left (or up-to-down I suppose) and you can understand logically
what you're doing each time.

## No Intermediate Variables

In the first example we had to either save back the modified DataFrame
to the original df variable, or create a new one each time. This means
you have to think about whether you want to store the DataFrame in each
of its states *and* come up with descriptive names for them, and as we
all know...

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">There are two hard things in computer science: cache invalidation, naming things, and off-by-one errors.</p>&mdash; Jeff Atwood (@codinghorror) <a href="https://twitter.com/codinghorror/status/506010907021828096?ref_src=twsrc%5Etfw">August 31, 2014</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## Avoids "inplace" Confusion

In my experience the fact that most DataFrame methods return a copy of
the DataFrame is actually confusingly counterintuitive for pandas
beginners. You either have to keep saving your DataFrame back to the
same variable, or use the "inplace" keyword. Using method chaining means
you only have to consider this problem once, i.e. set the final result
to a variable, without ever accidentally throwing away any of your
changes.


# Downsides

## No Intermediate Variables

Not having access to the intermediate states of the method can also be a
downside. If you want to reuse any of the intermediate steps in the
process, you need to keep a copy of it so you might not want to use
method chaining all the time.

## Debugging is Hard

Debugging a problem in a long method chain is hard. If your chain
consists of many intermediate steps and the final output is wrong, or
you get an error message, it can be hard to retrace your steps to see
what went wrong. If you had each command line by line, like in the first
example, you could step through the code with a debugger or simply run
the commands one at a time until you find the problem.

## You Can Get Carried Away

You can take method chaining to extremes...

    :::python
    import pandas as pd

    df = pd.read_csv("my_time_series.csv")

    # take a deep breath...
    (df.drop("column_1", axis=1)
       .rename(columns={"column_2":"date", "column_3":"price"})
       .dropna(subset="date")
       .fillna(0)
       .loc[df["price"] > 0, ["date", "price"]]
       .set_index("date")
       .resample("M")
       .mean()
       .plot())

Maybe that's a bit much.

# Best of Both Worlds 

There is a time and a place for method chaining.

If you don't care about intermediate steps, and just want a basic plot
for example, it's a good option.

If you want to do complex operations that might need serious debugging,
maybe it should be avoided.

What I tend to do is avoid using it while I'm still writing the code,
and refactor to use method chaining when I'm confident the code works.
The idea is that it helps future readability, so I can better understand
my code if I look back on it later.

This post was mostly inspired by the great [Modern Pandas series.](https://tomaugspurger.github.io/method-chaining.html)
