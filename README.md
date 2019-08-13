
# HTML Renderer

Renderer HTML from JSON files

# Versions
- [Task 1](https://github.com/Eugene-Kuzmenko/render_html_from_json/tree/feature/task_1) 
- [Task 2](https://github.com/Eugene-Kuzmenko/render_html_from_json/tree/feature/task_2) 
- [Task 3](https://github.com/Eugene-Kuzmenko/render_html_from_json/tree/feature/task_3) 
- [Task 4](https://github.com/Eugene-Kuzmenko/render_html_from_json/tree/feature/task_4) 
- [Task 5](https://github.com/Eugene-Kuzmenko/render_html_from_json/tree/feature/task_5) 

## Requirements

For using converver you have to use `Python 3.6` or higher


### Usage
usage: json2html.py [-h] [--dest DEST] source

positional arguments:
  source       Source JSON file

optional arguments:
  -h, --help   show help message and exit
  --dest Output HTML filename

Example:

```
$ python3 json2html.py source.json --dest result.html
```


### Testing
```
python3 -m unittest converters/tests/to_html.py 
```
