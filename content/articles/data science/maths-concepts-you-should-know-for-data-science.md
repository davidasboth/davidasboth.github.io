Title: Maths Concepts You Should Know for Data Science
Date: 2016-11-22 18:31
Author: david
Tags: featured
Slug: blog/maths-concepts-you-should-know-for-data-science
url: blog/maths-concepts-you-should-know-for-data-science
save_as: blog/maths-concepts-you-should-know-for-data-science/index.html
Status: published

If you're interested in data science, I have some potentially bad news -
you need to know some maths.

The good news is that despite what some resources might suggest, you
don't need *that much.* You still need more than zero, but chances are
you'll have seen a lot of it in high/secondary school.

Here's an overview of what topics you should brush up on.


# Linear Algebra


## What?

I've always thought the words "linear algebra" sound more intimidating
than they need to.

Basically, you need to know what a vector and a matrix are, the notation
to represent them, and how to do basic operations with them (addition,
multiplication, transposing, dot products, that sort of thing).

## Why?

Datasets are usually represented as matrices where each rows is a data
point and each column is a feature. When you talk about single data
points or parameters to machine learning algorithms, they're typically
vectors. You can avoid a lot of confusion by having your vector/matrix
knowledge up to date.

 

# Statistics
 

## What?

Arguably if you don't brush up on anything else it should be this.

You should know your means from your medians, your Gaussian distribution
from your multinomial, and you should know about the [Central Limit Theorem](http://www.jeannicholashould.com/the-theorem-every-data-scientist-should-know.html).

Understanding sampling and hypothesis testing is also important.

## Why?

> "Data scientists are statisticians because being a statistician is
> awesome and anyone who does cool things with data is a statistician."
>
> <small>Robert Rodriguez, President, American Statistical Association</small>

OK so the head of the American Statistical Association might not be the
most reliable source on how useful statistics is.

Overlooking that, the point is that data science is in many ways
computational statistics. You can't get away from the fact that
understanding fundamental statistical concepts is essential to make any
sense of data.

 
# Probability
 

## What?

Being comfortable with representations of probability and seeing
probability distributions is enough to cover your bases. You shouldn't
be thrown off by phrases like "conditional probability" or "random
variable".

Oh, also [learn and understand Bayes' Theorem](https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/).

## Why?

Understanding probabilities is a useful life skill anyway. Humans are
typically not wired to intuitively understand probabilities (I recommend
[The Drunkard's Walk](https://en.wikipedia.org/wiki/The_Drunkard's_Walk)
on this subject). Being able to do it is a good skill for a data
scientist. Also, many machine learning algorithms deal with
probabilities and probability distributions one way or another.


# Calculus (optional)

The word "optional" might be controversial among some data scientists.
I'd argue that you can go a long way in data science without ever
calculating a partial derivative.

Having said that, knowing **what** a partial derivative is and what it's
used for can't hurt. Some machine learning algorithms (neural networks,
linear regression) require that understanding if you want to go into the
details. Don't go anywhere near "gradient descent" until you understand
why you'd want to set a partial derivative to zero.

So high school level calculus (derivatives, integrals, the 'chain rule')
are useful concepts to know, but don't start there. The other things
I've mentioned above are more important.


## Resources

[Khan Academy](https://www.khanacademy.org/) has been my favourite
resource for brushing up on maths subjects. Something about Sal Khan's
teaching style really resonates with me.

For more advanced topics, the YouTube channel
[mathematicalmonk](https://www.youtube.com/user/mathematicalmonk) is
also excellent.

For linear algebra, getting familiar with the numpy library is also a
good idea if you already know some Python, as numpy encourages you to
deal with vectorised operations.

If you already have programming experience, check out [Project Euler](https://projecteuler.net/) - it's a series of mathematical
challenges you solve by writing code. It might not be immediately
related to data science, but it's a great way to get a bit more
motivated about maths.

Hopefully I've convinced you that you don't need a PhD in maths to
embark on the road to data science!


Footnote: This was the 22<sup>nd</sup> entry in my [30 day blog challenge](/blog/30-posts-in-30-days/).
