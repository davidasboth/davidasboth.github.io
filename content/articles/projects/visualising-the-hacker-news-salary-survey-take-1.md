Title: Visualising the Hacker News Salary Survey(Take 1)
Date: 2015-11-06 19:15
Author: david
Tags: datavis, featured
Slug: blog/visualising-the-hacker-news-salary-survey-take-1
url: blog/visualising-the-hacker-news-salary-survey-take-1
save_as: blog/visualising-the-hacker-news-salary-survey-take-1/index.html
Status: published

A few months ago, before starting a Masters in Data Science, I
experimented with a bit of data visualisation. I am an avid reader of
[Hacker News](https://news.ycombinator.com), which is a great site for
programmers to frequent. If you don't already know it, I can't recommend
it highly enough if you feel like you want to spend your procrastinating
time more wisely (that's my main motivation for visiting, anyway...). It
was an ad-hoc survey on there that led me to make this little
visualisation and I'd like to share the end result, as well as the
process that went into it, for two reasons. The first reason is that it
could give some interesting insight into how an amateur would approach a
data science problem using nothing but programming knowledge and some
common sense. The second reason is that in a few months I will revisit
this exact data set and analyse/visualise it again, to see how I can
apply what I learned on my course to improve upon my first attempt.

All I can say is: I anticipate the second attempt will be
recognisably... better.

So, without further ado I present:


## The (sort of) layman's guide to a basic data visualisation

### The Data

About the dataset: this was an anonymous survey run on Hacker News of
around 400 developers and designers, with data gathered about their job
title, seniority, location and salary. The dataset is inherently 'dirty'
as it contains some of the usual suspects: it has values in different
currencies, seniority levels and job titles aren't standardised and
there are multiple different entries for the same location.

The dataset I used is available
[here](https://docs.google.com/spreadsheets/d/17Mr201gfDoOTe5ONLS6LYJi1wQbtT26srXeSwUjMK0A/htmlview?usp=sharing&sle=true)
(credit to [@cameronmoll](http://twitter.com/cameronmoll) for making it
happen).

The original Hacker News discussion for those interested is
[here](https://news.ycombinator.com/item?id=8573221).


### The Hypothesis

As with any data science task, I needed to start with a hypothesis or a
purpose. Essentially I wanted to use this mini-project to find a nice
way to plot data on a map, so the purpose was to clean the data and find
a good library to visualise it geographically. I'll be honest, being a
data science layman I didn't even have a hypothesis about the data.

I just wanted to make a pretty map.


### The Process

#### Data Wrangling

Data wrangling is my favourite of the many phrases (closely followed by
'data jiu-jitsu') used to describe the act of 'cleaning' a dataset, i.e.
getting it into a shape that's suitable for analysis. It is apparently
what data scientists spend most of their time doing, so it's an
important step. This includes dealing with missing values, correcting
duplicate values (e.g. making sure we treat "London" and "London,
England" as the same location) and so on.

Let's have a look at some of the issues with the dataset after an
initial inspection:

-   The figures are in different currencies, this will need to be
    rectified
-   The job titles need to be merged into one column
-   The locations contain duplicates (e.g. 'US', 'USA', 'United States'
    all appear) 

Before I can do any meaningful analysis or visualisation, these issues
need to be ironed out. Being a data layman at the time, my data
wrangling tool of choice was Excel and I did most of my work manually.
My data wrangling consisted of:

-   Looking up the most up-to-date exchange rates online and converting
    all figures to USD (yes, I did this manually...)
-   Merging the job titles into one column
-   Manually merging duplicate locations (on the country column only)


Doing this all by hand was a pretty tedious method to use, and one I
don't wish to repeat in future. It's also an implausible method for
larger datasets, so when I revisit this dataset I'll look at what I
could have automated using something like Python or R.

You can download my final version of the dataset here (hopefully you'll agree it's better!): [Salary Data](http://davidasboth.com/wp-content/uploads/2015/10/SalaryData.csv)


#### Summarisation and Aggregation

Now was the time to do some basic statistics and aggregation to be able
to see the average salary by country on a map.

To do this, I used some basic [R, a popular data science
language](https://en.wikipedia.org/wiki/R_%28programming_language%29). I
recommend it as a good starting point for aspiring data scientists. My R
script was quite simple, the only real important line was the one that
took the salaries and averaged them by location:

    :::r
    # load the data
    SalaryData <- read.csv("SalaryData.csv")

    # get mean values in a table
    byCountry <- aggregate(SalaryUSD~Country, SalaryData, mean)

    # write new data to csv
    write.csv(byCountry, "ByCountry.csv")


Once this was done, it was time to get this onto a map!


#### Visualisation

I used [this excellent tutorial](http://jsdatav.is/chap06.html) to
visualise my data on a map using a map font and some Javascript. I
cheated a bit and manually entered the figures into a Javascript array
(one of the enhancements I'll do is to actually read that in from a
file). I won't go into depth about what I did differently, because I
pretty much followed the tutorial step by step, tweaking things like
colours as I went. I recommend following along, it's a very well-written
tutorial.

If you want to view it in the browser, here's [the final product](/hn-map/), otherwise, you can see it in
all its glory below.

![Hacker News Salary Map]({static}/images/visualising-the-hacker-news-salary-survey-take-1/hn-salary-map.png)

The survey proved Norway is practically radioactive due to high tech salaries


All the data I wrangled and code I wrote is [available on GitHub](https://github.com/davidasboth/HN-Survey-Analysis).

#### Conclusion

If you're interested in data analysis but have no idea where to start, I
hope this post will inspire you to try and attempt your own
visualisation without fear of getting it wrong. Data science is all
about trial and error, so I say just go for it! I used nothing but my
own intuition to come up with the process for what I did, there wasn't
any knowledge of best practices behind it, and I still came up with a
colourful visual that communicates something about the data.

