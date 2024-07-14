import json
from jinja2 import Template

# File paths
json_file_path = 'saksham_op.json'
latex_template_path = 'balance.tex'

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Extracting balance sheet analysis data from the JSON
balance_sheet_analysis = data["balance_sheet_analysis"]["table"]

years = [item["Year"] for item in balance_sheet_analysis["EquityCapital"]]
EquityCapital = [item["Value"] for item in balance_sheet_analysis["EquityCapital"]]
Reserves = [item["Value"] for item in balance_sheet_analysis["Reserves"]]
Borrowings = [item["Value"] for item in balance_sheet_analysis["Borrowings"]]
OtherLiabilities = [item["Value"] for item in balance_sheet_analysis["OtherLiabilities"]]
TotalLiabilities = [item["Value"] for item in balance_sheet_analysis["TotalLiabilities"]]
FixedAssets = [item["Value"] for item in balance_sheet_analysis["FixedAssets"]]
CWIP = [item["Value"] for item in balance_sheet_analysis["CWIP"]]
Investments = [item["Value"] for item in balance_sheet_analysis["Investments"]]
OtherAssets = [item["Value"] for item in balance_sheet_analysis["OtherAssets"]]
Inventories = [item["Value"] for item in balance_sheet_analysis["Inventories"]]
TradeReceivables = [item["Value"] for item in balance_sheet_analysis["TradeReceivables"]]
CashEquivalents = [item["Value"] for item in balance_sheet_analysis["CashEquivalents"]]
ShortTermLoans = [item["Value"] for item in balance_sheet_analysis["ShortTermLoans"]]
OtherAssetItems = [item["Value"] for item in balance_sheet_analysis["OtherAssetItems"]]
TotalAssets = [item["Value"] for item in balance_sheet_analysis["TotalAssets"]]

# Extracting commentary from the JSON
commentary = data["balance_sheet_analysis"]["commentary"]

balance_sheet_dict = {
    "years": years,
    "EquityCapital": EquityCapital,
    "Reserves": Reserves,
    "Borrowings": Borrowings,
    "OtherLiabilities": OtherLiabilities,
    "TotalLiabilities": TotalLiabilities,
    "FixedAssets": FixedAssets,
    "CWIP": CWIP,
    "Investments": Investments,
    "OtherAssets": OtherAssets,
    "Inventories": Inventories,
    "TradeReceivables": TradeReceivables,
    "CashEquivalents": CashEquivalents,
    "ShortTermLoans": ShortTermLoans,
    "OtherAssetItems": OtherAssetItems,
    "TotalAssets": TotalAssets,
    "commentary": commentary
}

# Reading the LaTeX template from the file
with open(latex_template_path, 'r') as file:
    latex_template = file.read()

# Rendering the LaTeX document
template = Template(latex_template)
rendered_latex = template.render(**balance_sheet_dict)

# Printing the rendered LaTeX document
print(rendered_latex)
