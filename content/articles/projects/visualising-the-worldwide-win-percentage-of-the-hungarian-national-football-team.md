Title: Visualising the Worldwide Win Percentage of the Hungarian National Football Team
Date: 2017-01-20 11:36
Author: david
Slug: visualising-the-worldwide-win-percentage-of-the-hungarian-national-football-team
Status: published
Summary: I've often read the advice that side projects should be solving problems or answering questions that you yourself are interested in. To that end, I've always wanted to know how well the Hungarian national team have done against various countries worldwide and to explore this question, I scraped the matches played by the Hungarian national team and made an interactive world map.
Alias: /2017/01/20/visualising-the-worldwide-win-percentage-of-the-hungarian-national-football-team

I've often read, and agreed with, the advice that side projects should
be solving problems or answering questions that you yourself are
interested in.

To that end, I've always wanted to know how well the Hungarian national
team have done against various countries worldwide. Hungary has [a
glorious football past](https://en.wikipedia.org/wiki/Golden_Team),
although the last 30 years have been possibly the worst ever decades in
Hungarian football.

To explore this question, I scraped a dataset of all matches played by
the Hungarian national team since 1907, aggregated it and made an
interactive world map.

I'll start with the final map, and you can read about some of the
details beneath.

![Hungarian National Team worldwide win percentage]({static}/images/visualising-the-worldwide-win-percentage-of-the-hungarian-national-football-team/hungarian-nt-win-map.png)

The worldwide win percentage of the national team

There is [an interactive version](https://plot.ly/~dasboth/0.embed)
where you can zoom and hover over each country to find out more. I
encourage you to look at it if you want to dive into the data and
explore. 

# The Details

## The Data

I scraped the data from the wonderful
[http://www.magyarfutball.hu](http://www.magyarfutball.hu/) which is a
great resource for those with the very niche interest in Hungarian
football. The data was unsurprisingly in Hungarian so I also had to
translate it!

There is [a Jupyter notebook](https://github.com/davidasboth/blog-notebooks/blob/master/hungarian-national-team/Scraping%20NT%20Data.ipynb)
for the scraping code and the [final dataset](https://github.com/davidasboth/blog-notebooks/blob/master/hungarian-national-team/hungarian_nt_matches.csv)
is also available.


## The Map

My [last experiment](/blog/the-world-map-of-the-2016-fifa-awards/)
making a [choropleth map](https://en.wikipedia.org/wiki/Choropleth_map)
was missing some features I'd have liked to add, such as more
interactivity. The library I used, folium, is still under development so
for this project I tried something new.

Introducing [plot.ly](http://plot.ly/)!

It's a great visualisation toolkit with a Python wrapper. It is much
easier to make interactive choropleths with it, I specifically used
[this set of tutorials](https://plot.ly/python/choropleth-maps/). The
ability to customise the hover label meant I could make a much more
useful visualisation, which you can explore.

There is [a Jupyter notebook](https://github.com/davidasboth/blog-notebooks/blob/master/hungarian-national-team/Mapping%20Records%20vs%20Countries.ipynb)
where I aggregated the data, dealt with countries that don't exist
anymore (the USSR, Yugoslavia, etc.) and made the final map.
