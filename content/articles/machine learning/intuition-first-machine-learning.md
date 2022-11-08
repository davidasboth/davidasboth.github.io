Title: "Intuition First" Machine Learning
Date: 2016-11-07 09:34
Author: david
Slug: intuition-first-machine-learning
Status: published
Summary: I've often felt machine learning needs to be taught "intuition first, equations later", but this doesn't seem to be the norm with most learning sources.

I read [an article on Machine Learning Mastery](http://machinelearningmastery.com/4-steps-to-get-started-in-machine-learning/)
recently about getting started with machine learning.

The reason it stuck in my mind was that it discussed a way of learning
that I always felt was closer to me and a better way for me to learn,
yet I hadn't encountered many resources that teach machine learning that
way.

The article calls this approach "top down". I refer to the same approach
as "intuition first".

The problem is that most books and online courses, while technically
aimed at people with no background in machine learning, are usually too
maths-heavy too soon. Andrew Ng's excellent [Coursera machine learning course](https://www.coursera.org/learn/machine-learning) does a good job
of introducing the intuition behind the algorithms without getting into
too much detail about the underlying mathematics. However, especially in
the chapter about support vector machines, I felt there was still a need
to step away from the technical details a bit more.

There is a time and a place for deep dives into algorithms and maths,
but it's not at the start of your learning.

I know from experience that if I want to learn a new concept, and the
first thing I see is equations I'll be discouraged, because there's too
much to understand too soon. By teaching the ideas in an abstract way
first, you get a "feel" for the concept before you get into the
nitty-gritty implementation details.

Here's the idea of top down machine learning, quoted straight from the
article:

We can summarize this top-down approach as follows:

1.  Learn the high-level process of applied machine learning.
2.  Learn how to use a tool enough to be able to work through problems.
3.  Practice on datasets, a lot.
4.  Transition into the details and theory of machine learning algorithms.


I wholeheartedly agree with step 1 being the high-level process. You
want to know exactly what you're trying to achieve before you need to
formalise it mathematically.

The part I don't agree with is the order of steps 3 and 4. There is a
slight danger in doing things that way around.

If you learn the intuition and start practising on datasets without
knowing some more details you can get derailed, and it might be
difficult to "debug" any problems you encounter. As with any new
technique, superficial knowledge of it is fine at the start, but you
need to understand it in more depth if you want to actually use it on a
real problem.

This is what I propose instead, for an amended version of "top down"
machine learning.

1.  Learn the high-level process of applied machine learning.
2.  Try some toy examples, get your hands dirty.
3.  Transition into the details and theory of machine learning algorithms.
4.  Practise on lots of datasets. 

Not a big change, but the key difference is that you should understand
the theory in more detail before you spend lots of time practising.
Trying some toy problems before diving into the theory will help you put
the theoretical concepts into context.

Getting exposed to more theory is mostly for practical reasons, so you
understand things like:

-   **Normalisation** - does my data need to be normalised? If you
    understand the inner workings of a machine learning algorithm you'll
    intuitively know the answer rather than having to resort to trial
    and error.
-   **Metrics** - measuring success in machine learning is an important
    topic and you don't want to be using the wrong metrics to judge how
    well your algorithm is performing.
-   **Cross-validation** - this might be covered in the high-level
    process but the idea of training and test sets needs to be drilled
    home before you start getting too deep.


This might not work for everyone, the mathematically-minded could well
prefer an approach where they're given the equations first, but I
suspect they're the minority. If the imbalance is the way I perceive it,
then there does seem to be a disconnect between the way people learn and
the way machine learning is often taught.
