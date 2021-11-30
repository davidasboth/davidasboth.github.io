Title: Was FiveThirtyEight Just Wrong?
Date: 2016-11-09 15:44
Author: david
Slug: blog/was-fivethirtyeight-just-wrong
url: blog/was-fivethirtyeight-just-wrong
save_as: blog/was-fivethirtyeight-just-wrong/index.html
Status: published

I have some brief thoughts about the outcome of the US election from an
entirely data science perspective. It's hard to remain objective and
have a scientific hat on when it comes to political events, but I never
intended this blog to be a place to discuss political opinion. Instead,
I want to look at this election outcome as an opportunity to talk about
probabilistic forecasts.

[FiveThirtyEight](http://fivethirtyeight.com/) tracked many polls over
time to forecast the probability of the two candidates. These fluctuated
quite a bit, but in the end their final forecast was an over 70%
probability of a Clinton win.

So was their model *wrong*?

Funnily enough it was Nate Silver himself who, in his book, talked about
how we evaluate a probabilistic forecast, his example being the weather.
In the case of the weather, this is the question:

Someone makes a forecast that tomorrow it will rain with a probability
of 30%. It rains tomorrow. Was the forecast correct?

The key idea here is that in instances like this the standard notion of
"accurate" doesn't hold. You simply can't evaluate the model based on a
single data point, unless its prediction was a 100% probability. That's
because the model isn't designed to make a single prediction. In the
case of the weather, forecasts are made multiple times a day, so very
quickly you have a whole set of "predictions" and true outcomes.

From that you now **can** evaluate the model.

When they say the probability of rain is 30% it doesn't just mean that
it's unlikely to rain. It also means that out of all the times they
predict 30% it will end up raining 30% of the time; to evaluate it
therefore requires multiple similar predictions. For example, after a
hundred 30% predictions, if it only rained on two occasions it's obvious
the model was too pessimistic (assuming you treat rain as a negative
outcome).

Then what about an event as rare as a general election?

That's a harder question and one where [there are disagreements](https://twitter.com/nntaleb/status/762033443932934144).

Clinton lost the electoral vote but appears to have won the popular vote
- an outcome FiveThirtyEight estimated to be around 10% likely. It was
explicitly covered by the forecast, which simply said that it's a rare
event, but still not an implausible one. Again, it is hard to quantify
whether that 10% was correct or not.

Ultimately in cases like this there are too many variables to be able to
make a definitive prediction. It is more worthwhile to think of it as a
statement of the probability distribution of all possible outcomes
rather than a means to actually predict who will be President. Of course
this probability distribution can be wrong, it's just not apparent how
to evaluate this.

I must admit I don't know that much about the technical details of such
an evaluation.

However, I am interested in finding out, so I will go away and do some
research and report back later this month in a future blog article.


Footnote: This was the 9<sup>th</sup> entry in my [30 day blog challenge](/blog/30-posts-in-30-days/).
