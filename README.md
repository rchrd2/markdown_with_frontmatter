markdown_with_frontmatter
=========================

Helper for YAML frontmatter in Markdown files

See <http://jekyllrb.com/docs/frontmatter/>.

Usage:


Get meta and html:
```
>>> get_html_and_meta('''---
... tags: one, two, three
... ---
... 
... # This is some markdown
... Test test test
... 
... ''')
({'tags': 'one, two, three'}, '<h1>This is some markdown</h1>\\n<p>Test test test</p>'')
```

Create a markdown document with YAML frontmatter.
```
>>> print create_markdown_with_meta({'tags':['one','two','three']}, "# Hi")
---
tags:
- one
- two
- three
<BLANKLINE>
---
# Hi
<BLANKLINE>
"""

```


Dependencies:
- PyYaml
- markdown
