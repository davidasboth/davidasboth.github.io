Title: Realistic Machine Learning
Date: 2016-11-10 15:41
Author: david
Slug: realistic-machine-learning
Status: published
Summary: As most data scientists quickly realise, there's a difference between the kind of data science you do while learning about it, and the kind you do at a real job. This is equally true of data cleaning/wrangling and machine learning.

As most data scientists quickly realise, there's a difference
between the kind of data science you do while learning about it, and the
kind you do at a real job.

This is especially true of university degrees, and isn't unique to data
science. However much you learn during your degree, reality will always
be different in a way you weren't prepared for. I don't mean this in a
scary way, just as a matter-of-fact appraisal of how things are.

This is equally true of data cleaning/wrangling and machine learning.

The "ML Hipster" [summed this up very well.](https://twitter.com/ML_Hipster/status/633954383542128640)

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">… and that concludes Machine Learning 101. Now, go forth and apply what you&#39;ve learned to real data! <a href="http://t.co/D6wSKgdjeM">pic.twitter.com/D6wSKgdjeM</a></p>&mdash; ML Hipster (@ML_Hipster) <a href="https://twitter.com/ML_Hipster/status/633954383542128640?ref_src=twsrc%5Etfw">August 19, 2015</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

There's also this quote I've seen (source unknown):

In data science, 80% of time is spent preparing data, and 20% of time is spent complaining about the need to prepare data

What are the main reasons for this disconnect?

### Real Data is Messy

Yes some data science courses cover this and talk about what sorts of
things you'd need to do to clean a dataset.

However, this usually amounts to converting strings to dates or dealing
with missing values. These are important skills to have, but only make
up 10% of the kind of data cleaning you might encounter.

Human-generated data is messy because people are not consistent, and
often data entry systems allow multiple ways of entering data or simply
free text.

Computer/machine-generated data is messy because things can go wrong,
log files from systems can have weird values in them, etc.

Not only does this have an impact on your data cleaning efforts (by
requiring 10x more work than anticipated) but also machine learning.

Scikit-learn random forests are not designed to deal with someone
putting "next Tuesday" in a free-type date field.

### The Question is Unclear

An underappreciated quality of a data scientist is the ability to frame
the question.

Converting a business requirement, which is often nebulous and
unquantifiable, into a machine learning problem is a difficult task.
There's usually more than one way to approach it, but it boils down to
making a human problem into a concrete, measurable task for an
algorithm.

This means a shift from your studies where you're given the question. No
longer are you identifying types of iris - you need to start with
identifying what to identify!

### A Difference of Purpose

This is the big one. The moment you're doing data science for a
business, your aims are different.

Previously you were solving problems for the sake of it. Now, the focus
is on **adding value**.

That means that at any point in a project the next step will depend on
what makes sense for the business, not what is academically most
interesting. The kind of work you do will by definition be different to
what you're used to.


# How can we better prepare?

The obvious way to smooth the transition between academia (or "learning"
in general) and industry is to teach more realistic problems.

That's not to say you should **start** with solving a business problem,
but you should certainly **end** on one.

A more rounded way of teaching data science would be to start with toy
problems and gradually build up to more complex ones. Something like
this scale of four difficulties:

#### Difficulty 1

You're given an "academic" dataset with perhaps some cleaning to do
(date formats, missing values). There is an explicit target value so
once the cleaning is done you know exactly what to do for machine
learning (e.g. predict the type of iris).

#### Difficulty 2

You're given a "real" dataset obtained from some real system or somehow
produced by real humans. There is not just some cleaning to do, but
questions of interpretation, data transformations, maybe even some
feature engineering. The machine learning task is still clear though.

#### Difficulty 3

A real dataset but with a less well-defined machine learning task. This
could be an unsupervised problem, where part of the work is in
interpreting the outcomes, or it could just be unclear whether you want
a classification or a regression approach. For example, a dataset with
sales figures where it's unclear if you should predict sales to the
nearest unit or just which group the sales belong to (in terms of size).

#### Difficulty 4

The "real world problem". You're given a broad task to solve but no
data, or a dataset that clearly needs enhancing somehow. This task would
involve scraping or just trawling the net for open data, then defining
your features and deciding on how best to frame it as a machine learning
problem.

For the last type of task to work though, I'd argue the teaching has to
be interactive. It's much easier to evaluate your approach by getting
qualitative feedback, unlike the first 2-3 tasks where you can
objectively measure your success.

This isn't always a practical way to teach, but it would go a long way
in preparing people for the reality of data science in the wild.
