import converters
import inputs

print(
    inputs.json_file('source.json', converters.dict_to_html)
)
