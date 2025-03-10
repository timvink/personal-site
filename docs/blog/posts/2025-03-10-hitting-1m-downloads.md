---
date: 2025-03-10 22:00:00
slug: hitting-1m-downloads
authors:
  - timvink
---

# Lessons learned after hitting 1M downloads/month

I hit that magic 1 million downloads/month milestone for one of the first open source projects I built: [mkdocs-git-revision-date-localized-plugin](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin). This post reflects on what I’ve learned maintaining that package since the first release end of 2019.

![1M downloads/month](../../assets/images/1Mmonth.svg)

<!-- more -->

For context, [mkdocs](https://www.mkdocs.org/) is a static site generator that can build HTML websites from markdown files.`git-revision-date-localized` is a plugin that extracts from `git` the last revision date of a markdown file and displays it at the bottom of the site’s page.

## Lesson 1: At scale simple things become hard

The entire plugin is basically a `git log` call. I had never expected something as simple as that to be hard. But at scale there are new edge cases. Some examples:

- Other plugins move, rename, edit or even generate new files. So things the order of execution of plugins start to matter. Compatibility with the plugin ecosystem meant more work building, testing and responding to issues
- Some websites are huge and involves 1000s of markdown files. Parallel processing of `git log` operations helps, but that means you’re processing files *before* they might be modified or moved, which means you need to deal with fallbacks also
- locale are tricky. There are many different places you can define them, and there are difference between which locales are supported by upstream dependencies (`babel` and `timeago`)

I even stumbled across a bug in `git` itself. I determine the *creation date* of a markdown file using more or less a `git log --follow` command. Turns out if you commit an empty file, the `--follow` path will break and go off track. This [blogpost has details](https://blog.plover.com/prog/git-log-follow.html), but I was not expecting having to read about git internals when I started working on this plugin.

## Lesson 2: Huge respect for open source maintainers, it’s a burden

When something you’ve built is used by so many others, you feel responsible. Especially when there is something that is broken. And even more so when people contribute time and effort into a pull request that needs a review. And then even more when I receive a couple of coffees per month (which is much appreciated dear [sponsors](https://github.com/timvink)!).

But fixing bugs, looking into issues, reviewing pull requests, they often require you to dive into the details again, or at least do a context switch. Between a busy job, family life, friends and other hobbies, there is not always enough time or energy left. And you don’t always feel like doing more programming work in your free time. I have the additional ‘problem’ of having creating 6 popular [mkdocs](https://mkdocs.org/) plugins. It’s hard to walk away and start ignoring the project. So at times it felt like a burden, and there was some feelings of guilt.

Now my little plugin doesn’t have *that* much scale, or any downstream dependencies. And I am not going to work on the plugin if I don’t feel like it. But this journey has just increased my respect level for open source maintainers so much more.

## Lesson 3: The Github community is generally a welcoming place

It’s been great to interact with other talented developers and design solutions together. I’ve read some accounts where maintainers are mistreated and people being disrespectful, but I’ve been lucky enough not to see those interactions.

Yes, it was surprising that some people decide they can lookup your personal email and reach out to ask for (free!) support for their (corporate!) work. And some people posting issues are very new to the ‘software world’ of providing proper small reproducible examples with their system information.

But people are generally very grateful and understanding — even when I respond to issues or PRs many months late 😃 The fact that the plugin has `31` contributors shows this; it’s really a community effort of people finding problems and solutions together.

## Lesson 4: Unit tests are awesome

Code always has had something magical to me. You define the logic once, and if the system environment is stable, it will keep working, even when you’ve long forgotten how it works.

Unit tests really give peace of mind that when you change something, that it will keep working. And when you *schedule* those unit tests to run once every week (because mkdocs or other plugins might change), it really helps with letting things go.

The plugin has been remarkably stable over the past 5 years, with only edge cases and minor new features being added. Maybe not a lesson but a confirmation then; *unit tests are awesome*.