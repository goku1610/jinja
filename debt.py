import json
from jinja2 import Environment, FileSystemLoader

# Function to escape LaTeX special characters
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

# Path to your JSON file
file_path = 'saksham_op.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Data extraction function with LaTeX escaping
def extract_debt_data(data):
    debt_data = {}
    table = data["debt_schedule"]["table"]

    for category, details in table.items():
        debt_data[category] = {}
        for key, values in details.items():
            years = [escape_latex(item["Year"]) for item in values]
            values = [escape_latex(item["Value"]) for item in values]
            debt_data[category][key] = {
                "Years": years,
                "Values": values
            }

    debt_data["commentary"] = [escape_latex(comment) for comment in data["debt_schedule"]["commentary"]]
    return debt_data

# Extracting the data
debt_data = extract_debt_data(data)

# Setting up Jinja2 environment
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

template = env.get_template('debt.tex')

# Rendering the template with the extracted data
output = template.render(borrowings=debt_data['borrowings'], other_liabilities=debt_data['other_liabilities'], commentary=debt_data['commentary'])

# Saving the output to a file
with open('debt_schedule_output.tex', 'w') as f:
    f.write(output)

print("LaTeX document has been generated and saved to 'debt_schedule_output.tex'")
print(output)