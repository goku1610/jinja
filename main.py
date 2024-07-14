import json
from jinja2 import Environment, FileSystemLoader

import json

file_path = 'saksham_op.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Print the data to verify it's been read correctly
# JSON data containing company profile information

# Load JSON data
company_profile = eval(company_profile_json)

# Define function to render template with Jinja2
def render_template(data):
    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('company_profile.tex')

    # Render template with data
    rendered_tex = template.render(company_profile=data)

    return rendered_tex

# Generate LaTeX output
latex_output = render_template(company_profile)

# Print the LaTeX output
print(latex_output)
