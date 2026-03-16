---
date: 2026-3-15 21:44:00
slug: thinking-big
authors:
  - timvink
---

# Thinking big

Remember February 2020, watching the covid virus spread overseas and wondering what would happen? Matt Schumer writes [something big is happening](https://shumer.dev/something-big-is-happening): *"I think we're in the 'this seems overblown' phase of something much, much bigger than Covid."* He's an AI developer and entrepreneur, talking about how shocked he is with the last few months of AI developments.

I no longer have to write code, instead I build on a higher abstraction level, describing in plain English what I want. I wrote about the tipping point for me last November ([My Opus Moment](./2026-01-11-my-opus-moment.md)). This new 'discipline' of writing software is being called ['*agentic engineering*'](https://simonwillison.net/tags/agentic-engineering/). But it's not just software that will be affected by these new AI models. I'm still recalibrating and wrapping my head around all the implications. This post collects some of my current thoughts.

<!-- more -->

## It's already here

It's not hype. It's not something that is about to happen. The technology *already works*. Most software engineers are not writing software by hand anymore. Two recent examples: Andrej Karpathy used [autoresearch to improve nanochat](https://github.com/karpathy/autoresearch), where AI was able to find significant improvements to his LLM training algorithm. Or Cursor who recently announced using AI to find a [novel scientific result in spectral graph theory](https://x.com/mntruell/status/2028903020847841336).

Keeping up with the developments is time consuming. Using AI is exhausting, with researchers dubbing the condition as [AI brain fry](https://edition.cnn.com/2026/03/13/business/ai-brain-fry-nightcap). 

We're already seeing a rapid acceleration in research and innovation. Even if AI development stops today and we are left with the current models, 2026 is still going to be wild.

## The economics are changing

Way back in 1937 Nobel-prize winning economist Ronald Coase published his paper *The Nature of the Firm, ‘Transaction Cost Economics’*. A corporation will continue to expand (bringing more functions "in-house") as long as the **internal coordination costs** are lower than the **external transaction costs**. Basically he said that using the open market isn't free. Every time you hire a freelancer or buy a part from a supplier, you incur costs:

- **Search and Information:** Finding the right person or price.
- **Bargaining:** Negotiating and writing a contract.
- **Enforcement:** Making sure they actually do what they said.

AI is changing this equation rapidly.

The **external transaction costs** are dropping. For example agents can do search and process information for you; the 'agentic web' is already being built. The [new WebMCP protocol](https://www.ivanturkovic.com/2026/02/15/webmcp-is-coming-how-ai-agents-will-reshape-the-web/#:~:text=This) is a proposed W3C standard already implemented in Chrome since last month. This lets websites expose structured tools directly to AI agents so they don't have to click around. It's a parallel web built for AI. A new [Agent Payments Protocol](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol) (AP2) was announced in September last year.

The **internal coordination costs** are *also* dropping. One example is that companies can deploy internal agents that know about all internal processes and systems. It's like having that helpful colleague sitting next to you who's been around for years and knows everything, who knows who to ask and in what system to make which request, and will do it for you real quick. All without maintaining a documentation jungle like confluence.

So the question is, which one drops more rapidly? Will we see larger or smaller corporations? One thing that hasn't changed is the cost of coordination between humans. It's still $\frac{n(n-1)}{2}$, where $n$ is the number of humans in a group. If developers are now 10x more productive, human coordination becomes even more of a bottleneck. My prediction is small teams $\gg$ large teams. I think we'll start seeing more very successful small teams. At the same time large companies can continue to do very well.

## New business opportunities

In the business world, a defensible moat is a distinct, sustainable advantage that protects a company from its competitors (the term was invented by Warren Buffett). If software/intelligence is so much cheaper, the moat shifts toward distribution, data, brand, network effects, regulation, and ecosystem integration. If your moat was built on high quality software, the bar has been raised significantly.

Paul Graham in his essay [Brand Age](https://paulgraham.com/brandage.html) states "Brand is what's left when the substantive differences between products disappear". If software is solved, what's left is brand. And brand is "not the clean kind of constraint that generates good things". To prove this point, Paul compares the [Vacheron Constantin 18k](https://goldammer.me/products/vacheron-constantin-18k-white-gold) watch (1960s, competing on quality) with the [6300/400G-001](https://www.patek.com/en/collection/grand-complications/6300-400g-001) 2022 'brand-age' watch. Yes, 'brand' watch is big, ugly and expensive. How do you escape brand competition? Paul: "Follow the problems." He argues most golden ages were found by smart people following interesting problems.

AI can do much more than just write software. Companies need to rethink their whole setup. You need to organize so you have loops where you can apply intelligence (models) + memory (RAG,notes) + retrieval (agentic search, webfetch, db access) and execution (code, automation, payment). It means companies have the opportunity to rethink processes, team structures and decision-making. It's Goldratt's old [Theory of Constraints](https://en.wikipedia.org/wiki/Theory_of_constraints) applied to modern company processes. Identify the bottlenecks in internal processes, find out how to best apply AI, repeat.

There is fearmongering about a "SaaS apocalypse"; that software as a service will end because the cost of software will approach zero. You hear stories that investors are selling software stocks and [1T dollars of value has been wiped](https://www.mindset.ai/blogs/the-saas-apocalypse-what-happens-when-creation-costs-collapse-to-zero) from the stock market. However, if software costs 10x less, there will be so many new opportunities opened up that were not feasible before. Demand for software (and software engineers) could actually go up. If you build more highways to fight traffic jams, total traffic will increase because it becomes more attractive.

The second-order effects of cheap software are hard to predict. Thorsten Ball has [a nice analogy](https://registerspill.thorstenball.com/p/joy-and-curiosity-78): If we could make oil from rainwater all of a sudden, a first-order effect is that all oil reserves lose their value. Second-order effects on energy policy, geopolitics, plastics, chemicals and fertilizers — those are much harder to predict. For example: the AI boom has made some hardware more expensive: RAM costs have [increased 500%](https://www.tomshardware.com/pc-components/dram/cyberpowerpc-announces-ram-price-hikes-coming-to-the-u-s-and-the-uk-starting-december-7th-prebuilt-proprietor-cites-500-percent-increase-in-memory-cost) and [Mac Mini's are selling out](https://www.techradar.com/computing/macs/mac-mini-shortages-are-starting-to-happen-and-the-openclaw-ai-boom-is-a-key-reason).

## Be more ambitious

I'm left with the feeling that there are more business and innovation opportunities than ever before.

The impact on jobs has many people worried. We've already seen organizations like [Block cutting half of their workforce](https://futurism.com/artificial-intelligence/jack-dorsey-block-layoffs-ai) due to AI. But at the same time companies like Whoop are [doubling their employee count](https://www.whoop.com/nl/en/press-center/whoop-announces-2026-hiring-surge-adding-more-than-600-roles/) because of AI. Either way, the [growth mindset](https://en.wiktionary.org/wiki/growth_mindset) is the right one: You should do *dramatically* more work, rather than focus on doing the same amount with fewer people. These are the companies that will win. 

Domain expertise is more important than ever. Do not limit yourself to what you personally know. Your conceptual understanding transfers more than you think. Simon Willison phrased this idea nicely: [Hoard things you know how to do](https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/).

In this new world, Peter Thiel's book [Zero to One](https://en.wikipedia.org/wiki/Zero_to_One) is more relevant than ever. It applies to innovation within companies and for new companies. He argues you should:

1. *Target a Small Market*: Start with a very small, specific niche where you can provide a concentrated solution. 
2. *Dominate that Niche*: It is much easier to dominate a small market than a large one.
3. *Scale Up*: Once you own that niche, you gradually expand into adjacent, broader markets.

Peter summarized this idea eloquently: "Competition is for losers." We now can and should tackle bigger and harder problems. 

It's not a winner-takes-all world. It's not too late, it's early. The future is bright, not gloomy. If you have domain expertise, if you have a problem you understand deeply: build. Be bold, be ambitious!