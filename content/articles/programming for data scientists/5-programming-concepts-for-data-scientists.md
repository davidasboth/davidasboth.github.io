Title: 5 Programming Concepts for Data Scientists
Date: 2016-11-23 20:17
Author: david
Tags: featured
Slug: 5-programming-concepts-for-data-scientists
Status: published
Summary: In this post I want to introduce some software development concepts that I think data scientists would benefit from. Specifically 5 of them.
Alias: /2016/11/23/5-programming-concepts-for-data-scientists

In a previous post I talked about maths you should know for data
science, partly with programmers in mind who want to move towards data
science.

Today I want to do the opposite.

I want to introduce some software development concepts that I think data
scientists would benefit from, and which are maybe less talked about
when discussing "what it takes" to be a data scientist.

## Source Control

To be fair, I've seen more and more data science resources cover this
topic, but it's still worth a mention.

If you start programming without source control and then get introduced
to it I guarantee you can't go back. It feels positively prehistoric
that once upon a time my version of source control was as sophisticated
as "code\_20160101.zip", "code\_20160104.zip" and so on (that's just an
example, I want to make it clear that I wasn't still doing that in
January 2016...).

The ability to go back to previous versions with near-zero effort, as
well as keep a log of what you've changed between versions is essential
for something as fundamentally experimental as the data science process.

Probably the most popular source control method these days is Git,
specifically [GitHub](https://github.com/) or
[BitBucket](https://bitbucket.org/). There are others out there, such as
subversion (using something like
[TortoiseSVN](https://tortoisesvn.net/)) or Microsoft's proprietary (and
expensive) Team Foundation Server.

You're probably better off using Git. Having a GitHub portfolio is
pretty handy.

If you don't want to learn the console commands ([obligatory related xkcd](https://xkcd.com/1597/)), don't feel obliged to.

I use [SourceTree](https://www.sourcetreeapp.com/) and it's pretty great.

## Automation

I've [touched on this topic before](/blog/turning-jupyter-notebooks-into-reusable-scripts/);
I think data scientists should adopt a lazy, programmer's mindset.

Automate everything you can.

Let the computer do the boring things while you do the hard thinking.

Have a script that automatically cleans your data, or even [does some of your machine learning for you](https://github.com/rhiever/tpot).

## IDEs

Using something like IPython to test out programming snippets in an
interactive way is a great idea. However, when you need more
reproducible code or just a bit more functionality than typing single
commands, use an IDE (Integrated Development Environment).

The staple Python IDE is the [Jupyter notebook](http://jupyter.org)
environment, great for presentation and reproducibility, and therefore
terrific for data science.

[Spyder](https://pythonhosted.org/spyder/),
[Rodeo](https://www.yhat.com/products/rodeo) and
[PyCharm](https://www.jetbrains.com/pycharm/) are all good alternatives.

At the very least use a text editor with syntax highlighting.
[Notepad++](https://notepad-plus-plus.org/), [Sublime Text](https://www.sublimetext.com/), [Atom](https://atom.io/) or similar.


## Relational Databases

One skill that is sometimes overlooked on data science courses is the
use of SQL and relational databases. I might even do a separate post
dedicated to this topic because I think it's a useful skill to have.

Database design is an important aspect of creating a functioning
application, so if you ever want to make your machine learning algorithm
into a software product it's worth knowing how best to design a backend
database.

Codecademy do [a SQL course](https://www.codecademy.com/learn/learn-sql)
(in fact it looks like they do multiple). I haven't done them myself,
but other Codecademy courses I've done were all excellent. My first SQL
resource was [w3schools](http://www.w3schools.com/sql/), which is also
worth a look.


## D. R. Y. - Don't Repeat Yourself

I'm not usually a fan of teaching people programming best practices when
they're starting out, and many people learning data science don't have a
programming background, but if there's one concept that I'd recommend
internalising it's this.

Don't repeat yourself.

If you have a few lines of code that do something that you'll need to do
over and over again, or you find yourself copying and pasting the same
code snippet multiple times, make it into a function.

If you have a collection of related functions you call over and over
again, make it into a class. At the very least move them into a separate
file.

These sound like little things but they add up and make your code easier
to read and more maintainable.

I hope you agree that data scientists can learn a lot of useful concepts
from software development, even if they never end up having to build
production-ready systems!
