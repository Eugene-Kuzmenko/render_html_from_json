def to_tag(item, tag):
    return f'<{tag}>{item[tag]}</{tag}>'


def to_html(tree):
    if not isinstance(tree, list):
        raise TypeError(f'Expected type {type(list())}. Got {type(tree)}')

    result = ''
    for item in tree:
        for tag in item:
            result = f'{result}{to_tag(item, tag)}'

    return result
