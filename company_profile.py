import json
import re
from jinja2 import Environment, FileSystemLoader

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

file_path = 'saksham_op.json'
template_path = 'company_profile.tex'
output_file_path = 'credit_appraisal_output.tex'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

company_profile = data["company_profile"]

def clean_text(text):
    # Remove remaining \n and ** characters
    text = text.replace('\n', ' ')
    text = re.sub(r'\*\*', '', text)
    return text

def convert_to_list_format(profile):
    formatted_profile = {}
    for key, value in profile.items():
        items = value.split('\n- ')
        formatted_list = [clean_text(item.replace('- **', '').replace('**:', '')) for item in items]
        formatted_profile[key] = formatted_list
    return formatted_profile

formatted_profile = convert_to_list_format(company_profile)

# Setup Jinja2 environment and load template file
env = Environment(loader=FileSystemLoader('.'))
env.filters['escape_latex'] = escape_latex
template = env.get_template(template_path)

# Render the template
rendered_str = template.render(company_profile=formatted_profile)

# Write the rendered template to the output file
with open(output_file_path, "w") as f:
    f.write(rendered_str)

print("Credit Appraisal LaTeX file has been generated and saved as credit_appraisal_output.tex")
print(rendered_str)