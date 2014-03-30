"""
Helper for YAML frontmatter in Markdown files

@author Richard Caceres, @rchrd2
"""

import markdown
import yaml
import re

# Setup Markdown
md = markdown.Markdown(extensions=['meta', 'sane_lists', 'smarty'])

frontmatter_regex = re.compile(r'^\s*---(.*)---\s*(.*)$', re.DOTALL|re.MULTILINE)

def get_html_and_meta(md_string):
    """
    >>> get_html_and_meta('''---
    ... tags: one, two, three
    ... ---
    ... 
    ... # This is some markdown
    ... Test test test
    ... 
    ... ''')
    ({'tags': 'one, two, three'}, u'<h1>This is some markdown</h1>\\n<p>Test test test</p>')
    
    """
    # parse out front matter
    # render rest as html
    m = frontmatter_regex.match(md_string)
    if m:
        try:
            meta = yaml.load(m.group(1))
        except:
            meta = {}
        return meta, md.convert(m.group(2))
    else:
        return {}, md.convert(md_string)
    
def create_markdown_with_meta(meta, md_string):
    """
    Create a markdown document with YAML frontmatter.
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
    return u"""---
%s
---
%s
""" % ( yaml.dump(meta, default_flow_style=False), md_string )
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
