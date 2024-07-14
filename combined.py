import json
import re
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
        '_': '\\_',
        '{': '\\{',
        '}': '\\}',
        '~': ' ',
        '^': ' ',
        '\n': '',
    }
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text

# File paths
json_file_path = 'saksham_op.json'
latex_template_path = 'combined.tex'
output_file_path = 'credit_appraisal_output.tex'

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Extracting data from the JSON
company_profile = data["company_profile"]
promoter_data = data["promoters"]
key_issues = data["key_issues"]
key_strengths = data["key_strengths"]
industry_risks = data["industry_risks"]
brief_financials = data["brief_financials"]
peer_ratings = data["peer_ratings"]

# Cleaning and formatting company profile data
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

# Preparing promoter data
names = [escape_latex(promoter["name"]) for promoter in promoter_data["promoters"]]
experiences = [escape_latex(promoter["experience"]) for promoter in promoter_data["promoters"]]

promoters_dict = {
    "names": names,
    "experiences": experiences
}

# Preparing key issues data
key_issues_list = [
    (escape_latex(issue["point_header"]), escape_latex(issue["point_content"]))
    for issue in key_issues["issues"]
]

# Preparing key strengths data
key_strengths_list = [
    (escape_latex(strength["point_header"]), escape_latex(strength["point_content"]))
    for strength in key_strengths["strengths"]
]

# Preparing industry risks data
industry_risks_list = [
    (escape_latex(risk["sources"]), escape_latex(risk["risk"]))
    for risk in industry_risks["risks"]
]

# Preparing brief financials data
financials_data = []
for key, values in brief_financials.items():
    row = {
        "name": escape_latex(key.replace('_', ' ').title()),
        "values": [escape_latex(v["value"]) if v["value"] != 'NA' else 'NA' for v in values]
    }
    financials_data.append(row)

# Preparing peer ratings data
peer_ratings_list = [
    {
        "company_name": escape_latex(rating["company_name"]),
        "long_term_rating": escape_latex(rating["long_term_rating"]),
        "short_term_rating": escape_latex(rating["short_term_rating"])
    }
    for rating in peer_ratings["ratings"]
]

peer_ratings_commentary = [escape_latex(comment) for comment in peer_ratings["commentary"]]

# Setup Jinja2 environment and load template file
financial_data = data["financial_data"]["table"]

years = [item["Quarter"] for item in financial_data["Sales"]]
value_sales = [item["Value"] for item in financial_data["Sales"]]
value_expenses = [item["Value"] for item in financial_data["Expenses"]]
OperatingProfit = [item["Value"] for item in financial_data["OperatingProfit"]]
OPM = [item["Value"] for item in financial_data["OPM %"]]
OtherIncome = [item["Value"] for item in financial_data["OtherIncome"]]
Interest = [item["Value"] for item in financial_data["Interest"]]
Depreciation = [item["Value"] for item in financial_data["Depreciation"]]
ProfitBeforeTax = [item["Value"] for item in financial_data["ProfitBeforeTax"]]
TaxPercentage = [item["Value"] for item in financial_data["TaxPercentage"]]
NetProfit = [item["Value"] for item in financial_data["NetProfit"]]
EPS = [item["Value"] for item in financial_data["EPS"]]

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
    "EPS": EPS
}

financial_commentary = [escape_latex(comment) for comment in data["financial_data"]["commentary"]]

# Setup Jinja2 environment and load template file
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
    "TotalAssets": TotalAssets
}

balance_sheet_commentary = [escape_latex(comment) for comment in data["balance_sheet_analysis"]["commentary"]]

# Setup Jinja2 environment and load template file
leverage_ratio_data = data["leverage_ratio"]
leverage_ratio_graphs = [{"name": key, "url": value["url"]} for key, value in leverage_ratio_data["graphs"].items()]
leverage_ratio_commentary = [escape_latex(comment) for comment in leverage_ratio_data["commentary"]]

# Extracting performance ratios data
performance_ratios_data = data["performance_ratios"]
performance_ratio_graphs = [{"name": key, "url": value["url"]} for key, value in performance_ratios_data["graphs"].items()]
performance_ratio_commentary = [escape_latex(comment) for comment in performance_ratios_data["commentary"]]

