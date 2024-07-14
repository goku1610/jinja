import json
from jinja2 import Environment, FileSystemLoader

file_path = 'financials.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Define function to render template with Jinja2
def render_template(data):
    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('financials.tex')

    # Render template with data
    rendered_tex = template.render(data=data)

    return rendered_tex

# Generate LaTeX output
latex_output = render_template(data)

# Print the LaTeX output
print(latex_output)
