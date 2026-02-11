

def on_page_context(context, **kwargs):
    """
    Store blog pages in context, so we can use them in home.html override.
    """
    context['blog_pages'] = []
    for page in context['pages']:
        if page.page.meta.get('template') == "blog-post.html" and not page.page.meta.get('draft'):
            context['blog_pages'].append(page.page)

