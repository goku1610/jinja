import json
from jinja2 import Template

# File paths
json_file_path = 'saksham_op.json'
latex_template_path = 'financial.tex'

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Extracting financial data from the JSON
financial_data = data["financial_data"]["table"]

years = [entry["Quarter"] for entry in financial_data["Sales"]]
value_sales = [entry["Value"] for entry in financial_data["Sales"]]
value_expenses = [entry["Value"] for entry in financial_data["Expenses"]]
OperatingProfit = [entry["Value"] for entry in financial_data["OperatingProfit"]]
OPM = [entry["Value"] for entry in financial_data["OPM %"]]
OtherIncome = [entry["Value"] for entry in financial_data["OtherIncome"]]
Interest = [entry["Value"] for entry in financial_data["Interest"]]
Depreciation = [entry["Value"] for entry in financial_data["Depreciation"]]
ProfitBeforeTax = [entry["Value"] for entry in financial_data["ProfitBeforeTax"]]
TaxPercentage = [entry["Value"] for entry in financial_data["TaxPercentage"]]
NetProfit = [entry["Value"] for entry in financial_data["NetProfit"]]
EPS = [entry["Value"] for entry in financial_data["EPS"]]

# Extracting commentary from the JSON
commentary = data["financial_data"]["commentary"]

financial_dict = {
    "years": years,
    "value_sales": value_sales,
    "value_expenses": value_expenses,
    "OperatingProfit": OperatingProfit,
    "OPM": OPM,
    "OtherIncome": OtherIncome,
    "Interest": Interest,
    "Depreciation": Depreciation,
    "ProfitBeforeTax": ProfitBeforeTax,
    "TaxPercentage": TaxPercentage,
    "NetProfit": NetProfit,
    "EPS": EPS,
    "commentary": commentary
}

# Reading the LaTeX template from the file
with open(latex_template_path, 'r') as file:
    latex_template = file.read()

# Rendering the LaTeX document
template = Template(latex_template)
rendered_latex = template.render(**financial_dict)

# Printing the rendered LaTeX document
print(rendered_latex)
