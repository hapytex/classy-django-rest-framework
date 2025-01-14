"""
    Most of the tests here are taken from Pygments since we had
    to replace the _format_lines method. Credits go to the authors.
"""

import os
import re
import unittest
import tempfile
import inspect

from html import escape
from io import StringIO
from pygments.lexers import PythonLexer
from pygments.formatters import NullFormatter
from pygments.formatters.html import escape_html

from rest_framework_ccbv.custom_formatter import CodeHtmlFormatter


class CodeHtmlFormatterTest(unittest.TestCase):
    def test_correct_output(self):
        hfmt = CodeHtmlFormatter(instance_class=type, nowrap=True)
        houtfile = StringIO()
        hfmt.format(tokensource, houtfile)

        nfmt = NullFormatter()
        noutfile = StringIO()
        nfmt.format(tokensource, noutfile)

        stripped_html = re.sub('<.*?>', '', houtfile.getvalue())
        escaped_text = escape_html(noutfile.getvalue())
        self.assertEqual(stripped_html, escaped_text)

    def test_all_options(self):
        for optdict in [dict(nowrap=True),
                        dict(linenos=True),
                        dict(linenos=True, full=True),
                        dict(linenos=True, full=True, noclasses=True)]:

            outfile = StringIO()
            fmt = CodeHtmlFormatter(instance_class=type, **optdict)
            fmt.format(tokensource, outfile)

    def test_linenos(self):
        optdict = dict(linenos=True)
        outfile = StringIO()
        fmt = CodeHtmlFormatter(instance_class=type, **optdict)
        fmt.format(tokensource, outfile)
        html = outfile.getvalue()
        self.assertTrue(re.search('<pre><span class="normal">\s+1</span>', html))

    def test_linenos_with_startnum(self):
        optdict = dict(linenos=True, linenostart=5)
        outfile = StringIO()
        fmt = CodeHtmlFormatter(instance_class=type, **optdict)
        fmt.format(tokensource, outfile)
        html = outfile.getvalue()
        self.assertTrue(re.search('<pre><span class="normal">\s+5</span>', html))

    def test_lineanchors(self):
        optdict = dict(lineanchors="foo")
        outfile = StringIO()
        fmt = CodeHtmlFormatter(instance_class=type, **optdict)
        fmt.format(tokensource, outfile)
        html = outfile.getvalue()
        self.assertTrue(re.search('<pre><span></span><a name="foo-1">', html))

    def test_lineanchors_with_startnum(self):
        optdict = dict(lineanchors="foo", linenostart=5)
        outfile = StringIO()
        fmt = CodeHtmlFormatter(instance_class=type, **optdict)
        fmt.format(tokensource, outfile)
        html = outfile.getvalue()
        self.assertTrue(re.search('<pre><span></span><a name="foo-5">', html))

    def test_get_style_defs(self):
        def fix_style_def(s):
            # Removes styles that were added by default on newer pygments versions
            return "\n".join(s.splitlines()[5:])

        fmt = CodeHtmlFormatter(instance_class=type)
        sd = fmt.get_style_defs()
        self.assertTrue(fix_style_def(sd).startswith('.'))

        fmt = CodeHtmlFormatter(instance_class=type, cssclass='foo')
        sd = fmt.get_style_defs()
        self.assertTrue(fix_style_def(sd).startswith('.foo'))
        sd = fmt.get_style_defs('.bar')
        self.assertTrue(fix_style_def(sd).startswith('.bar'))
        sd = fmt.get_style_defs(['.bar', '.baz'])
        fl = fix_style_def(sd).splitlines()[0]
        self.assertTrue('.bar' in fl and '.baz' in fl)

    def test_unicode_options(self):
        fmt = CodeHtmlFormatter(title=u'Föö',
                            instance_class=type,
                            cssclass=u'bär',
                            cssstyles=u'div:before { content: \'bäz\' }',
                            encoding='utf-8')
        handle, pathname = tempfile.mkstemp('.html')
        tfile = os.fdopen(handle, 'w+b')
        fmt.format(tokensource, tfile)
        tfile.close()

    def noop(self):
        pass

    def test_incode_links(self):
        # reference another method
        self.noop()
        this_token_source = list(PythonLexer().get_tokens(
            inspect.getsource(CodeHtmlFormatterTest.test_incode_links)
        ))
        hfmt = CodeHtmlFormatter(instance_class=self.__class__, nowrap=True)
        houtfile = StringIO()
        hfmt.format(this_token_source, houtfile)
        assert escape('<a href="#noop">noop</a>') in houtfile.getvalue()


tokensource = list(PythonLexer().get_tokens(
    inspect.getsource(CodeHtmlFormatterTest.test_correct_output)))
