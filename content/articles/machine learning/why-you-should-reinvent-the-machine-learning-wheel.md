Title: Why You Should Reinvent the Machine Learning Wheel
Date: 2016-11-11 17:17
Author: david
Tags: featured
Slug: blog/why-you-should-reinvent-the-machine-learning-wheel
url: blog/why-you-should-reinvent-the-machine-learning-wheel
save_as: blog/why-you-should-reinvent-the-machine-learning-wheel/index.html
Status: published

When you're a data scientist, unless you're in a job that's very
research-focused (and likely requires a PhD) you'll mostly be using
machine learning algorithms invented anywhere between say 5 and 30 years
ago. Similar to being a programmer, you'll be using many libraries made
by other people based on other people's ideas.

There's nothing wrong with that.

In fact, it's usually more productive to use someone else's
implementation of an idea. Why reinvent the wheel every time?

With machine learning, I want to make a case for why it's good to
reinvent the wheel **when you're still learning**.

I want to stress that I still think it's a good idea to use scikit-learn
99% of the time. However, when you're learning about [one of the most popular algorithms](http://www.kdnuggets.com/2016/08/10-algorithms-machine-learning-engineers.html)
(I've linked to this KDNuggets article before because I think it's a
good overview of the minimum you should know) I think it's worthwhile
trying to implement them yourself.

So why go through the effort of implementing existing algorithms again?

### Programming Practice

This is an obvious benefit of trying to implement anything: you get
programming experience. Many data scientists don't come from a
programming background, so a crucial part of the learning process is
feeling at home when writing code. Coupling this with additional machine
learning practice seems like a good way to do this.

Also, implementing machine learning algorithms is a harder coding
challenge than the ones you'd face if you were doing an introductory
programming course, so this is a good transition from FizzBuzz-type
problems to more meaty challenges.

### Deeper Understanding

I'd argue this is the most important benefit. It's one thing to
conceptually understand an algorithm and it's another to understand it
in enough depth to tell a computer how to do it. Computers don't deal
with ambiguity so you need to understand every little implementation
detail to get to the end. That can only be helpful in deepening your
understanding. Once you move on and use in-built libraries you can also
more easily debug any strange behaviour because you'll know more about
what is happening under the hood.

### Portfolio Pieces

Perhaps not a reason to do this outright, but a good byproduct of these
coding exercises is getting little pieces to add to your GitHub profile.
That's never a bad thing.

A few things to remember.

### We are not trying to "beat" other implementations

If you're really into optimisation and want to spend time learning how
to make your implementations faster, obviously I wouldn't advise against
it. At the same time it might not be worthwhile spending too much time
improving the performance/scalability of your code if your aim was to
deepen your understanding of machine learning.

### Don't overdo it and implement everything you read about

Again, I'm not suggesting you should actively **not** implement every
algorithm you hear about, but some algorithms might be harder to
implement than others. Start small to avoid getting frustrated by
complex problems. For example, don't start by implementing a deep
convolutional neural network.

Then which algorithms should I choose?

Here are the ones I've gone for so far, because I thought they were easy
enough to implement but I wanted to dive in to the details.

### Naive Bayes

This was one of the activities of the [Becoming a Data Scientist Learning Club](http://www.becomingadatascientist.com/learningclub/).
Actually, the activity was to read about and use the algorithm, but I
took this as an opportunity to go through and [implement it from scratch](https://github.com/davidasboth/data-science-learning-club/tree/master/activity-5-naive-bayes).

The Naive Bayes classifier is conceptually quite straightforward and a
good place to start.

### K-Means Clustering

I will spend some time later this month diving into clustering, but for
now it's enough to say that this is also a good choice to start with.
Conceptually simple, but you need to understand the details to be able
to code the whole thing.

This is [another algorithm I implemented](https://github.com/davidasboth/data-science-learning-club/blob/master/activity-6-kmeans/notebooks/K-Means.ipynb)
as part of the Learning Club.

### Self-Organising Maps

I
[discussed](/blog/self-organising-maps-an-introduction/)
this algorithm recently, and hopefully showed that two blog posts are
enough to go through the details enough to actually [write the code](https://github.com/davidasboth/blog-notebooks/blob/master/self-organising-map/Self-Organising%20Map.ipynb)
for it. This is perhaps a less mainstream choice but conceptually lends
itself to a good coding exercise.

### Markov Chains

A popular choice for modelling and predicting sequential data (text,
audio, time series). It only requires simple probability theory and is
another good choice to start with.

Another topic I'll return to later this month. My
[implementation](https://github.com/davidasboth/markov-chain-for-text)
generates new text based on text you give it.

### Other Choices

Some other algorithms I suggest might be reasonable choices:

-   [Decision Trees](http://machinelearningmastery.com/classification-and-regression-trees-for-machine-learning/)
    (although you might end up needing the help of
    [recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science)))
-   [K Nearest Neighbours](http://machinelearningmastery.com/k-nearest-neighbors-for-machine-learning/)

Or if you're feeling a bit more brave, try a [Multilayer Perceptron](http://deeplearning.net/tutorial/mlp.html). You'll need to
understand and [implement backpropagation](https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/),
but it would be a good advanced programming challenge.

Hopefully I've convinced you that implementing machine algorithms from
scratch is a worthwhile endeavour. I'm always interested in seeing other
people's implementations so let me know if you've done any!

Footnote: This was the 11<sup>th</sup> entry in my [30 day blog challenge](/blog/30-posts-in-30-days/).
