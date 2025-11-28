---
date: 2025-11-28 18:00:00
slug: introducing-alt-alpha
authors:
  - timvink
---

# Introducing Alt Alpha: Explore alternative keyboard layouts

<script>
/**
 * Standalone Keyboard Visualization for Blog Post
 * Renders a static split keyboard layout
 */

(function() {
    // Key dimensions
    const KEY_W = 50;
    const KEY_H = 50;
    const GAP = 5;
    const KS = KEY_W + GAP;

    // Columnar stagger (vertical offset for each column)
    const STAGGER = [20, 20, 10, 0, 10, 20];

    // Hand offsets
    const LEFT_HAND_X = 50;
    const LEFT_HAND_Y = 10;
    const RIGHT_HAND_X = 425;
    const RIGHT_HAND_Y = 10;
    const THUMB_Y_OFFSET = 180;

    // Home position key indices (columns 1-4 of home row)
    const HOME_POSITIONS = [13, 14, 15, 16, 19, 20, 21, 22];

    // Key positions for columnar staggered layout
    function getKeyPositions() {
        return [
            // Left Hand - Top row (0-5)
            { x: LEFT_HAND_X + KS * 0, y: LEFT_HAND_Y + KS * 0 + STAGGER[0], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 1, y: LEFT_HAND_Y + KS * 0 + STAGGER[1], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 2, y: LEFT_HAND_Y + KS * 0 + STAGGER[2], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 3, y: LEFT_HAND_Y + KS * 0 + STAGGER[3], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 4, y: LEFT_HAND_Y + KS * 0 + STAGGER[4], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 5, y: LEFT_HAND_Y + KS * 0 + STAGGER[5], w: KEY_W, h: KEY_H },
            
            // Right Hand - Top row (6-11)
            { x: RIGHT_HAND_X + KS * 0, y: RIGHT_HAND_Y + KS * 0 + STAGGER[5], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 1, y: RIGHT_HAND_Y + KS * 0 + STAGGER[4], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 2, y: RIGHT_HAND_Y + KS * 0 + STAGGER[3], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 3, y: RIGHT_HAND_Y + KS * 0 + STAGGER[2], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 4, y: RIGHT_HAND_Y + KS * 0 + STAGGER[1], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 5, y: RIGHT_HAND_Y + KS * 0 + STAGGER[0], w: KEY_W, h: KEY_H },

            // Left Hand - Home row (12-17)
            { x: LEFT_HAND_X + KS * 0, y: LEFT_HAND_Y + KS * 1 + STAGGER[0], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 1, y: LEFT_HAND_Y + KS * 1 + STAGGER[1], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 2, y: LEFT_HAND_Y + KS * 1 + STAGGER[2], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 3, y: LEFT_HAND_Y + KS * 1 + STAGGER[3], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 4, y: LEFT_HAND_Y + KS * 1 + STAGGER[4], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 5, y: LEFT_HAND_Y + KS * 1 + STAGGER[5], w: KEY_W, h: KEY_H },
            
            // Right Hand - Home row (18-23)
            { x: RIGHT_HAND_X + KS * 0, y: RIGHT_HAND_Y + KS * 1 + STAGGER[5], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 1, y: RIGHT_HAND_Y + KS * 1 + STAGGER[4], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 2, y: RIGHT_HAND_Y + KS * 1 + STAGGER[3], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 3, y: RIGHT_HAND_Y + KS * 1 + STAGGER[2], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 4, y: RIGHT_HAND_Y + KS * 1 + STAGGER[1], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 5, y: RIGHT_HAND_Y + KS * 1 + STAGGER[0], w: KEY_W, h: KEY_H },

            // Left Hand - Bottom row (24-29)
            { x: LEFT_HAND_X + KS * 0, y: LEFT_HAND_Y + KS * 2 + STAGGER[0], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 1, y: LEFT_HAND_Y + KS * 2 + STAGGER[1], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 2, y: LEFT_HAND_Y + KS * 2 + STAGGER[2], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 3, y: LEFT_HAND_Y + KS * 2 + STAGGER[3], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 4, y: LEFT_HAND_Y + KS * 2 + STAGGER[4], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 5, y: LEFT_HAND_Y + KS * 2 + STAGGER[5], w: KEY_W, h: KEY_H },
            
            // Right Hand - Bottom row (30-35)
            { x: RIGHT_HAND_X + KS * 0, y: RIGHT_HAND_Y + KS * 2 + STAGGER[5], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 1, y: RIGHT_HAND_Y + KS * 2 + STAGGER[4], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 2, y: RIGHT_HAND_Y + KS * 2 + STAGGER[3], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 3, y: RIGHT_HAND_Y + KS * 2 + STAGGER[2], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 4, y: RIGHT_HAND_Y + KS * 2 + STAGGER[1], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 5, y: RIGHT_HAND_Y + KS * 2 + STAGGER[0], w: KEY_W, h: KEY_H },

            // Thumbs (36-39)
            { x: LEFT_HAND_X + KS * 4, y: LEFT_HAND_Y + THUMB_Y_OFFSET + STAGGER[4], w: KEY_W, h: KEY_H },
            { x: LEFT_HAND_X + KS * 5, y: LEFT_HAND_Y + THUMB_Y_OFFSET + STAGGER[5], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 0, y: RIGHT_HAND_Y + THUMB_Y_OFFSET + STAGGER[5], w: KEY_W, h: KEY_H },
            { x: RIGHT_HAND_X + KS * 1, y: RIGHT_HAND_Y + THUMB_Y_OFFSET + STAGGER[4], w: KEY_W, h: KEY_H }
        ];
    }

    // Parse Cyanophage URL layout string to flat array
    function parseLayoutString(layoutString) {
        const decoded = decodeURIComponent(layoutString);
        const flatLayout = Array(40).fill(' ');

        // Cyanophage key mapping
        const keyMap = [];
        
        // Positions 0-10: row 0, cols 1-11
        for (let i = 0; i <= 10; i++) {
            if (i <= 4) keyMap[i] = i + 1;           // Left: cols 1-5 -> indices 1-5
            else keyMap[i] = i + 1;                   // Right: cols 6-11 -> indices 6-11
        }
        
        // Positions 11-21: row 1, cols 1-11  
        for (let i = 0; i <= 10; i++) {
            if (i <= 4) keyMap[11 + i] = 13 + i;     // Left home row: indices 13-17
            else keyMap[11 + i] = 18 + (i - 5);      // Right home row: indices 18-23
        }
        
        // Positions 22-31: row 2, cols 1-10
        for (let i = 0; i <= 9; i++) {
            if (i <= 4) keyMap[22 + i] = 25 + i;     // Left bottom: indices 25-29
            else keyMap[22 + i] = 30 + (i - 5);      // Right bottom: indices 30-35
        }
        
        // Position 32: left bottom outer pinky (index 24)
        keyMap[32] = 24;
        // Position 34: left home outer pinky (index 12)
        keyMap[34] = 12;

        // Map the 32 main keys
        for (let i = 0; i < 32; i++) {
            if (decoded[i]) {
                const physicalKeyIndex = keyMap[i];
                if (physicalKeyIndex !== undefined) {
                    flatLayout[physicalKeyIndex] = decoded[i].toLowerCase();
                }
            }
        }

        // Map outer pinky keys
        if (decoded.length > 32 && decoded[32] !== '\\') {
            flatLayout[24] = decoded[32].toLowerCase();
        }
        if (decoded.length > 34 && decoded[34] !== '^') {
            flatLayout[12] = decoded[34].toLowerCase();
        }

        // Handle thumb key (position 33)
        if (decoded.length > 33) {
            const thumbChar = decoded[33].toLowerCase();
            if (/^[a-z]$/.test(thumbChar)) {
                flatLayout[39] = thumbChar; // Right inner thumb
            }
        }

        return flatLayout;
    }

    // Create SVG key element
    function createKey(id, x, y, w, h, isThumb, char) {
        const ns = "http://www.w3.org/2000/svg";
        const isHomePosition = HOME_POSITIONS.includes(id);
        const isAssigned = char !== ' ' && char !== '';

        const group = document.createElementNS(ns, 'g');
        group.setAttribute('id', `key-group-${id}`);
        
        let groupClass = 'key';
        if (isThumb) groupClass += ' thumb-key';
        if (isHomePosition) groupClass += ' home-position-key';
        if (!isAssigned) groupClass += ' unassigned-key';
        group.setAttribute('class', groupClass);

        // Apply rotation for thumb keys
        if (isThumb) {
            let angle = 0;
            if (id === 36) angle = 6;
            if (id === 37) angle = 12;
            if (id === 38) angle = -12;
            if (id === 39) angle = -6;
            
            const centerX = x + w / 2;
            const centerY = y + h / 2;
            group.setAttribute('transform', `rotate(${angle} ${centerX} ${centerY})`);
        }

        const rect = document.createElementNS(ns, 'rect');
        rect.setAttribute('x', x);
        rect.setAttribute('y', y);
        rect.setAttribute('width', w);
        rect.setAttribute('height', h);
        rect.setAttribute('class', 'key-rect');
        rect.setAttribute('rx', '6');
        
        const text = document.createElementNS(ns, 'text');
        text.setAttribute('x', x + w / 2);
        text.setAttribute('y', y + h / 2);
        text.setAttribute('class', 'key-legend');
        text.textContent = char;
        
        group.appendChild(rect);
        group.appendChild(text);
        
        return group;
    }

    // Render keyboard to SVG element
    function renderKeyboard(svgElement, layoutArray) {
        const positions = getKeyPositions();
        
        // Calculate viewBox
        let maxX = 0, maxY = 0;
        positions.forEach((pos) => {
            maxX = Math.max(maxX, pos.x + pos.w);
            maxY = Math.max(maxY, pos.y + pos.h);
        });
        
        svgElement.setAttribute('viewBox', `0 0 ${maxX + 20} ${maxY + 20}`);
        svgElement.innerHTML = '';
        
        positions.forEach((pos, i) => {
            const isThumb = i >= 36;
            const char = layoutArray[i] || ' ';
            const key = createKey(i, pos.x, pos.y, pos.w, pos.h, isThumb, char);
            svgElement.appendChild(key);
        });
    }

    // Initialize keyboard demo
    function init() {
        const containers = document.querySelectorAll('.keyboard-container');
        if (!containers.length) return;

        containers.forEach(container => {
            const layoutString = container.dataset.layout;
            if (!layoutString) return;

            const layoutArray = parseLayoutString(layoutString);
            
            const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
            svg.style.maxWidth = '100%';
            svg.style.height = 'auto';
            
            renderKeyboard(svg, layoutArray);
            container.appendChild(svg);
        });
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();

</script>


Almost a year ago I switched to the [ZSA Voyager](https://www.zsa.io/voyager), a programmable, ergonomic split keyboard that features four thumb buttons per hand instead of the single spacebar found on traditional keyboards. After having a lot of fun optimizing [my keyboard layout](https://configure.zsa.io/voyager/layouts/bZ5m5/latest/0) and [customizing shortcuts](https://github.com/timvink/dotfiles), I got interested in alternative alpha keyboard layouts. The 'AKL' scene is still actively developing new layouts with many great new options in the last two years. I found it hard to choose and fun to compare, so in this post I'll introduce a new tool I built: [altalpha.timvink.nl](https://altalpha.timvink.nl)

*[AKL]: Alternative Keyboard Layouts

<!-- more -->

## Alternatives to QWERTY

We all know QWERTY is flawed. It was designed in 1873 for typewriters, not ergonomic comfort. It requires frequent, uncomfortable finger stretches and high same-finger utilization. While you can certainly type fast on QWERTY ([world record of 305 wpm](https://www.youtube.com/watch?v=GGwKCi4FX84)), it requires more effort than necessary.

Alternative layouts aim to fix this. There are many great options. I highly recommend Pascal Getreuer's [Guide to alt keyboard layouts](https://getreuer.info/posts/keyboards/alt-layouts/index.html) which recommends as a very solid pick the 2024 [gallium](https://github.com/GalileoBlues/Gallium) layout:

<figure class="keyboard-demo">
<div class="keyboard-container" data-layout="bldcvjyou%2C-nrtsgphaei%2Fxqmwzkf%27%3B.%5C%5E"></div>
<figcaption>The <a href="https://github.com/GalileoBlues/Gallium">gallium</a> (2024) layout as visualized by <a href="https://altalpha.timvink.nl/">altalpha.timvink.nl</a></figcaption>
</figure>

But is that the best one? And what about those thumb buttons?

## Thumb layouts

Having a keyboard with multiple thumb buttons opens up an interesting opportunity: **What if you assign a letter to a thumb key?**. The [Pressing E with the Thumb](https://precondition.github.io/pressing-e-with-the-thumb) article explores this concept in depth. For example, the [night](https://www.valorance.org/night/) (2024) 'thumb' layout assigns the `r` to one of the left thumb buttons:

<figure class="keyboard-demo">
<div class="keyboard-container" data-layout="bflkqpgou.%3Dnshtmycaei%3Bxvjdz%27w-%2F%2C%5Cr"></div>
<figcaption>The <a href="https://www.valorance.org/night/">night</a> (2024) layout as visualized by <a href="https://altalpha.timvink.nl/">altalpha.timvink.nl</a></figcaption>
</figure>

These thumb layouts only make it harder to choose a layout.

## How to pick a layout?

Note that creating a new layout is non-trivial. There are $26! \approx 4.03 \times 10^{26}$ possible combinations for the 26 letters of the English alphabet. If it took 1 nanosecond to review a layout, it would take ~3.17 billion years to review them all. The alternative keyboard layout community is vibrant, with enthusiasts using optimizers and statistical analysis to design better layouts. In recent years there has been significant progress with new layouts performing very well on a range of metrics. Examples include layouts like [Enthium v11](https://github.com/sunaku/enthium), [nordrassil rejuvened](https://www.reddit.com/r/KeyboardLayouts/comments/1oqqfql/%F0%96%A3%82nordrassils_rejuvenation%EF%BE%9F_a_refinement_of_the/) or the [Hands Down Neu variants](https://sites.google.com/alanreiser.com/handsdown/home/hands-down-neu).

Learning a new layout is not an easy undertaking. It's worth it according to many who have made the investment. But making a good choice is hard.
Now it's true that *any* reasonable choice is going to be a huge upgrade from QWERTY. The relative differences between good layouts are a lot smaller. That said, it's still very interesting to search for a layout that fits best for your personal preferences. 

## Introducing Alt Alpha Ranker

I decided to deep dive into this rabbit hole and build my own tool to compare and test these layouts: **[altalpha.timvink.nl](https://altalpha.timvink.nl)**. 
It has a ranking board for layouts, but you can also use a typing test to try what a layout 'feels' like, without learning it! The trick there is to translate the corresponding characters to a keyboard layout you can already touch type.

<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
    <div style="text-align: center;">
        <img src="/assets/images/posts/altalpha/ranker.png" width="400px" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />
        <p><em>Layout Rankings</em></p>
    </div>
    <div style="text-align: center;">
        <img src="/assets/images/posts/altalpha/typingtest.png" width="400px" style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);" />
        <p><em>Typing Test</em></p>
    </div>
</div>

The tool focuses on Latin-language layouts and intentionally excludes esoteric concepts like [Magic Keys](https://layouts.wiki/reference/terminology/magic/) or Repeat Keys to keep comparisons fair and approachable.

## How It's Built

For those technically inclined, here are a few highlights of the project:

### Visualization & Parsing

I wrote a custom [`keyboard.js`](https://github.com/timvink/alt_alpha_ranker/blob/main/site/keyboard.js) class to manage layout definitions. This powers the [`keyboard_visualization.js`](https://github.com/timvink/alt_alpha_ranker/blob/main/site/keyboard_visualization.js) renderer and [`cyanophage.js`](https://github.com/timvink/alt_alpha_ranker/blob/main/site/cyanophage.js), a module that generates URLs for the [Cyanophage layout playground](https://cyanophage.github.io/).

### Scraping metrics

Cyanophage has built an excellent [keyboard layout ranking engine](https://cyanophage.github.io/). We use the generated Cyanophage url for a layout and then scrape the corresponding metrics.

### The Typing Test

The typing test interface was inspired by [Monkeytype](https://github.com/monkeytypegame/monkeytype). I even used their open-source 1k word language datasets to ensure the test content is representative of real-world usage.

### Let users add layouts

Layouts are constantly evolving. To keep up, I built an automated workflow:

1.  The [Add new layout](https://altalpha.timvink.nl/new_layout.html) page includes a parser that converts text-based layouts into a configuration format.
2.  Clicking "Create GitHub issue" pre-fills the issue body with the correct YAML configuration.
3.  The issue is assigned to **GitHub Copilot**, which automatically opens a Pull Request to update [`config/layouts.yml`](https://github.com/timvink/alt_alpha_ranker/blob/main/config/layouts.yml).
4.  Once merged, a GitHub Action runs [`scripts/scrape_stats.py`](https://github.com/timvink/alt_alpha_ranker/blob/main/scripts/scrape_stats.py) to scrape any missing layout data and commits it to `data.json`, triggering a redeploy of the website.

### Tracing `r/KeyboardLayouts`

Many new layouts are announced on Reddit. So I built a scraper ([`scripts/scrape_reddit.py`](https://github.com/timvink/alt_alpha_ranker/blob/main/scripts/scrape_reddit.py)) for `r/KeyboardLayouts` that uses Reddit's RSS feed to extract posts and comments. Those are then passed to an LLM. If the post or comment is deemed a new layout, a new GitHub issue will be created and assigned to me to review it.

## Conclusion

I still haven't picked a layout to learn! But building the tool was a lot of fun. Hopefully it's useful for the community.

If you want to dive deeper, here are some good starting points:

- [layout wiki's recommendations](https://layouts.wiki/guides/start/recommendations)
- Pascal Getreuer's [Guide to alt keyboard layouts](https://getreuer.info/posts/keyboards/alt-layouts/index.html) 