---
date: 2024-09-22 22:00:00
slug: benchmarking-sklearn-python
authors:
  - timvink
---

# Benchmarking scikit-learn across python versions using `uv`

When python 3.11 came out 2 years ago (24 October 2022) it promised to be 10-60% faster than python 3.10, and 1.25x faster on the standard benchmark suite (see the [what's new in 3.11](https://docs.python.org/3/whatsnew/3.11.html)). I've always wondered how that translates to training machine learning models in python, but I couldn't be bothered to write a benchmark. That is, until [astral](https://astral.sh/) released [uv 0.4.0](https://github.com/astral-sh/uv/releases/tag/0.4.0) which introduces ["_a new, unified toolchain that takes the complexity out of Python development_"](https://astral.sh/blog/uv-unified-python-packaging).

<!-- more -->

`uv` has been blowing my mind and is transforming the way I work, and there are many resources out there already discussing it (like [Rye and uv: August is Harvest Season for Python Packaging](https://lucumr.pocoo.org/2024/8/21/harvest-season/) and [uv under discussion on Mastodon](https://simonwillison.net/2024/Sep/8/uv-under-discussion-on-mastodon/)). One of the new capabilities is that `uv python` can _bootstrap and install Python for you_. Instead of building python from source, `uv` uses (and contributes to) the [python standalone builds](https://gregoryszorc.com/docs/python-build-standalone/main/) project. For each python version they will pre-build python binaries suitable for a wide range of system architectures (currently 773 builds per python version).

The CEO of Astral (creator of `uv`) is Charlie Marsh, and he recently appeared on the _Talk Python To Me_ podcast ([Episode #476 unified packaging with uv](https://talkpython.fm/episodes/show/476/unified-python-packaging-with-uv)). There he explained that these python builds _"will be noticeably faster than what you would get by default with [PyEnv](https://github.com/pyenv/pyenv)"_ because they are compiled with optimizations. And because it's a standalone binary, the installation speed is restricted to the time it takes to stream and unzip it down into disk. It now takes me ~10-20 _seconds_ to install a new python version!

## The benchmark

We train a binary classifier (sklearn's `HistGradientBoostingClassifier`)
on a small and medium dataset:

- [adult](https://www.openml.org/search?type=data&sort=runs&id=1590&status=active) openml dataset (39k rows and 14 features, 2.6Mb). 
- [click_prediction_small](https://www.openml.org/search?type=data&sort=runs&id=1218&status=active) openml dataset (1.2M rows and 9 features, 102Mb).

We'll run on a laptop running Ubuntu with an AMD Ryzen 7 5000 series CPU and 16GB of RAM.

To setup the benchmark project I ran:

```bash
uv init sk_benchmark && cd sk_benchmark
uv add scikit-learn pandas memo tqdm
```

Then we can add a `scripts/benchmark.py` script:

<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Ftimvink%2Fpersonal-site%2Fblob%2Fmain%2Fscripts%2Fsk_benchmark%2Fbenchmark.py&style=atom-one-dark&type=code&showBorder=on&showLineNumbers=on&showFileMeta=on&showFullPath=on&showCopy=on&fetchFromJsDelivr=on"></script>

This is the real party trick :partying_face::

```bash
for py in 3.10 3.11 3.12; 
do
  uv run --quiet --python $py --python-preference "managed-only" benchmark.py;
done
```

A couple of things to note here:

- `uv run` will take care of updating our virtual environment with the correct python version and dependencies
- the `--python-preference "managed-only"` flag makes sure we only use the optimized python builds from the python-standalone-builds 
- The `--quiet` flag will suppress the output of the `uv` command

## The results

I processed the result using my own [mkdocs-charts-plugin](https://github.com/timvink/mkdocs-charts-plugin) to visualize with [vega-lite](https://vega.github.io/vega-lite/). The results:

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
   "title": "Training on 'adult' dataset",
  "data": {"url" : "assets/json_data/benchmark_python_adult.json"},
  "encoding": {"y": {"field": "python", "type": "nominal", "title": null}},
  "layer": [
    {
      "mark": {"type": "rule"},
      "encoding": {
        "x": {"field": "lower", "type": "quantitative","scale": {"zero": false}, "title": "Time taken (s)"},
        "x2": {"field": "upper"}
      }
    },
    {
      "mark": {"type": "bar", "size": 14},
      "encoding": {
        "x": {"field": "q1", "type": "quantitative"},
        "x2": {"field": "q3"},
        "color": {"field": "Species", "type": "nominal", "legend": null}
      }
    },
    {
      "mark": {"type": "tick", "color": "white", "size": 14},
      "encoding": {
        "x": {"field": "median", "type": "quantitative"}
      }
    }
  ]
}
```

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
   "title": "Training on 'click_prediction_small' dataset",
  "data": {"url" : "assets/json_data/benchmark_python_click_prediction_small.json"},
  "encoding": {"y": {"field": "python", "type": "nominal", "title": null}},
  "layer": [
    {
      "mark": {"type": "rule"},
      "encoding": {
        "x": {"field": "lower", "type": "quantitative","scale": {"zero": false}, "title": "Time taken (s)"},
        "x2": {"field": "upper"}
      }
    },
    {
      "mark": {"type": "bar", "size": 14},
      "encoding": {
        "x": {"field": "q1", "type": "quantitative"},
        "x2": {"field": "q3"},
        "color": {"field": "Species", "type": "nominal", "legend": null}
      }
    },
    {
      "mark": {"type": "tick", "color": "white", "size": 14},
      "encoding": {
        "x": {"field": "median", "type": "quantitative"}
      }
    }
  ]
}
```

... are quite underwhelming!

The differences are not that big, and python 3.12 is even the slowest. Digging a bit deeper, it turns out python 3.12 is indeed slower than python 3.11. Of course it depends (see this [extensive comparison benchmark](https://en.lewoniewski.info/2023/python-3-11-vs-python-3-12-performance-testing/)).

But of course what is _really_ going on here is that scikit-learn is not using python for training the models, but rather more optimized routines written in [Cython](https://cython.readthedocs.io/en/latest/src/quickstart/overview.html) (Cython is a superset of Python that compiles to C/C++).

So this entire benchmark doesn't make much sense.. but it was fun to do!

## Conclusions

The training speed of scikit-learn won't differ much between python versions because most of the workload is done in Cython. And I could have known before running any benchmarks!

If you're looking to speed up your ML projects, start at scikit-learn's page on [computational performance](https://scikit-learn.org/stable/computing/computational_performance.html). As a bonus, you can try switching all your preprocessing code from `pandas` to [`polars`](https://github.com/pola-rs/polars) dataframes. `scikit-learn` supports `polars` since January 2024 ([scikit-learn 1.4+](https://scikit-learn.org/dev/whats_new/v1.4.html#version-1-4-0)) so you won't even have to convert your dataframes.
Queries using [polars](https://github.com/pola-rs/polars) dataframes are 10-100x faster than [pandas](https://github.com/pandas-dev/pandas) dataframes ([benchmark](https://pola.rs/posts/benchmarks/)). On top of that, polars just [released a new accelerated GPU engine with nvidia](https://pola.rs/posts/gpu-engine-release/) that promises another 2-13x speedup.
