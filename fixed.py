import json
from jinja2 import Environment, FileSystemLoader

# Function to escape LaTeX special characters
def escape_latex(text):
    """
    Escapes LaTeX special characters in the given text.
    """
    if not isinstance(text, str):
        return text
    replacements = {
        '&': '\\&',
        '%': '\\%',
        '$': '\\$',
        '#': '\\#',
        '_': '\\_',
        '{': '\\{',
        '}': '\\}',
        '~': '\\textasciitilde{}',
        '^': '\\textasciicircum{}',
        '\\': '\\textbackslash{}',
        '\n': '\\newline{}',
    }
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text

# Path to your JSON file
file_path = 'saksham_op.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Data extraction function with LaTeX escaping
def extract_fixed_assets_data(data):
    fixed_assets_data = {}
    table = data["fixed_assets"]["table"]

    for category, details in table.items():
        years = [escape_latex(item["Year"]) for item in details]
        values = [escape_latex(item["Value"]) for item in details]
        fixed_assets_data[category] = {
            "Years": years,
            "Values": values
        }

    fixed_assets_data["commentary"] = [escape_latex(comment) for comment in data["fixed_assets"]["commentary"]]
    return fixed_assets_data

# Extracting the fixed assets data
fixed_assets_data = extract_fixed_assets_data(data)

# Setting up Jinja2 environment
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

template = env.get_template('fixed.tex')

# Rendering the template with the extracted data
output = template.render(fixed_assets=fixed_assets_data, commentary=fixed_assets_data['commentary'])

# Saving the output to a file
with open('fixed_assets_output.tex', 'w') as f:
    f.write(output)

print("LaTeX document has been generated and saved to 'fixed_assets_output.tex'")
print(output)