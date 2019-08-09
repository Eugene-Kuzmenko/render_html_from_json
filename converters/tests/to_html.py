from converters import to_html
import unittest
from collections import OrderedDict


class TestToHTML(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(
            '<h1>title 1</h1><p>body 1</p><h1>title 2</h1><p>body 2</p>',
            to_html([
                OrderedDict([
                    ('h1', 'title 1'), ('p', 'body 1'),
                ]),
                OrderedDict([
                    ('h1', 'title 2'), ('p', 'body 2'),
                ]),
            ])
        )

        self.assertEqual(
            '{0}{1}{2}'.format(
                '<h1>title 2</h1><h2>title 1</h2><span>body 1</span>',
                '<h1>title 3</h1>',
                '<header>header 3</header><article>content</article>',
            ),
            to_html([
                OrderedDict([
                    ('h1', 'title 2'), ('h2', 'title 1'), ('span', 'body 1'),
                ]),
                OrderedDict([
                    ('h1', 'title 3'),
                ]),
                OrderedDict([
                    ('header', 'header 3'), ('article', 'content')
                ])
            ])
        )


    def test_not_list(self):
        with self.assertRaises(TypeError) as context:
            to_html({
                0: {'h1': 'title 1', 'div': 'body 1'},
                1: {'h1': 'title 2', 'div': 'body 2'},
            })

            self.assertTrue(
                'Expected type <class \'list\'>. Got <class \'dict\'>' in context.exeptions
            )
