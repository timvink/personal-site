---
date: 2026-02-11 17:44:00
slug: digital-sovereignty
authors:
  - timvink
---

# What you can do for European Digital Sovereignty

We pay for insurance but hope we never need it. It's the same with digital sovereignty: we should never need it, yet we really can't go without. 
For me, the urgency of independence from American technology really hit home in Jan 2026 when [Trump imposed tariffs](https://www.dutchnews.nl/2026/01/trumps-greenland-tariffs-are-blackmail-says-dutch-minister/) on the Netherlands for sending troops to Greenland to prepare an Artic NATO defense mission. America threatening to take possession of an allied, sovereign country by military force really shook Europe awake, and rightly so. Although earlier warning signs were already clearly there. Like when in May 2025 the chief prosecutor for the International Criminal Court (based in The Hague) [lost access to his Microsoft email](https://www.dutchnews.nl/2026/01/trumps-greenland-tariffs-are-blackmail-says-dutch-minister/) after Trump imposed sanctions. Or maybe already back in 2018 when the US CLOUD Act was enacted, that obliges US companies to provide data *"in their possession, custody, or control"*, regardless of where that data is stored. So while Amazon might announce products with names like [AWS European Sovereign Cloud](https://www.aws.eu/), they are not sovereign because [they do not have jurisdictional immunity](https://fabricemonnier.substack.com/p/aws-european-sovereign-cloud-marketing).

<!-- more -->

## European digital sovereignty

In October 2025 Francesca Bria published an essay called ["Reclaiming Europe’s Digital Sovereignty"](https://www.noemamag.com/reclaiming-europes-digital-sovereignty/). She's clear on what the stakes are: *"Europe faces a choice: build sovereign technological capacity or accept digital colonization"*. But she's also pro-active and the initiator of the [EuroStack Project](https://www.euro-stack.info/), that offers innovative European technology for all layers of the digital stack. The EuroStack project is backed by well-known European companies like [HuggingFace](https://huggingface.co/) (France), [Mistral](http://mistral.ai/) (France), [ASML](https://www.asml.com/) (Netherlands) and [SAP](https://www.sap.com/) (Germany).

European projects like EuroStack are promising for digital sovereignty for governments and public services. Migration won't be easy, but there are already microsoft-alternatives like [LaSuite](https://lasuite.numerique.gouv.fr/en), [openDesk](https://www.opendesk.eu/en) and [NextCloud](https://nextcloud.com/). But for private individuals I was under the *mistaken* impression that there are no good alternatives for scale and quality of the American 'Big Tech' digital services. I was very wrong; there are very strong and well designed alternatives available. As Francesca put it: *"The real test isn’t technical capability — it’s whether Europe can secure adoption at scale and turn these building blocks into a coherent ecosystem before dependencies become irreversible."*. And that's where choices by individuals make a difference.

## What can you do right now

### Stop using WhatsApp, use Signal instead

While WhatsApp encrypts the content of your messages, it collects a massive amount of metadata: who you message, how often, your IP address (location), your device signal, and your contact list. This data is shared across the Meta ecosystem (Facebook, Instagram) to build a detailed profile of your life. Think you have nothing to hide? [Yes, you have stuff to hide!](https://jacquesmattheij.com/if-you-have-nothing-to-hide/). As an alternative, I recommend [Signal](https://signal.org/), which uses a "Zero Knowledge" architecture: Signal doesn't even know who is messaging whom. The only information Signal stores is the date you registered and the last time you connected to the server. It's encryption is even [safe for a post-quantum world](https://signal.org/blog/spqr/?utm_source=substack&utm_medium=email), when quantum computers become sufficiently powerful to decrypt many current encryptions (the *'cryptocalypse'*).

Signal has a lot going for it. It's fully open source. It's a non-profit. It has no shareholders, no advertisers, and no incentive to track you. It exists solely to provide secure communication. And it has the *network effect* -- in the Netherlands where I live a lot of my contacts are already on signal. But the company is American. Signal’s President, Meredith Whittaker, has repeatedly stated that Signal will shut down operations in any country that passes laws requiring "backdoors" or the scanning of private messages. Signal’s stance is that because the app is End-to-End Encrypted (E2EE), it doesn't matter where the headquarters is.

### Switch to a European email provider

Yes. This one hurts. And it's a lot of work. Hear me out.

I've been using Google's Gmail for more than 20 years. But not only is my data being used for ads, I don't want to risk losing access to such a critical service. We're in luck as there is a really good alternative to Gmail, Hotmail, Outlook, etc: [Proton Mail](https://proton.me/mail). It's European, has a generous free tier, has great design, is open source and it's fully encrypted. The Proton company recently [became a non-profit foundation](https://proton.me/blog/proton-non-profit-foundation) to *'serve the interests of all society'*.

Moving from email provider *is* a bit of a pain. Migrating over all your emails and contacts, and setting up an auto-forwarding rule on your old email is [just a couple clicks](https://proton.me/easyswitch). But you'll need to update all your digital accounts to use your new email address. Couple of tips:

- Update all your main accounts in one go, and then update remaining accounts as you receive emails from them.
- You should absolutely use a different password for every single account you have. If you're not: take action! Install a password manager (tips: [proton pass](https://proton.me/pass) or [vaultwarden](https://github.com/dani-garcia/vaultwarden)), update your passwords, sleep peacefully.
- If you have a domainname, you could setup a custom email to ensure this is the last email switch you'll ever make.
- Take ownership of your old data. You can download a copy of your entire email history using export services like [Google Takeout](https://takeout.google.com/). I'm watching new projects like [msgvault](https://www.msgvault.io/) (from Wes McKinney, creator of `pandas`) that help manage, sync and search your message history locally.

### Start using Firefox

The problem here is *Engine Monopoly*: Most of the world's browsers run on Chromium, an open-source engine controlled primarily by Google. When you use Chrome, you are reinforcing a "monoculture" where Google decides how the web work. One example is their controversial "Privacy Sandbox" which replaces third-party cookies with Google-controlled tracking. That [initiative was killed](https://proton.me/blog/privacy-sandbox-dead) after immensive pressure from regulators. Chrome has [>70% market share](https://gs.statcounter.com/browser-market-share) and is made by Google, an advertising company. Chrome is designed to feed Google’s advertising machine. Even with privacy settings turned on, Chrome collects significant metadata (telemetry) about how you use the browser, which is stored on US servers. 

[Firefox](https://www.mozilla.org/firefox/) is the obvious alternative. It's open source, backed by the non-profit Mozilla Foundation, built on the open-source [Gecko](https://firefox-source-docs.mozilla.org/overview/gecko.html) rendering engine, and has strong privacy defaults like [Enhanced Tracking Protection](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop). It supports powerful ad blockers like [uBlock Origin](https://addons.mozilla.org/firefox/addon/ublock-origin/), which Chrome is actively crippling. Firefox also syncs bookmarks and history across devices with an encrypted Mozilla account. Switching is easy: Firefox can [import your bookmarks and history](https://support.mozilla.org/kb/import-data-another-browser) from Chrome automatically. While you're at it, consider switching your default search engine to [DuckDuckGo](https://duckduckgo.com/) or [Startpage](https://www.startpage.com/) (a Dutch company that serves Google results without the tracking).

### Use a different authenticator app

All your important accounts have two-factor authentication (2FA) set up... right? If not, get that in order! A simple username/password is too insecure and your digital identity too important.

That 2FA app holds the keys to your digital identity. If you use an American Authenticator app like the one from Google or Microsoft, you risk digital lockout. Switch to a secure European one, and make sure you have a regular secure backup as well as a recovery procedure (like for when your phone breaks). All this sounds complicated but you'll be up and running again in 5 minutes. I personally recommend [Proton Authenticator](https://proton.me/authenticator) (free). 

If you're on an iPhone you're in bad luck though.. Apple expects you to stay in their walled garden.

## Start using different services

### Consider moving to Android

Right now, I don't see a good sovereign solution for mobile. Android is open source, which is good. But the reality is that Google adds a big layer on top: The Play Store, Google Maps, Chrome, and other services that collect metadata, often sent to Google every few minutes. You could run a 'de-googled' android (like [grapheneOS](https://grapheneos.org/)), but some high-security banking apps might complain that your device is "untrusted" because the bootloader is unlocked, and NFC payments don't work (because they rely on Google Pay).

Using Google's Android is still a better, more open option than Apple's walled garden. Hopefully better alternatives will emerge in 2026, and moving to Android will set you up better for changing. If you really want to de-google now, look at [Fairphone](https://shop.fairphone.com/nl/about-us), which is based in the Netherlands and offers phones that (optionally) come pre-installed with a de-googled android version.

### Replace cloud services

There are many more digital cloud services we use everyday. Consider moving to secure european services for:

- Files sync: Replace dropbox, google drive. I recommend [Proton Drive](https://proton.me/drive)
- Calendar: First own calendar data, and add it as a feed to whatever (web) app you like best. I recommend [Proton Calendar](https://proton.me/calendar).
- Password manager. This is critical infrastructure, choose wisely. I recommend [Proton Pass](https://proton.me/pass) or self-hosting.

## Why you should run a home server

If you are slightly technical: build your own homelab. 2026 is the year. The software has become very mature. The hardware has become incredibly powerful, affordable and surprisingly small and quiet. And AI can assist you with setting everything up in a breeze. No nerdy sysadmin friend required.

You can run high quality, free open source software in your own home, and access it securely from anywhere in the world. De-centralized, like the spirit of the original internet. You can gain full control of your own data and your own services. Here are some examples of cloud services you could choose to run:

- [immich](https://immich.app/) replaces photo backup/viewing services like [Google Photos](https://photos.google.com/)
- [jellyfin](https://jellyfin.org/) or [plex](https://watch.plex.tv/) can replace [Netflix](https://netflix.com/) and other streaming services, at least for the content that you own.
- [navidrome](https://www.navidrome.org/) can replace music services like [Spotify](https://spotify.com/), for music that you own.
- [vaultwarden](https://github.com/dani-garcia/vaultwarden) can replace password manager services like [Lastpass](https://www.lastpass.com/) or [1password](https://1password.com/)
- [nextcloud](http://nextcloud.com/) can replace file syncing/backup services like [Google drive](https://workspace.google.com/products/drive/) and [Dropbox](https://www.dropbox.com/). It can also replace online collaborative tools like [Google Sheets](https://workspace.google.com/products/sheets/) and [Google Docs](https://workspace.google.com/products/docs/?from=gafb-sheets-global_nav-en)
- [baikal](https://github.com/sabre-io/Baikal) as a calendar+contacts server which you can use with your favorite clients.
- automated workflows (f.e. on self-hosted [n8n](https://n8n.com/)) to download your linkedin contacts, backup github code repositories, sign up for your gym classes or order your groceries. AI can write the scripts for you.

<figure>
<img src="/assets/images/posts/homelab/immich_demo.png" alt="immich demo">
<figcaption>Immich photo backup and viewing interface</figcaption>
</figure>

There is so much more. To name a few: [Home Assistant](https://www.home-assistant.io/) to run your smart home, [cal.com](https://cal.com/) to manage calendar invites, [pi-hole](https://pi-hole.net/) to block ads on your network, [gitlab](https://about.gitlab.com/) to version control your code, [plausible](https://plausible.io/) to safely track visitors to your website, [endurain](https://github.com/endurain-project/endurain) to sync your sports data from Garmin and Strava, and [Campfire](https://once.com/campfire) to host your own group chat.

And I haven't even discussed AI *home inference*. If you have the budget for buying some serious hardware, you can run some serious AI models locally. As of Feb 2026, [Kimi K2.5](https://www.kimi.com/blog/kimi-k2-5.html) is fully open source and competitive with current leading models such as Claude Opus 4.5, Google's Gemini 3 and OpenAI's 5.2.

The cool thing is that you can host these services and then share them with your family and friends. I've ordered my hardware and will share more about the technical setup in a future blog.

## Conclusion

Don't wait and see. Sure, probably everything will be fine. Except that one time when it's not. You don't need to do everything at once. Start at the first row from the table below and do it this weekend. Then pick another next week. Each switch you make will help digital sovereignty.

Here's a quick overview of the switches discussed in this post:

| What | Replace | With | Effort |
|---|---|---|---|
| Messaging | WhatsApp | [Signal](https://signal.org/) | Low |
| Browser | Chrome | [Firefox](https://www.mozilla.org/firefox/) | Low |
| Search engine | Google | [Startpage](https://www.startpage.com/), [DuckDuckGo](https://duckduckgo.com/) | Low |
| 2FA app | Google/Microsoft Authenticator | [Proton Authenticator](https://proton.me/authenticator) | Low |
| File sync | Google Drive, Dropbox | [Proton Drive](https://proton.me/drive) or self-host | Low |
| Calendar | Google Calendar | [Proton Calendar](https://proton.me/calendar) or self-host | Low |
| Password manager | LastPass, 1Password | [Proton Pass](https://proton.me/pass), [Vaultwarden](https://github.com/dani-garcia/vaultwarden) | Medium |
| Email | Gmail, Outlook | [Proton Mail](https://proton.me/mail) | High |
| Photos | Google/Apple Photos | [Immich](https://immich.app/) (self-hosted) | High |
| Mobile OS | iPhone | Android / [Fairphone](https://shop.fairphone.com/nl/about-us) | High |

For me, digital sovereignty is not a sacrifice -- it's a push toward progress. A way out of complacency. The alternatives are often better designed, more private, and more respectful of your attention. The diversity and decentralization of these services is going to make all our digital lives better and more exciting. When you're set up, make sure to share what you've learned with friends and family.
