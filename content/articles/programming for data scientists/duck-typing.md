Title: Duck Typing
Date: 2016-11-14 16:05
Author: david
Tags: python
Slug: duck-typing
Status: published
Summary: My first attempt to bridge the gap between the two disciplines of programming and data science, by talking about programming concepts useful for data scientists, and vice versa. Today: duck typing.
Alias: /2016/11/14/duck-typing

In an attempt to bridge the gap between the two disciplines of
programming and data science I will occasionally talk about programming
concepts useful for data scientists, and vice versa.

Today I want to discuss **duck typing**.

Duck typing is a concept that originated in the Python community. It is
a way of checking an object's type not by testing its type directly, but
testing its **methods**.

The idea is based on something called [the duck test](https://en.wikipedia.org/wiki/Duck_test). You've probably heard it
before:

> "If it looks like a duck, swims like a duck, and quacks like a duck,
> then it probably is a duck."

How does this relate to programming?

Well, Python is a dynamically-typed language. That means that the types
of objects (whether they're integers, strings etc.) is checked at
**runtime, not compile time**.

A variable is allowed to have different types at different points of a
program's execution. This is perfectly valid:

    :::python
    my_variable = 42
    # do stuff with my_variable...
    # and later...
    my_variable = "now it's a string!"

You can't do this in a statically-typed language. Once you declare a
variable as a certain type, it stays that way. Take this example in C#:

    :::c#
    int my_variable = 42; // explicitly declare an integer
    // do stuff
    my_variable = "can I be a string?"; // this will produce a compiler error

*Actually there are [dynamic types in C\#](https://msdn.microsoft.com/en-us/library/dd264736.aspx) but we'll just gloss over that.*

The point is you can be quite liberal with types in Python.

You can take this one step further with duck typing.

## Duck Typing in Python

Say you have a function that makes a duck quack, like this:

    :::python
    def make_it_quack(something_duck_like):
        something_duck_like.quack()

We've taken an object in and called its quack method. We don't care what
type of object this is, only that it is able to quack. So if we had a
"real" duck and an impostor, they'd both work with this method:

    :::python
    class Duck(object):
        def quack(self):
            print("Quack quack")

    class Ferret(object):
        # ferrets can't normally quack, but this one's cunning
        def quack(self):
            print("Quack quack")

    donald = Duck()
    fred = Ferret()

    make_it_quack(donald)
    make_it_quack(fred)

Both of these will produce the output "Quack quack" because all we did
was make it quack. If it can do that, then as far as we're concerned
it's a duck.

## Duck Typing in Data Science

This is a concept that can be quite useful in data science.

For example, imagine that you have your own implementation of a machine
learning algorithm but want to use a lot of the goodness built in to
scikit-learn.

Well, you know how all scikit-learn implementations have a fit and
predict function?

You can create your own object and make use of duck typing by "quacking
like a scikit-learn duck".

First, create a class that has fit and predict methods:

    :::python
    class MyFakeClassifier():
        def fit(self, x, y):
            print("Working VERY HARD...")
        
        def predict(self, x):
            # predict 0 no matter what
            return [0 for item in range(len(x))]

Now you can fit and predict the same way as you could with, say, a
Random Forest.

Imagine you already wrote a small function that takes in a machine
learning classifier, does a train-test split and gets the accuracy and
confusion matrix of the predictions.

    :::python
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, confusion_matrix

    # write a function to give us a train-test accuracy score
    def get_accuracy(model, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print("Accuracy: {}\n{}".format(accuracy_score(y_test, y_pred),
                                        confusion_matrix(y_test, y_pred)))

We can use this for a built-in classifier, but also our new estimator:

    :::python
    from sklearn.datasets import load_iris
    from sklearn.ensemble import RandomForestClassifier

    iris = load_iris()
    X = iris.data
    y = iris.target

    rf = RandomForestClassifier()
    random_model = MyFakeClassifier()

    # we can get the accuracy of our Random Forest
    get_accuracy(rf, X, y)
    # and our new model!
    get_accuracy(random_model, X, y)

There you have it. All we had to do was create something that can "fit"
and "predict" and Python doesn't need anything else for it to work.

Note: to use the full range of scikit-learn functions with your own
estimator, you should [do it properly](http://scikit-learn.org/stable/developers/contributing.html#rolling-your-own-estimator),
but the point is you can do a lot of it by duck typing.

Here's [the associated notebook](https://github.com/davidasboth/blog-notebooks/blob/master/duck-typing/Duck%20Typing.ipynb).

Happy quacking!
