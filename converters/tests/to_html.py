from converters import to_html
import unittest
from collections import OrderedDict


class TestToHTML(unittest.TestCase):
    def test_correct_1(self):
        self.assertEqual(
            ''.join([
                '<ul>',
                '<li><h1>title 1</h1><p>body 1</p></li>',
                '<li><h1>title 2</h1><p>body 2</p></li>',
                '</ul>'
            ]),
            to_html([
                OrderedDict([
                    ('h1', 'title 1'), ('p', 'body 1'),
                ]),
                OrderedDict([
                    ('h1', 'title 2'), ('p', 'body 2'),
                ]),
            ])
        )

    def test_correct_2(self):
        self.assertEqual(
            ''.join([
                '<ul>',
                '<li><h1>title 2</h1><h2>title 1</h2><span>body 1</span></li>',
                '<li><h1>title 3</h1></li>',
                '<li><header>header 3</header><article>content</article></li>',
                '</ul>'
            ]),
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

    def test_nested(self):
        self.assertEqual(
            ''.join([
                '<ul>',
                    '<li>',
                        '<h1>title 1</h1>',
                        '<p>body 1</p>',
                    '</li>',
                    '<li>'
                        '<h1>title 2</h1>',
                        '<p>body 2</p>',
                    '</li>',
                    '<li>',
                        '<section>'
                            '<ul>',
                                '<li>',
                                    '<h3>Level 2</h3>',
                                '</li>',
                                '<li>',
                                    '<h3>Status:</h3>',
                                    '<span>Achieved</span>',
                                '</li>',
                            '</ul>',
                        '</section>',
                        '<div>here</div>',
                    '</li>',
                '</ul>'
            ]),
            to_html([
                OrderedDict([
                    ('h1', 'title 1'), ('p', 'body 1'),
                ]),
                OrderedDict([
                    ('h1', 'title 2'), ('p', 'body 2'),
                ]),
                OrderedDict([
                    ('section', [
                        OrderedDict([
                            ('h3', 'Level 2'),
                        ]),
                        OrderedDict([
                            ('h3', 'Status:'), ('span', 'Achieved')
                        ]),
                    ]),
                    ('div', 'here')
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

    def test_children_not_dict(self):
        with self.assertRaises(TypeError) as context:
            to_html([
                OrderedDict([
                    ('h1', 'title 1'), ('p', 'body 1'),
                ]),
                OrderedDict([
                    ('h1', 'title 2'), ('p', 'body 2'),
                ]),
                OrderedDict([
                    ('section', OrderedDict([
                        ('h3', 'Level 2'),
                    ])),
                    ('div', 'here')
                ])
            ])

            self.assertTrue('Tag content can\'t be instance of Dict')
