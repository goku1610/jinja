import json
from jinja2 import Template

# File paths
json_file_path = 'saksham_op.json'
latex_template_path = 'own.tex'

# Open and read the JSON file
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extracting ownership structure data from the JSON
graphs_data = data["ownership_structure"]

graphs = {
    "name": graphs_data["graphs"]["name"],
    "url": graphs_data["graphs"]["url"]
}

commentary = graphs_data["commentary"]

ownership_structure_dict = {
    "graphs": zip(graphs["name"], graphs["url"]),
    "commentary": commentary
}

# Reading the LaTeX template from the file
with open(latex_template_path, 'r', encoding='utf-8') as file:
    latex_template = file.read()

# Rendering the LaTeX document
template = Template(latex_template)
rendered_latex = template.render(**ownership_structure_dict)

# Saving the rendered LaTeX document
output_file_path = 'ownership_structure_analysis.tex'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(rendered_latex)
print(f'Rendered LaTeX document saved to {output_file_path}')
