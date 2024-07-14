import json
from jinja2 import Template

# File paths
json_file_path = 'saksham_op.json'
latex_template_path = 'key_strengths.tex'

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Extracting key strengths from the data
key_strength = data["key_strengths"]

names = [promoter["point_header"] for promoter in key_strength["strengths"]]
experiences = [promoter["point_content"].replace('%', '\\%') for promoter in key_strength["strengths"]]  # Replacing % with \%

# Creating the new dictionary
key_strength_dict = {
    "point_header": names,
    "point_content": experiences
}

# Combining the headers and contents into a list of tuples
key_strengths = list(zip(key_strength_dict["point_header"], key_strength_dict["point_content"]))

# Reading the LaTeX template from the file
with open(latex_template_path, 'r') as file:
    latex_template = file.read()

# Rendering the LaTeX document
template = Template(latex_template)
rendered_latex = template.render(key_strengths=key_strengths)

# Printing the rendered LaTeX document
print(rendered_latex)