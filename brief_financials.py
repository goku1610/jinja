import json
from jinja2 import Template

# File paths
json_file_path = 'saksham_op.json'
latex_template_path = 'brief_financials.tex'

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Extracting brief financials from the data
brief_financials = data["brief_financials"]

# Prepare the data for the LaTeX template
financials_data = []
for key, values in brief_financials.items():
    row = {"name": key.replace('_', ' ').title(), "values": [v["value"] for v in values]}
    financials_data.append(row)

# Reading the LaTeX template from the file
with open(latex_template_path, 'r') as file:
    latex_template = file.read()

# Rendering the LaTeX document
template = Template(latex_template)
rendered_latex = template.render(brief_financials=financials_data)

# Printing the rendered LaTeX document
print(rendered_latex)
