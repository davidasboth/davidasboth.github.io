Title: The Junk in Fallout 4 - a Web Scraping Tutorial
Date: 2016-11-03 22:36
Author: david
Tags: python
Slug: the-junk-in-fallout-4
Status: published
Summary: This is a short web scraping tutorial based on a script I wrote to fetch and analyse data about junk in the game Fallout 4.

_This post originally appeared on my blog in 2016_

## Introduction

### The Problem

A few months ago I was playing one of my favourite games of 2015 -
[Fallout 4.](https://en.wikipedia.org/wiki/Fallout_4)

If you haven't heard of it, it's an action-RPG set in a post-apocalyptic
world. The story is engaging and you're sort of trying to rebuild
civilisation after the world has been devastated by nuclear war. I mean
"rebuild" quite literally - a lot of the game is spent scavenging for
raw materials so you can build pretty shoddy housing for strangers. And
that rebuilding requires raw materials, which is contained mostly in
junk.

Lots and lots of junk.

You can end up spending a disproportionately long time looking for,
buying and selling things like broken telephones, toy rocketships, teddy
bears, and ashtrays all because they contain precious raw materials for
your resettlement project, or for enhancing your guns and armour.

If you play it long enough eventually you start remembering which items
contain which raw material (information which then replaces more
important things in your brain...). However, not all items contain the
same amount of raw material. For example aluminium, which is quite
useful but relatively rare, is in oil cans (which contain 1, erm, "unit"
of aluminium) but it's better to get it from surgical trays, which
contain 3.

That means if you want to maximise your scavenging efforts you have to
start remembering which item contains which material *and* how much it
contains.

So I thought: is there a more efficient way of scavenging?

The answer is yes.

With data.

### The solution

What I really wanted to do is look at each material, and figure out
which items it made sense to find to maximise the amount of the material
I get. The plan was:

-   Find a list of all the items in Fallout 4 and the materials they
    contain
-   Scrape and store the list
-   Analyse it and make some plots


## The Tutorial

### Prerequisites

First of all, we need some data and some Python libraries.

The data comes from [a webpage of all Fallout 4 junk items](http://fallout.wikia.com/wiki/Fallout_4_junk_items), specifically
the table marked "[Other junk items](http://fallout.wikia.com/wiki/Fallout_4_junk_items#Other_junk_items)".

The Python libraries we need are:

-   [requests](http://docs.python-requests.org) - for fetching the
    webpage content via HTTP
-   [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) -
    for reading, parsing and extracting data from the returned HTML
-   [pandas](http://pandas.pydata.org/pandas-docs/stable/) - the usual
    suspect for manipulating data
-   [matplotlib](http://matplotlib.org/) - for plotting


### Step 1 - Fetch the Data

Side note: This isn't a tutorial about HTML, CSS or Javascript, so I'll
assume you know enough about them. However, if you want to learn/brush
up, [w3schools](http://www.w3schools.com) is a great resource.

We've identified our data source and it's already in a table format,
which will make things easier. What we want to do is isolate the table
in the HTML so we can extract only that table.

The easiest way to do this is directly on the website.

Right click and choose "Inspect Element".

{% with image_path='{static}/images/the-junk-in-fallout-4/inspect_element.png',
        image_alt='Inspecting an element',
        figcaption="I'm using Firefox but this should be applicable to any browser." %}
    {% include 'include/image.html' %}
{% endwith %}

This will open the Inspector, or Chrome Dev Tools or the equivalent,
where we can inspect the raw HTML. Then we want to look at the
&lt;table&gt; element to see its ID.

{% with image_path='{static}/images/the-junk-in-fallout-4/tablehtml.png',
        image_alt='HTML table in the inspector',
        figcaption="Unlucky, no ID." %}
    {% include 'include/image.html' %}
{% endwith %}

OK, well it doesn't have an ID, so we need to find a way to uniquely
select that element. It has a class "va-table-center" - we can check if
that's unique on the page. To do this, go into the Console tab of the
Inspector (in the above screenshot it's the second tab, but your browser
may differ). In the console you can type and evaluate arbitrary
Javascript/jQuery expressions, so let's try selecting a table with the
class *va-table-center*.

{% with image_path='{static}/images/the-junk-in-fallout-4/junktable_selector.png',
        image_alt='Selecting the table in the console',
        figcaption="Apparently a script on the page finished 'shamefully'..." %}
    {% include 'include/image.html' %}
{% endwith %}

It looks like that class isn't unique, there are 5 tables that match it
on the page. What we can do is then figure out which one of those 5 is
the one we need. We can expand the output on the console to help us find
it.

You can highlight each of the 5 items and the corresponding table will
be highlighted on the page. Doing this reveals we're after the second of
those 5 tables.

{% with image_path='{static}/images/the-junk-in-fallout-4/table_highlight.png',
        image_alt='Table highlight',
        figcaption="Note the Halloween-themed adverts about The Exorcist." %}
    {% include 'include/image.html' %}
{% endwith %}

Great, now we've identified the HTML element we want to load in, and we
can do the rest of the wrangling in Python.

### Step 2 - Clean and Wrangle

Using requests and BeautifulSoup we read in the HTML and grab just the
table we need.

    :::python
    import requests
    from bs4 import BeautifulSoup

    # load the entire page
    req = requests.get('http://fallout.wikia.com/wiki/Fallout_4_junk_items')
    
    # read the output as text
    raw = req.text

    # load it into BeautifulSoup for parsing
    soup = BeautifulSoup(raw, "html.parser")

    # select just the second table with the right class
    junk_table = soup.select("table.va-table-center")[1]

Next step is to iterate over the table rows and extract what we need.
For now, we'll focus on the item name and its components.

There are often multiple materials in a single item, so we need to
extract them individually. What you'll notice in the table is that each
new material starts with a capital letter, so we can split on that with
some regex. Then we'll create a dictionary where the key is the item and
the value is a list of its components.

    :::python
    junk_dict = {}

    # start from the second table row (to skip the header)
    for j in junk_table.findAll('tr')[1:]:
        # select all the table cells
        cells = j.select('td')
        # get item name and components cells
        item_name = cells[0].text.strip()
        components_cell = cells[5]
        # split components text at uppercase letters
        components = [x.strip() for x in re.findall('[A-Z][^A-Z]*', components_cell.text)]
        junk_dict[item_name] = components

Next we'll create a pandas DataFrame from the dictionary. The only quirk
is some components have "x2" style additions if there are more than one
units in the item, and the absence of this signifies 1 unit.

    :::python
    df = pd.DataFrame(columns = ('item', 'component', 'quantity'))
    row_idx = 0

    for k in junk_dict:
        for c in junk_dict[k]:
            quantity = 1 # default unless otherwise specified
            # extract the multiplier
            multiplier = re.search(' ?x ?([0-9]*)', c)
            component_name = c
            # if the multiplier is specified set the quantity to the right value
            if multiplier:
                if multiplier.group(1) != '':
                    quantity = int(multiplier.group(1))
                    component_name = c[:-3]
            # add as a row
            df.loc[row_idx] = [k, component_name.strip(), quantity]
            row_idx += 1

### Step 3 - Plot

We now have our very own Fallout 4 junk dataset that we can analyse to
our heart's content. For example we can plot the frequencies of each
component to order them by rarity.

{% with image_path='{static}/images/the-junk-in-fallout-4/junkplot.png',
        image_alt='A bar chart showing the rarity of junk components',
        figcaption="It's a strange world where concrete is so rare." %}
    {% include 'include/image.html' %}
{% endwith %}

## Conclusion

There you have it - data-driven video gaming. Here's the whole thing in
[Jupyter notebook form](https://github.com/davidasboth/blog-notebooks/blob/master/fallout-junk/Fallout%20Junk%20Data.ipynb),
and a direct link to [the csv file]({static}/files/fallout_junk.csv)
if you want to analyse it yourself - if you do, let me know!

### Post-script

Since writing this tutorial (in 2016) I discovered pandas has a `read_html()` method, which scans an entire HTML document and extracts all `<table>` elements as pandas DataFrames. You should definitely use that instead of looping over table rows and cells, but I'm keeping this tutorial as it was, since it's still instructive.