# Extracting activity ratios data
activity_ratios_data = data["activity_ratio"]
activity_ratio_graphs = [{"name": key, "url": value["url"]} for key, value in activity_ratios_data["graphs"].items()]
activity_ratio_commentary = [escape_latex(comment) for comment in activity_ratios_data["commentary"]]

# Extracting valuation ratios data
# valuation_ratios_data = data["valuation_ratios"]
# valuation_ratio_graphs = [{"name": key, "url": value["url"]} for key, value in valuation_ratios_data["graphs"].items()]
# valuation_ratio_commentary = [escape_latex(comment) for comment in valuation_ratios_data["commentary"]]

# Setup Jinja2 environment and load template file
ownership_structure_data = data["ownership_structure"]
ownership_structure_graphs = [{"name": key, "url": value["url"]} for key, value in ownership_structure_data["graphs"].items()]
ownership_structure_commentary = [escape_latex(comment) for comment in ownership_structure_data["commentary"]]

# Setup Jinja2 environment and load template file
subsidiary_jv_info_data = {
    "subsidiary": [],
    "JV_information": [escape_latex(jv) for jv in data["subsidiary_jv_info"]["JV information"]]
}

subsidiaries = data["subsidiary_jv_info"]["subsidiary"]
for subsidiary in subsidiaries:
    subsidiary_info = {
        "subsidiary_name": escape_latex(subsidiary["subsidiary_name"]),
        "Date_of_Creation": escape_latex(subsidiary["Date of Creation"]),
        "Interest": escape_latex(subsidiary["Interest"]),
        "Location": escape_latex(subsidiary["Location"])
    }
    subsidiary_jv_info_data["subsidiary"].append(subsidiary_info)

# Setup Jinja2 environment and load template file
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
    years = [item["year"] for item in details]
    values = [item["value"] for item in details]
    cash_flow_data["table"][category] = {
        "Years": years,
        "Values": values
    }
financial_analysis_data = {
    "Profitability": {},
    "commentary": [escape_latex(comment) for comment in data["financial_analysis"]["commentary"]]
}

profitability = data["financial_analysis"]["Profitability"]
for metric, details in profitability.items():
    years = [item["year"] for item in details]
    values = [item["value"] for item in details]
    financial_analysis_data["Profitability"][metric] = {
        "Years": years,
        "Values": values
    }

print(financial_analysis_data)

# Setup Jinja2 environment and load template file
env = Environment(loader=FileSystemLoader('.'))
env.filters['escape_latex'] = escape_latex
template = env.get_template(latex_template_path)

# Render the template with the combined data
rendered_str = template.render(
    company_profile=formatted_profile,
    promoters_dict=promoters_dict,
    key_issues=key_issues_list,
    key_strengths=key_strengths_list,
    industry_risks=industry_risks_list,
    brief_financials=financials_data,
    financial_dict=financial_dict,
    financial_commentary=financial_commentary,
    balance_sheet_dict=balance_sheet_dict,
    balance_sheet_commentary=balance_sheet_commentary,
    leverage_ratio_graphs=leverage_ratio_graphs,
    leverage_ratio_commentary=leverage_ratio_commentary,
    performance_ratio_graphs=performance_ratio_graphs,
    performance_ratio_commentary=performance_ratio_commentary,
    activity_ratio_graphs=activity_ratio_graphs,
    activity_ratio_commentary=activity_ratio_commentary,
    ownership_structure_graphs=ownership_structure_graphs,
    ownership_structure_commentary=ownership_structure_commentary,
    peer_ratings=peer_ratings_list,
    peer_commentary=peer_ratings_commentary,
    # debt_data=debt_data,
    # working_capital_data=working_capital_data,
    subsidiary_jv_info_data=subsidiary_jv_info_data,
    financial_analysis_data=financial_analysis_data
)

# Write the rendered template to the output file
with open(output_file_path, "w") as f:
    f.write(rendered_str)

print("Credit Appraisal LaTeX file has been generated and saved as credit_appraisal_output.tex")
print(rendered_str)
