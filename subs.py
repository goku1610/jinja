import json
from jinja2 import Environment, FileSystemLoader

# Function to escape LaTeX special characters and replace underscores with spaces
def escape_latex(text):
    """
    Escapes LaTeX special characters in the given text and replaces underscores with spaces.
    """
    if not isinstance(text, str):
        return text
    replacements = {
        '&': '\\&',
        '%': '\\%',
        '$': '\\$',
        '#': '\\#',
        '_': ' ',  # Replace underscores with spaces
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

# Extract and process subsidiary and JV information with LaTeX escaping
subsidiary_jv_info_data = {
    "subsidiary": [],
    "JV_information": [escape_latex(info) for info in data["subsidiary_jv_info"]["JV information"]]
}

subsidiaries = data["subsidiary_jv_info"]["subsidiary"]
for subsidiary in subsidiaries:
    subsidiary_info = {
        "subsidiary_name": escape_latex(subsidiary["subsidiary_name"]),
        "Date_of_Creation": escape_latex(subsidiary["Date of Creation"]),
        "Interest": escape_latex(subsidiary["Interest"]),
        "Location": escape_latex(subsidiary["Location"])
    }
    subsidiary_jv_info_data["subsidiary"].append(subsidiary_info)

print(subsidiary_jv_info_data)

# Setting up Jinja2 environment
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

template = env.get_template('subs.tex')

# Rendering the template with the extracted data
output = template.render(
    subsidiary=subsidiary_jv_info_data['subsidiary'],
    JV_information=subsidiary_jv_info_data['JV_information']
)

# Saving the output to a file
with open('subsidiary_jv_output.tex', 'w') as f:
    f.write(output)

print("LaTeX document has been generated and saved to 'subsidiary_jv_output.tex'")
print(output)