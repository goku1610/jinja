import json
from jinja2 import Environment, FileSystemLoader

# Function to escape LaTeX special characters and replace underscores with spaces
def escape_latex(text):
    """
    Escapes LaTeX special characters in the given text and replaces underscores with spaces.
    """
    if not isinstance(text, str):
        return text
    replacements = {
        '&': '\\&',
        '%': '\\%',
        '$': '\\$',
        '#': '\\#',
        '_': ' ',  # Replace underscores with spaces
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

# Extract and process cash flow data with LaTeX escaping
cash_flow_data = {
    "commentary": [escape_latex(comment) for comment in data["cash_flow_analysis"]["commentary"]],
    "graph": {
        "url": escape_latex(data["cash_flow_analysis"]["graph"]["url"])
    },
    "graph_commentary": [escape_latex(comment) for comment in data["cash_flow_analysis"]["graph_commentary"]]
}

table = data["cash_flow_analysis"]["table"]
cash_flow_data["table"] = {}

for category, details in table.items():
    years = [escape_latex(item["year"]) for item in details]
    values = [escape_latex(item["value"]) for item in details]
    cash_flow_data["table"][category] = {
        "Years": years,
        "Values": values
    }

# Setting up Jinja2 environment
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

template = env.get_template('cash.tex')

# Rendering the template with the extracted data
output = template.render(
    table=cash_flow_data['table'],
    commentary=cash_flow_data['commentary'],
    graph=cash_flow_data['graph'],
    graph_commentary=cash_flow_data['graph_commentary']
)

# Saving the output to a file
with open('cash_flow_output.tex', 'w') as f:
    f.write(output)

print("LaTeX document has been generated and saved to 'cash_flow_output.tex'")
print(output)