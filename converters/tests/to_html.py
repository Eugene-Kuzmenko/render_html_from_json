from converters import to_html
import unittest


class TestToHTML(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(
            to_html([
                {'title': 'title 1', 'body': 'body 1'},
                {'title': 'title 2', 'body': 'body 2'}
            ]),
            '<h1>title 1</h1><p>body 1</p><h1>title 2</h1><p>body 2</p>'
        )

    def test_not_list(self):
        with self.assertRaises(TypeError) as context:
            to_html({
                0: {'title': 'title 1', 'body': 'body 1'},
                1: {'title': 'title 2', 'body': 'body 2'},
            })

            self.assertTrue(
                'Expected type <class \'list\'>. Got <class \'dict\'>' in context.exeptions
            )

    def test_field_missing(self):
        with self.assertRaises(ValueError) as context:
            to_html([
                {'title': 'title 1', 'body': 'body 1'},
                {'body': 'body 2'},
            ])

            self.assertTrue(
                'title is missing from the item #2' in context.exeptions
            )

        with self.assertRaises(ValueError) as context:
            to_html([
                {'title': 'title 1', 'body': 'body 1'},
                {'title': 'title 2'},
                {'body': 'body 3'}
            ])

            self.assertTrue(
                'body is missing from the item #2' in context.exeptions
            )
