Title: Analysis: Is Alan Davies Getting Better at QI?
Date: 2017-02-15 12:06
Author: david
Slug: analysis-is-alan-davies-getting-better-at-qi
Status: published
Summary: I was watching a later series of QI recently and couldn't help but notice that Alan Davies was winning quite a few episodes. That prompted me to ask the question: is Alan Davies getting better at QI?

_This post originally appeared on my blog in 2017_

I'm a big fan of the quiz show [QI](https://en.wikipedia.org/wiki/QI). I
was watching a later series of it recently on Netflix and I couldn't
help but notice that Alan Davies was winning quite a few episodes. This
felt odd, because I was sure that when I first watched the show he
routinely finished last, and certainly wasn't winning any shows.

That prompted me to ask the question: *is Alan Davies getting better at
QI?*

To sate my curiosity I tried to answer that question the best way I know
how: with **data**.

## The Data

The data comes from [The British Comedy Guide](https://www.comedy.co.uk/), which has an exhaustive list of
everything related to British comedy, including every episode of QI.
There was a lot of laborious data cleaning involved, which you can see
for yourself in [the associated Jupyter notebook](https://github.com/davidasboth/blog-notebooks/blob/master/qi-analysis/Scrape%20QI%20Episodes.ipynb).

The [final dataset](https://github.com/davidasboth/blog-notebooks/blob/master/qi-analysis/qi_episodes.csv)
includes every episode with its title, broadcast date and each
contestant and their scores.


## The Analysis

As with many data science projects, once the dataset was nice and clean
the question was straightforward to answer. All it needed was a plot to
show Alan's win ratio over time. Here's the accompanying [Jupyter notebook](https://github.com/davidasboth/blog-notebooks/blob/master/qi-analysis/QI%20Analysis.ipynb).

{% with image_path='{static}/images/analysis-is-alan-davies-getting-better-at-qi/alan_davies_over_time.png',
        image_alt="Alan Davies's QI performance over time",
        figcaption="Alan's more or less consistently winning a quarter of shows now" %}
    {% include 'include/image.html' %}
{% endwith %}

So to answer the question: yes, Alan does appear to be getting better at
QI, certainly since the first few series. It does however remain to be
seen whether his win ratio will plateau at 25%, I guess we'll see in a
few years' time.