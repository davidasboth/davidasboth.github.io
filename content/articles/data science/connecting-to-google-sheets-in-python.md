Title: How to Connect to Google Sheets in Python
Date: 2016-11-13 13:54
Author: david
Tags: featured
Slug: connecting-to-google-sheets-in-python
Status: published
Summary: A quick tutorial on how to connect to Google Sheets in Python, so you can access it like a regular CSV file.
Alias: /2016/11/13/connecting-to-google-sheets-in-python

In most data science and machine learning tutorials you typically
encounter csv files. Either you connect to them locally, something like
this:

    :::python
	import pandas as pd
	df = pd.read_csv("my_local_data.csv")

Or you access them via a direct url like this:

    :::python
	import pandas as pd
	df = pd.read_csv("http://www.lotsofdata.com/hosted_data.csv")

What I rarely see though is connecting to slightly more obscure data
sources. You will probably end up doing this once you go out into the
real world of data science.

One useful data source is Google Sheets. If you have a spreadsheet
hosted on Google Drive, which is made available for public access, and
want to access it, it's not immediately clear how to do that.

Let's go through an example of how to connect to one. I'll use a
spreadsheet that has the [Hacker News salary survey results](https://docs.google.com/spreadsheets/d/17Mr201gfDoOTe5ONLS6LYJi1wQbtT26srXeSwUjMK0A/htmlview?usp=sharing&sle=true)
from a couple of years ago.

You can't use the url directly, because the url isn't just pointing to
the data, it's pointing to the entire Google Sheets interface.

Instead you need the sheet's export link.

To do this simply take the url until the /d/ part, and the unique ID
that comes after, so this much:

https://docs.google.com/spreadsheets/d/17Mr201gfDoOTe5ONLS6LYJi1wQbtT26srXeSwUjMK0A

and add **/export** at the end with some parameters.

You can specify the sheet number (zero-indexed) using **gid**, and the
format to be csv using **format**.

The full url then becomes:

[https://docs.google.com/spreadsheets/d/17Mr201gfDoOTe5ONLS6LYJi1wQbtT26srXeSwUjMK0A/**export?gid=0&format=csv**](https://docs.google.com/spreadsheets/d/17Mr201gfDoOTe5ONLS6LYJi1wQbtT26srXeSwUjMK0A/export?gid=0&format=csv)

Try that in your browser and it will download the csv file directly.

You can then read it into pandas and it will be treated as a regular csv
file.

Here is the [associated Jupyter notebook](https://github.com/davidasboth/blog-notebooks/blob/master/connecting-to-google-sheets/Connecting%20to%20a%20Google%20Sheet.ipynb)
to see it all in action.
