from collections import OrderedDict


def get_tag_content(content):
    if isinstance(content, OrderedDict):
        raise TypeError('Tag content can\'t be instance of Dict')

    if isinstance(content, list):
        return to_html(content)

    return content


def to_tag(item, tag):
    return f'<{tag}>{get_tag_content(item[tag])}</{tag}>'


def to_html(tree):
    if not isinstance(tree, list):
        raise TypeError(f'Expected type {type(list())}. Got {type(tree)}')

    result = ''
    for item in tree:
        tags = ''
        for tag in item:
            tags = f'{tags}{to_tag(item, tag)}'

        result = f'{result}<li>{tags}</li>'

    return f'<ul>{result}</ul>'
