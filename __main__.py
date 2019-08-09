import converters
import inputs

print(
    inputs.json_file('source.json', converters.to_html)
)
