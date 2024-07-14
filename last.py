import json
from jinja2 import Environment, FileSystemLoader

file_path = 'saksham_op.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

brief_financials_json = '''
{'sales': [{'year': 'FY-20', 'value': 'NA'}, {'year': 'FY-21', 'value': 'NA'}, {'year': 'FY-22', 'value': 'NA'}, {'year': 'FY-23', 'value': 'NA'}, {'year': 'FY-24', 'value': 'NA'}], 'EBITDA': [{'year': 'FY-20', 'value': 'NA'}, {'year': 'FY-21', 'value': 'NA'}, {'year': 'FY-22', 'value': 'NA'}, {'year': 'FY-23', 'value': 'NA'}, {'year': 'FY-24', 'value': 'NA'}], 'PAT': [{'year': 'FY-20', 'value': '157'}, {'year': 'FY-21', 'value': '185'}, {'year': 'FY-22', 'value': '308'}, {'year': 'FY-23', 'value': '250'}, {'year': 'FY-24', 'value': '-57'}], 'total_equity_capital': [{'year': 'FY-20', 'value': '25'}, {'year': 'FY-21', 'value': '25'}, {'year': 'FY-22', 'value': '25'}, {'year': 'FY-23', 'value': '25'}, {'year': 'FY-24', 'value': '25'}], 'non_current_liabilities': [{'year': 'FY-20', 'value': 'NA'}, {'year': 'FY-21', 'value': 'NA'}, {'year': 'FY-22', 'value': 'NA'}, {'year': 'FY-23', 'value': 'NA'}, {'year': 'FY-24', 'value': 'NA'}], 'current_liabilities': [{'year': 'FY-20', 'value': 'NA'}, {'year': 'FY-21', 'value': 'NA'}, {'year': 'FY-22', 'value': 'NA'}, {'year': 'FY-23', 'value': 'NA'}, {'year': 'FY-24', 'value': 'NA'}], 'ebt_margin': [{'year': 'FY-20', 'value': 'NA'}, {'year': 'FY-21', 'value': 'NA'}, {'year': 'FY-22', 'value': 'NA'}, {'year': 'FY-23', 'value': 'NA'}, {'year': 'FY-24', 'value': 'NA'}], 'non_current_assets': [{'year': 'FY-20', 'value': 'NA'}, {'year': 'FY-21', 'value': 'NA'}, {'year': 'FY-22', 'value': 'NA'}, {'year': 'FY-23', 'value': 'NA'}, {'year': 'FY-24', 'value': 'NA'}], 'current_assets': [{'year': 'FY-20', 'value': 'NA'}, {'year': 'FY-21', 'value': 'NA'}, {'year': 'FY-22', 'value': 'NA'}, {'year': 'FY-23', 'value': 'NA'}, {'year': 'FY-24', 'value': 'NA'}], 'total_assets': [{'year': 'FY-20', 'value': '1652'}, {'year': 'FY-21', 'value': '1967'}, {'year': 'FY-22', 'value': '2733'}, {'year': 'FY-23', 'value': '3001'}, {'year': 'FY-24', 'value': '2790'}], 'return_on_equity': [{'year': 'FY-20', 'value': 'NA'}, {'year': 'FY-21', 'value': 'NA'}, {'year': 'FY-22', 'value': 'NA'}, {'year': 'FY-23', 'value': 'NA'}, {'year': 'FY-24', 'value': 'NA'}], 'current_ratio': [{'year': 'FY-20', 'value': 'NA'}, {'year': 'FY-21', 'value': 'NA'}, {'year': 'FY-22', 'value': 'NA'}, {'year': 'FY-23', 'value': 'NA'}, {'year': 'FY-24', 'value': 'NA'}], 'ebt_margin_percent': [{'year': 'FY-20', 'value': 'NA'}, {'year': 'FY-21', 'value': 'NA'}, {'year': 'FY-22', 'value': 'NA'}, {'year': 'FY-23', 'value': 'NA'}, {'year': 'FY-24', 'value': 'NA'}]}
'''

print(brief_financials_json)
# Load JSON data
brief_financials = json.loads(brief_financials_json)

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader('./'))
template = env.get_template('financials.tex')

# Render template with data
rendered_tex = template.render(**brief_financials)

# Print the LaTeX output
print(rendered_tex)