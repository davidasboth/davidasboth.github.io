Title: Markov Chains for Text Generation
Date: 2016-11-12 22:09
Author: david
Slug: markov-chains-for-text-generation
Status: published
Summary: Markov chains are a popular way to model sequential data. I want to run through an implementation where I generate new songs based on lyrics by Muse.

Markov chains are a popular way to model sequential data. They form the
basis of more complex ideas, such as Hidden Markov Models, which are
used for speech recognition and have applications in bioinformatics.

Today I want to run through an implementation of Markov chains for
generating text based on an existing corpus. First of course we need to
understand what Markov chains are before we can implement one.

 

## The Intuition


I've talked about [intuition-first machine learning](/intuition-first-machine-learning)
before, so I'll start with the intuition. The first thing we need to
know about is what a Markov chain consists of, then we need to define
the Markov assumption.

### States and Transitions

In a Markov chain we are assuming our sequence is made up of **discrete states**. That is, every item in the sequence is one of a finite set of
possible values. In text, the states could be every letter of the
alphabet and our punctuation marks.

We assume that for every item in the sequence, there is a probability
associated with what the next value will be or, more formally, what
state we will transition to. This is called the **transition probability**.

This is different between pairs of states, so the probability of going
from state A to state B might be different than going from B to A. There
is also a probability of staying in the same state.

However, it would be too difficult to attempt to model the transition
probabilities if we always used the entire sequence. This would be like
trying to predict the last word in War and Peace and having to take into
account every single word that came before it.

To make this easier, we make what's called the Markov assumption.

### The Markov Assumption

The Markov assumption is when we assume the Markov property to be true.

The Markov property (of a sequence) is typically formulated like so:

*The future is independent of the past, given the present.*

That sounds a bit like an old proverb but it's a simple concept.

If a sequence has the Markov property it means that the value of the
sequence at the next step **depends only on the value at the past $n$ steps**. The value of $n$ (how far back we assume we need to go) is
called the **order** of a Markov chain.

So a second-order Markov chain is one where we use the current and the
previous value to predict the next value. We are assuming that it does
not matter what the rest of the text was before the previous word, we
only need the current word and the one before it.

In effect, the Markov chain has no "memory" beyond the last $n$ steps.

The Markov assumption simply states that we believe this Markov property
to hold for a given sequence.

This is a simplifying assumption that means it is much easier to compute
these Markov chains at the cost of some complexity and accuracy. However
simple this assumption may feel, it performs remarkably well.

### The Markov Assumption in Text

Let's look at an example. What does this Markov assumption look like for
text? We'll work with second-order Markov chains, as defined above.

Let's imagine that our sequence is this string of animals:

cat cat cat dog cat cat cat fish cat dog fish cat dog dog cat

What we say if we assume the Markov property is that our prediction of
the next word in the sequence depends only on the last two words: dog
cat.

How do we use that for predicting?

We need to calculate the transition probabilities based on the text that
we have, then assume that going forward those probabilities are what
decide our next words.

Because we are using second-order Markov chains, we calculate the
probabilities of each word following a two-word pair. To do this, we
simply count what percentage of the time a word appeared after each
possible pair.

If we take a single example, "cat cat", we'll see that this pair was
followed by "cat" twice, "dog" once and "fish" also once. That means if
we're in the state "cat cat" the next word will be "cat" with a 50%
probability, or "dog" or "fish" with 25% probability each.

## The Code

That's enough intuition, let's get into the code.

I've scraped the lyrics to all songs written by [Muse](http://muse.mu/)
and we'll use this as our corpus. We'll use it to generate some more
text, specifically a new Muse song.

### Preparation

The first step is to read the file in and clean it so we have a sequence
of words and new lines. I won't go into the details, you can see how the
cleaning is done in the accompanying Jupyter notebook. I also included
the code I wrote to scrape the lyrics in the first place, but going
through that is optional as I'll also include the final source file.

### Training

When we do the "learning" for a Markov chain, we're just identifying all
unique triplets of words, and creating our transition probabilities
using the first two words as the current state and the third as the next
state.

