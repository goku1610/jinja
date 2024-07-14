import json
from jinja2 import Template

# File paths
json_file_path = 'saksham_op.json'
latex_template_path = 'industry_risk.tex'

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Extracting industry risks from the data
industry_risks = data["industry_risks"]

names = [risk["sources"] for risk in industry_risks["risks"]]
experiences = [risk["risk"].replace('%', '\\%') for risk in industry_risks["risks"]]  # Replacing % with \%

# Creating the new dictionary for industry risks
industry_risks_dict = {
    "sources": names,
    "risk": experiences
}

# Combining the sources and risks into a list of tuples for industry risks
industry_risks_list = list(zip(industry_risks_dict["sources"], industry_risks_dict["risk"]))

# Reading the LaTeX template from the file
with open(latex_template_path, 'r') as file:
    latex_template = file.read()

# Rendering the LaTeX document
template = Template(latex_template)
rendered_latex = template.render(industry_risks=industry_risks_list)

# Printing the rendered LaTeX document
print(rendered_latex)
