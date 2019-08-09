def to_html(tree):
    result = ''

    if not isinstance(tree, list):
        raise TypeError(f'Expected type {type(list())}. Got {type(tree)}')

    i = 0
    for item in tree:
        for field in ('title', 'body'):
            if field not in item:
                raise ValueError(f'{field} is missing from the item #{i}')
        result = f'{result}<h1>{item["title"]}</h1><p>{item["body"]}</p>'
        i += 1

    return result