As an implementation detail, I've made the transition probabilities a
Python dictionary where each key is a unique word pair, and the value is
a list of all the words that have ever followed that pair. I haven't
even explicitly calculated the probabilities, but instead included each
word as many times as it appears.

Our "cat cat" example above would look like an entry in a Python
dictionary like this:

    :::python
    { "cat cat": [ "cat", "cat", "dog", "fish" ] }

To generate our transition probabilities we use a helper function:

    :::python
    def generate_triples(word_list):
        d = {}
        # loop through the text and generate triples
        for i in range(len(word_list)):
            if i == 0 or i == len(word_list) - 1:
                continue
            else:
                if (word_list[i-1], word_list[i]) in d:
                    d[(word_list[i-1], word_list[i])].append(word_list[i+1])
                else:
                    d[(word_list[i-1], word_list[i])] = []
                    d[(word_list[i-1], word_list[i])].append(word_list[i+1])
        return d

So given a list of words (our entire text) we go through it word by
word, creating dictionary entries for every pair we encounter, and
adding the next word into the list associated with that pair.

To then simulate the probability of choosing a word given a pair of
words, we randomly sample from the list associated with that pair.

This function gives us the next word each time. This is part of a Markov
class, where self.words is our previously trained dictionary.

    :::python
    def get_random_word(self, phrase=None):
        if phrase:
            # find a phrase from the list of words associated with the last two words in the supplied phrase
            phrase_words = [x.lower() for x in phrase.split(' ')]
            if len(phrase_words) > 1:
                if (phrase_words[-2], phrase_words[-1]) in self.words:
                    past = self.words[(phrase_words[-2], phrase_words[-1])]
                else:
                    past = self.words[random.choice(list(self.words.keys()))]
            else:
                past = self.words[random.choice(list(self.words.keys()))]
        else:
            # no phrase supplied, return a word from our dict at random
            past = self.words[random.choice(list(self.words.keys()))]
        return random.choice(past)

The function will look at a phrase, check if it is at least two words
long and for the last two words, it finds the appropriate dictionary
entry and samples from the list associated with that pair.

So if we gave it "banana cat cat" it would look up "cat cat" in the
dictionary and sample from the list.

**Remember**: the words in the list implicitly represent the transition
probabilities. Because we have "cat" twice out of four words in our list
we've defined the transition probability as 50%.

To generate the text we can then either give it some text to start it
off, or let it start with a random pair.

I've added some structure so that the code creates a song title, a
chorus and a couple of verses.

It came up with this:

> hear me moan
>
> Verse 1
>
> you are just  
> too much attention  
> and its gonna be  
> show me mercy can someone rescue me  
> make me agitated
>
> Chorus
>
> escaped your world  
> no one is crying alone  
> i wont let them hurt  
> hurting you no
>
> Verse 2
>
> you know what youve done  
> bring me peace and wash away my dirt  
> spin me round and have me to
>
> Chorus
>
> escaped your world  
> no one is crying alone  
> i wont let them hurt  
> hurting you no

I dare say Matt Bellamy couldn't have written it better himself.

Here's the [associated Jupyter notebook](https://github.com/davidasboth/blog-notebooks/blob/master/markov-chain-muse-lyrics/Markov%20Chain%20Muse%20Lyrics.ipynb).
I've also previously published the code as more of a plug and play
library, which [you can find here](https://github.com/davidasboth/markov-chain-for-text).

### Next Steps

We could improve this code by doing any of the following:

-   Experiment with different orders for the Markov chain
-   Giving it more data is never a bad idea, you could mash Muse's
    lyrics up with another artist
-   You could try a character-level Markov chain to see if it would
    generate meaningful text that way, although for that you might want
    a [Recurrent Neural Network](https://github.com/karpathy/char-rnn)
-   Adding support for punctuation

## Further Reading

If you want to learn more about Markov chains, and even see them 'in
action', this is [a great resource](http://setosa.io/ev/markov-chains/)
to start with.

I glossed over a lot of the maths behind the algorithm, but if you're
interested you could [start here](https://www.youtube.com/watch?v=WUjt98HcHlk).
