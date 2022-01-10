Title: Turning Jupyter Notebooks into Reusable Scripts
Date: 2016-11-17 19:56
Author: david
Tags: python
Slug: turning-jupyter-notebooks-into-reusable-scripts
Status: published
Summary: As part of my commitment to occasionally talk about "programming for data scientists", I want to share ideas that will facilitate this to help data scientists focus on important stuff. In this post I want to share some thoughts on how to make your Jupyter notebooks easier to "productionise".
Alias: /2016/11/17/turning-jupyter-notebooks-into-reusable-scripts

I read an article today called Data Scientists Need More Automation. No
prizes for guessing what it was about.

A lot of the specifics were focused on sysadmin-type work like using
SSH, but the main idea is one that applies to all data science tasks.

The thrust of the article was:

> Someone please help data scientists be lazier, do less work, and
> reduce the mental overhead of dealing with computers!
>
> <small>From [Data Scientists Need More Automation](http://stiglerdiet.com/blog/2016/Nov/15/data-scientists-need-more-automation/)</small>

As part of my commitment to occasionally talk about "programming for
data scientists", I want to share ideas that will facilitate this to
help data scientists focus on important stuff.

Laziness is a virtue when it comes to programming.

Always thinking "how can I do the same thing with less effort?" is a
great way to be more productive and focus on the hard parts of data
science.

For example, it's clear that you want to speed up and automate your data
cleaning. That's not the important stuff you want to focus on. So in
this post I want to share some thoughts on how to make your Jupyter
notebooks easier to "productionise".

When you do data cleaning, notebooks are a great way to experiment with
your code in an interactive way before you can create a script that runs
on gigabytes of data. These thoughts are mostly concerned with how you
take a notebook that can clean a specific file, and make it into a
Python script you could run in the background to process many similar
files automatically.

## Start Small

If your datasets are big enough that processing them takes longer than a
few seconds, you are going to lose a lot of time if don't you test your
code on a smaller subset first.

If you are cleaning your data, you shouldn't be using your entire
dataset until you can prove that your script will run on a smaller
version of it. That might be as easy as just restricting your dataframe
to its first N rows:

    :::python
    import pandas as pd

    df = pd.read_csv("my_huge_file.csv")
    df = df.head(1000) # delete this line later, but only when you're ready!

This might sound obvious but it's important to get into the habit of
doing it.

### Brief Digression: Subsets of Data for Machine Learning

For machine learning, if you're just testing your code to make sure it
runs, you can do the same thing and take the first few hundred rows.
Obviously if you're training predictive models you want to use your
entire dataset.

*However*, if you want to just get a sense of which models are more
accurate than others, in the case of classification problems you can use
a **stratified** subset of your data. Instead of taking a random sample
you can sample based on the frequencies of your classes, so that your
smaller sample has the same class proportions. In scikit-learn you can
use
[StratifiedShuffleSplit](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html)
for example.

### Back to Notebooks...

Once you've experimented enough with your code so that you know it works
on your small subset, you'll want to ensure your code is general enough
that it would run with any file you give it.

For example, if you have a dataset that covers one day's of data you
might eventually want to let it loose and process months of data one day
at a time.

The obvious way to do this is parametrisation.

## Use Parameters

Stop hard-coding things.

Seriously, whenever you have a value that is likely to change when you
run the script multiple times, make it a variable.

Turn this:

    :::python
    pd.read_csv("my_data_2016-01-01.csv")

Into this:

    :::python
    filepath = "my_data_2016-01-01.csv"
    pd.read_csv(filepath)

It's an extra line but you're going to have to do it if you want to
automate your script, so get in the habit of starting out like this.

Even better, create a separate cell at the top of your notebook **just
for parameters**. That way you won't forget which things will need to
change for each file.

## Converting Parameters to Command Line Arguments

If you've created the right variables for automation, you can convert
them to command line arguments.

This can be as simple as exporting your notebook to a Python file (File
-&gt; Download as -&gt; Python) and replacing your parameters with
command line arguments.

Assuming your notebook looks something like this:

    :::python
    date = "2016-01-01"
    other_parameter = 16

    # rest of your code here...
    # ...
    # ...

Export it to Python, then amend the script slightly:

    :::python
    import sys

    if __name__ == "__main__":
        date = sys.argv[1]
        other_parameter = sys.argv[2]

        # the rest of your code from the notebook
        # can be pasted here UNEDITED

All we've done is replace the hard-coded parameter values with arguments
from the command line (remember [sys.argv\[0\] is the name of the script](http://stackoverflow.com/a/2626634/2039162)), so now you can do
this on the command line:

    :::python
    python my_automated_script.py "2016-01-01" "15"

This is the "quick and dirty" way of doing it. For more robustness and
better documentation of your arguments, use
[argparse](https://docs.python.org/3/library/argparse.html) or
[begins](https://pypi.python.org/pypi/begins/0.9).

To make this workflow possible, you also need to make sure your notebook
doesn't do too much.

## Single-Purpose Notebooks

There might be a lot of code involved in cleaning your data. You might
need to deal with things like missing values, but then perform
transformations and computations.

Eventually your notebook might be hundreds of lines of code.

If you ever get to that point, break the notebook into multiple smaller
ones. You could even make the first notebook output a semi-cleaned
version of your data which your second notebook picks up.

You can then still combine your notebooks into one Python script by
exporting them, and just removing the intermediate files that you were
creating when experimenting.

Say your notebook workflow is like this:

1.  Notebook 1 reads raw csv
2.  Notebook 1 does some data cleaning
3.  Notebook 1 exports semi-cleaned data (intermediate csv)
4.  Notebook 2 reads in intermediate csv
5.  Notebook 2 does data transformations
6.  Notebook 2 exports final csv

You can see that if we export both notebooks, combine them into a single
file and **remove steps 3 and 4**, we get our final automated script. In
fact, if we encounter problems later on we can always go back and debug
them using our notebooks, and re-export them to get an updated version
of the script. As long as you make all your changes in the notebooks and
not the final script, this will be a valuable approach.

Hopefully I've given you some ideas about how you can design your
notebooks from the start with a view to future automation.

Now go forth and be lazy!
