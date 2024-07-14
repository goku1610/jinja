import json
from jinja2 import Template

# File paths
json_file_path = 'saksham_op.json'
latex_template_path = 'key_issues.tex'

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Extracting key issues from the data
key_issues = data["key_issues"]

names_issues = [issue["point_header"] for issue in key_issues["issues"]]
experiences_issues = [issue["point_content"].replace('%', '\\%') for issue in key_issues["issues"]]  # Replacing % with \%

# Creating the new dictionary for issues
key_issues_dict = {
    "point_header": names_issues,
    "point_content": experiences_issues
}

# Combining the headers and contents into a list of tuples for issues
key_issues_list = list(zip(key_issues_dict["point_header"], key_issues_dict["point_content"]))

# Reading the LaTeX template from the file
with open(latex_template_path, 'r') as file:
    latex_template = file.read()

# Rendering the LaTeX document
template = Template(latex_template)
rendered_latex = template.render(key_issues=key_issues_list)

# Printing the rendered LaTeX document
print(rendered_latex)