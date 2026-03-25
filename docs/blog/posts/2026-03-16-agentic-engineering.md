---
date: 2026-3-12 17:44:00
slug: agentic-engineering
draft: true
authors:
  - timvink
---

# Agentic engineering

potential new post?


Nate: Describes example of high-performer quitting company and building a prodcut with paying customers in 1 month. "How did we spend the last thirty years building organizations that make extraordinary people look ordinary?".  https://natesnewsletter.substack.com/p/executive-briefing-one-solo-founder?publication_id=1373231&post_id=190757490&isFreemail=true&r=7ekpeq&triedRedirect=true&utm_source=substack&utm_medium=email

"Every layer of review makes you 10x slower" https://apenwarr.ca/log/20260316. This rings so true.

<!-- more -->

## Building with AI: Agentic engineering

It’s incredibly exciting to pursue a flow of ideas so incredibly fast. It’s so much more fun to dive into complex intimidating topics and learn them from a patient expert that answers all your stupid questions until you *finally* understand. 

At the same time there's been legitimate concern about 'AI slop'. With AI everything becomes boring, average, predictable and mediocre. Code would have critical bugs and security flaws. But [as Simon Willison put it](https://simonwillison.net/guides/agentic-engineering-patterns/better-code/): "Shipping worse code with agents is a choice. We can choose to ship code that is better instead.". This new discipline is called *agentic engineering* or *harness engineering*.

It's a field that is rapidly evolving. For instance, you now have some organisations that deploy version-controlled skills across all their agents. This ensures AI uses up to date brand identity and process controls centrally. Many conventional wisdoms are changing. For example: *“Making imperfect decisions is no longer fatal. In fact, it can be productive. A flawed reference implementation provides better context than a pristine specification.”* (['zen of AI coding'](https://nonstructured.com/zen-of-ai-coding/)).

With agentic engineering, the bottlenecks are now frequently human coordination. The challenge now is to look how you can close manual loop. For example, you can have an AI agent access all the logs of ingestion jobs nightly and create a JIRA ticket if they fail. Then another agent is triggered that assesses whether the error is transient, or repairable. By the time you start the day with a coffee there is already a pull request waiting. CI is passing and the changes have already been reviewed by another agent. 

So the work is now creating these tight feedback loops, evaluating the work you're doing manually and seeing how you can automate it. All this means working at a higher abstraction level. It means learning to stop handholding. I've started marking tasks as done already after prompting them. I'm learning to prompt immediately instead of saving tasks. To let go of control in many places, while building strong control flows (preferably automated). It’s weird to work at such different speeds, going from super fast (agents) to super slow (human).

Some people are worried about skill atrophy. If you have a very smart friend who's willing to do all your homework.. you won't do well. To back that up: the recent paper [How AI Impacts Skill Formation, Shen, 2026](https://arxiv.org/pdf/2601.20245) finds that "AI use impairs conceptual understanding, code reading, and debugging abilities, without delivering significant efficiency gains on average". Even [Anthropic recently blogged](https://www.anthropic.com/research/AI-assistance-coding-skills) about this, saying: *"Cognitive effort — and even getting painfully stuck — is likely important for fostering mastery."*. The remedy is simple: you need to put conscious effort into understanding what you're building. You should use AI to learn about what you're building if you're pushing the frontier of your knowledge. And yes, that takes additional effort.

As [Nate Jones summarized](https://natesnewsletter.substack.com/p/cursors-coding-agents-solved-a-math): "The skill that survives this transition isn’t doing the work. It’s evaluating whether the work is correct."


## Other relevant links

- no cambrian explosion of software visible?! https://www.answer.ai/posts/2026-03-12-so-where-are-all-the-ai-apps.html