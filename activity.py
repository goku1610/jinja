import json
from jinja2 import Template

# File paths
json_file_path = 'saksham_op.json'
latex_template_path = 'activity.tex'

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Extracting activity ratios data from the JSON
graphs_data = data["activity_ratio"]

graphs = {
    "name": [],
    "url": []
}

for key, value in graphs_data["graphs"].items():
    graphs["name"].append(key)
    graphs["url"].append(value["url"])

commentary = graphs_data["commentary"]

activity_ratios_dict = {
    "graphs": zip(graphs["name"], graphs["url"]),
    "commentary": commentary
}

# Reading the LaTeX template from the file
with open(latex_template_path, 'r') as file:
    latex_template = file.read()

# Rendering the LaTeX document
template = Template(latex_template)
rendered_latex = template.render(**activity_ratios_dict)

# Printing the rendered LaTeX document
print(rendered_latex)
