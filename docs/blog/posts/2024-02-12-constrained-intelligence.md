---
date: 2024-02-12 9:00:00
slug: constrained-intelligence
authors:
  - timvink
---

# Thoughts on Constrained Intelligence

In my career I've focused mostly on applying what is now called 'traditional machine learning': regression, classification, time series, anomaly detection and clustering algorithms. You could frame machine learning as applying an algorithmic 'constrained intelligence' to a specific business problem. The challenge has always been to 'unconstrain the intelligence' (f.e. by tuning hyperparameters) and to further specify the business problem (proper target definition, clean data, proper cross validation schemes). The advent of large language models is starting to flip the equation; from 'unconstraining' intelligence to 'constraining' it instead.

<!-- more -->

## Large language models as unconstrained intelligence

Large language models can be seen as having 'world knowledge'. They are generic models that have been trained on 'everything' (high quality text data). I like how [François Chollet](https://twitter.com/fchollet) (creator of Keras) puts it:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">My interpretation of prompt engineering is this:<br><br>1. A LLM is a repository of many (millions) of vector programs mined from human-generated data, learned implicitly as a by-product of language compression. A &quot;vector program&quot; is just a very non-linear function that maps part of…</p>&mdash; François Chollet (@fchollet) <a href="https://twitter.com/fchollet/status/1709242747293511939?ref_src=twsrc%5Etfw">October 3, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

So a (very) large language model is just a huge repository of many millions of vectors programs containing generic world knowledge. A prompt would select one of the vector programs. Prompt engineering can thus be seen the effort to constrain all that 'intelligence'.

The overlap of machine learning with LLMs is becoming larger. You can use an LLM to determine if an email as 'spam' or 'not spam' (classification), which department should handle an incoming email (multi-class classification), or measuring the quality of a CV (ordinal classification or regression). So for a given business problem, is it easier to 'constrain the intelligence' of a large language model, or to 'unconstrain the intelligence' of a machine learning model? 

## The limits of prompt engineering

You would think that making LLMs more stupid (constraining intelligence) is a simple matter. It's not. A couple of arguments:

- A prime example is *prompt injection*, where a user inserts [malicious inputs that order the model to ignore its previous directions](https://twitter.com/goodside/status/1569128808308957185?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1569128808308957185%7Ctwgr%5E6dee103c38bb1042a68022a3a24a0e4b0a16b233%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fsimonwillison.net%2F2022%2FSep%2F12%2Fprompt-injection%2F) . For more background, see the excellent blogposts by [Simon Willison](https://simonwillison.net/) on the topic (f.e. [You can't solve AI security problems with more AI](https://simonwillison.net/2022/Sep/17/prompt-injection-more-ai/) and [I don't know how to solve prompt injection](https://simonwillison.net/2022/Sep/16/prompt-injection-solutions/)).
- Prompt engineering is a heavily researched field and writing a good prompt is not straight forward; it's a trial-and-error process with quality metrics that are very hard to define. OpenAI has a [prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering) containing many of the lessons learned, showing there are many subtleties.
- There are many funky edge cases and tricks (see [this overview](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)). For example changing `Q:` to `Question:` is found to be helpful. ([Fu et al. 2023](https://arxiv.org/abs/2210.00720)). Prompting using Chain-of-thought (CoT) improves complex reasoning ([Wei et al. 2022](https://arxiv.org/abs/2201.11903)). If you tell an LLM that it's december holiday season, it will reply with more brevity because it 'learned' to do less work over the holidays ([source](https://t.co/mtCY3lmLFF))

A funny example where an LLM failed to be just a helpful chatbot and started giving away cars:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I just bought a 2024 Chevy Tahoe for $1. <a href="[https://t.co/aq4wDitvQW](https://t.co/aq4wDitvQW)">[pic.twitter.com/aq4wDitvQW](http://pic.twitter.com/aq4wDitvQW)</a></p>— Chris Bakke (@ChrisJBakke) <a href="[https://twitter.com/ChrisJBakke/status/1736533308849443121?ref_src=twsrc^tfw](https://twitter.com/ChrisJBakke/status/1736533308849443121?ref_src=twsrc%5Etfw)">December 17, 2023</a></blockquote> <script async src="[https://platform.twitter.com/widgets.js](https://platform.twitter.com/widgets.js)" charset="utf-8"></script>

All this goes to show that constraining these 'intelligent' generic large language models is *challenging*. Just like reducing the constraints of the limited intelligence of traditional machine-learning models is very challenging. Can we learn something from both approaches; is there something in the middle?

## Where LLMs meet traditional ML

It's well established that traditional ML algorithms are still the undisputed king for tabular data when compared to deep learning based approaches ([source](https://gael-varoquaux.info/programming/people-underestimate-how-impactful-scikit-learn-continues-to-be.html)). They are likely to capture most of the signal present in the data (see my other post [Is XGBoost all we need?](https://timvink.nl/blog/is-xgboost-all-we-need/)). Many real world ML problems involve some level of predicting human behaviour and/or randomness. Adding world knowledge won't add much — we won't be seeing LLM-based classifiers and regressors very soon.

The breakthrough with LLMs was based on the scale of the data used. Trained on generic data (many different types of texts), the LLMs were then able to solve domain-specific problems (questions in prompts). This lesson; that generic models outperform specific models; seems to apply to machine learning as well. In businesses the same model is often rebuilt for each region or product or customer group separately. A single, larger, generic model however often outperforms the more specific ones. A series of experiment in the blogpost [The Unreasonable Effectiveness of General Models](https://towardsdatascience.com/the-unreasonable-effectiveness-of-general-models-b4e822eaeb27) seems to hint at the direction also.

## Conclusions & thoughts

So an LLM is just a specific type of generic model for text. And perhaps we can't properly constrain them because they are not intelligent at all. Perhaps *compression is all there is*:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Based on our latest study: <a href="[https://t.co/yltTHPcPVW](https://t.co/yltTHPcPVW)">[https://t.co/yltTHPcPVW](https://t.co/yltTHPcPVW)</a>, compression seems to be all there is in current AI systems, including GPT-4. The remaining question is: Can compression alone lead to general intelligence or even consciousness? My bet is a clear NO.</p>— Yi Ma (@YiMaTweets) <a href="[https://twitter.com/YiMaTweets/status/1727544356620652984?ref_src=twsrc^tfw](https://twitter.com/YiMaTweets/status/1727544356620652984?ref_src=twsrc%5Etfw)">November 23, 2023</a></blockquote> <script async src="[https://platform.twitter.com/widgets.js](https://platform.twitter.com/widgets.js)" charset="utf-8"></script>

