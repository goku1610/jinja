import re
import json

import json

file_path = 'saksham_op.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# company_profile = data["company_profile"]
#
# def clean_text(text):
#     # Remove remaining \n and ** characters
#     text = text.replace('\n', ' ')
#     text = re.sub(r'\*\*', '', text)
#     return text
#
# def convert_to_list_format(profile):
#     formatted_profile = {}
#     for key, value in profile.items():
#         items = value.split('\n- ')
#         formatted_list = [clean_text(item.replace('- **', '').replace('**:', '')) for item in items]
#         formatted_profile[key] = formatted_list
#     return formatted_profile
#
# formatted_profile = convert_to_list_format(company_profile)
#
# print(json.dumps(formatted_profile, indent=2))
#

#
# promoter_data = data["promoters"]
#
#
# names = [promoter["name"] for promoter in promoter_data["promoters"]]
# experiences = [promoter["experience"] for promoter in promoter_data["promoters"]]
#
# # Creating the new dictionary
# promoters_dict = {
#     "names": names,
#     "experiences": experiences
# }
# #
# # Printing the new dictionary
# print(promoters_dict)
#
# key_strength = data["key_strengths"]
#
#
# names = [promoter["point_header"] for promoter in key_strength["strengths"]]
# experiences = [promoter["point_content"] for promoter in key_strength["strengths"]]
#
# # Creating the new dictionary
# key_strength_dict = {
#     "point_header": names,
#     "point_content": experiences
# }
#
# Printing the new dictionary
# print(key_strength_dict)
#
# key_issues = data["key_issues"]
#
#
# names = [promoter["point_header"] for promoter in key_issues["issues"]]
# experiences = [promoter["point_content"] for promoter in key_issues["issues"]]
#
# # Creating the new dictionary
# key_issues_dict = {
#     "point_header": names,
#     "point_content": experiences
# }
#
# # Printing the new dictionary
# print(key_issues_dict)
#
# industry_risks = data["industry_risks"]
#
#
# names = [promoter["sources"] for promoter in industry_risks["risks"]]
# experiences = [promoter["risk"] for promoter in industry_risks["risks"]]
#
# # Creating the new dictionary
# industry_risks_dict = {
#     "sources": names,
#     "risk": experiences
# }
#
# # Printing the new dictionary
# print(industry_risks_dict)
#
# brief_financials = data["brief_financials"]
#
#
# sales = [promoter["year"] for promoter in brief_financials["sales"]]
# value = [promoter["value"] for promoter in brief_financials["sales"]]
#
# # Creating the new dictionary
# brief_financials_dict = {
#     "sources": sales,
#     "risk": value
# }
#
# # Printing the new dictionary
# print(brief_financials)

# peer_ratings  = data["peer_ratings"]
#
# company_name = [promoter["company_name"] for promoter in peer_ratings["ratings"]]
# long_term_rating = [promoter["long_term_rating"] for promoter in peer_ratings["ratings"]]
# short_term_rating = [promoter["short_term_rating"] for promoter in peer_ratings["ratings"]]
#
# peer_ratings_dict = {
#     "company_name": company_name,
#     "long_term_rating": long_term_rating,
#     "short_term_rating": short_term_rating
# }
#
# print(peer_ratings_dict)
#
# print(peer_ratings["commentary"])

# financial_data = data["financial_data"]["table"]
#
# years = [promoter["Quarter"] for promoter in financial_data["Sales"]]
# value_sales = [promoter["Value"] for promoter in financial_data["Sales"]]
# value_expenses = [promoter["Value"] for promoter in financial_data["Expenses"]]
# OperatingProfit = [promoter["Value"] for promoter in financial_data["OperatingProfit"]]
# OPM = [promoter["Value"] for promoter in financial_data["OPM %"]]
# OtherIncome = [promoter["Value"] for promoter in financial_data["OtherIncome"]]
# Interest = [promoter["Value"] for promoter in financial_data["Interest"]]
# Depreciation = [promoter["Value"] for promoter in financial_data["Depreciation"]]
# ProfitBeforeTax = [promoter["Value"] for promoter in financial_data["ProfitBeforeTax"]]
# TaxPercentage = [promoter["Value"] for promoter in financial_data["TaxPercentage"]]
# NetProfit = [promoter["Value"] for promoter in financial_data["NetProfit"]]
# EPS = [promoter["Value"] for promoter in financial_data["EPS"]]
#
# financial_dict = {
#     "years": years,
#     "value_sales": value_sales,
#     "value_expenses": value_expenses,
#     "OperatingProfit": OperatingProfit,
#     "OPM": OPM,
#     "OtherIncome": OtherIncome,
#     "Interest": Interest,
#     "Depreciation": Depreciation,
#     "ProfitBeforeTax": ProfitBeforeTax,
#     "TaxPercentage": TaxPercentage,
#     "NetProfit": NetProfit,
#     "EPS": EPS
# }
#
# print(financial_dict)
#

# balance_sheet_analysis = data["balance_sheet_analysis"]["table"]
#
# years = [item["Year"] for item in balance_sheet_analysis["EquityCapital"]]
# EquityCapital = [item["Value"] for item in balance_sheet_analysis["EquityCapital"]]
# Reserves = [item["Value"] for item in balance_sheet_analysis["Reserves"]]
# Borrowings = [item["Value"] for item in balance_sheet_analysis["Borrowings"]]
# OtherLiabilities = [item["Value"] for item in balance_sheet_analysis["OtherLiabilities"]]
# TotalLiabilities = [item["Value"] for item in balance_sheet_analysis["TotalLiabilities"]]
# FixedAssets = [item["Value"] for item in balance_sheet_analysis["FixedAssets"]]
# CWIP = [item["Value"] for item in balance_sheet_analysis["CWIP"]]
# Investments = [item["Value"] for item in balance_sheet_analysis["Investments"]]
# OtherAssets = [item["Value"] for item in balance_sheet_analysis["OtherAssets"]]
# Inventories = [item["Value"] for item in balance_sheet_analysis["Inventories"]]
# TradeReceivables = [item["Value"] for item in balance_sheet_analysis["TradeReceivables"]]
# CashEquivalents = [item["Value"] for item in balance_sheet_analysis["CashEquivalents"]]
# ShortTermLoans = [item["Value"] for item in balance_sheet_analysis["ShortTermLoans"]]
# OtherAssetItems = [item["Value"] for item in balance_sheet_analysis["OtherAssetItems"]]
# TotalAssets = [item["Value"] for item in balance_sheet_analysis["TotalAssets"]]
#
# balance_sheet_dict = {
#     "years": years,
#     "EquityCapital": EquityCapital,
#     "Reserves": Reserves,
#     "Borrowings": Borrowings,
#     "OtherLiabilities": OtherLiabilities,
#     "TotalLiabilities": TotalLiabilities,
#     "FixedAssets": FixedAssets,
#     "CWIP": CWIP,
#     "Investments": Investments,
#     "OtherAssets": OtherAssets,
#     "Inventories": Inventories,
#     "TradeReceivables": TradeReceivables,
#     "CashEquivalents": CashEquivalents,
#     "ShortTermLoans": ShortTermLoans,
#     "OtherAssetItems": OtherAssetItems,
#     "TotalAssets": TotalAssets
# }
#
# print(balance_sheet_dict)
#
#
# print(graphs_data["commentary"])

# graphs_data = data["leverage_ratio"]
#
# result = {
#     "graphs": {
#         "name": [],
#         "url": []
#     }
# }
#
# for key, value in graphs_data["graphs"].items():
#     result["graphs"]["name"].append(key)
#     result["graphs"]["url"].append(value["url"])
# print(result)
# print(graphs_data["commentary"])
#
# graphs_data = data["performance_ratios"]
#
# result = {
#     "graphs": {
#         "name": [],
#         "url": []
#     }
# }
#
# for key, value in graphs_data["graphs"].items():
#     result["graphs"]["name"].append(key)
#     result["graphs"]["url"].append(value["url"])
# print(result)
# print(graphs_data["commentary"])
#
# graphs_data = data["activity_ratio"]
#
# result = {
#     "graphs": {
#         "name": [],
#         "url": []
#     }
# }
#
# for key, value in graphs_data["graphs"].items():
#     result["graphs"]["name"].append(key)
#     result["graphs"]["url"].append(value["url"])
# print(result)
# print(graphs_data["commentary"])


# graphs_data = data["ownership_structure"]
# #
# result = {
#     "graphs": {
#         "name": [],
#         "url": []
#     }
# }
#
# for key, value in graphs_data["graphs"].items():
#     result["graphs"]["name"].append(key)
#     result["graphs"]["url"].append(value["url"])
# print(result)
# print(graphs_data["commentary"])


# financial_data = {}
# table = data["company_financials"]
#
# for key, values in table["table"].items():
#     years = [item["Year"] for item in values]
#     values = [item["Value"] for item in values]
#     financial_data[key] = {
#         "Years": years,
#         "Values": values
#     }
#
# print(financial_data)
# print(table["commentary"])


# debt_data = {}
# table = data["debt_schedule"]["table"]
#
# for category, details in table.items():
#     debt_data[category] = {}
#     for key, values in details.items():
#         years = [item["Year"] for item in values]
#         values = [item["Value"] for item in values]
#         debt_data[category][key] = {
#             "Years": years,
#             "Values": values
#         }
#
# debt_data["commentary"] = data["debt_schedule"]["commentary"]
#
# print(debt_data)
#
# working_capital_data = {
#     "graph": {
#         "url": data["working_capital_movement"]["graph"]["url"]
#     },
#     "commentary": data["working_capital_movement"]["commentary"]
# }
#
# print(working_capital_data)

# fixed_assets_data = {}
# table = data["fixed_assets"]["table"]
#
# for category, details in table.items():
#     years = [item["Year"] for item in details]
#     values = [item["Value"] for item in details]
#     fixed_assets_data[category] = {
#         "Years": years,
#         "Values": values
#     }
#
# fixed_assets_data["commentary"] = data["fixed_assets"]["commentary"]
#
# print(fixed_assets_data)

financial_analysis_data = {
        "Profitability": data["financial_analysis"]["Profitability"],
        "commentary": data["financial_analysis"]["commentary"]
    }

print(financial_analysis_data)

cash_flow_data = {
    "commentary": data["cash_flow_analysis"]["commentary"],
    "graph": {
        "url": data["cash_flow_analysis"]["graph"]["url"]
    },
    "graph_commentary": data["cash_flow_analysis"]["graph_commentary"]
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
print(cash_flow_data)

# subsidiary_jv_info_data = {
#     "subsidiary": [],
#     "JV_information": data["subsidiary_jv_info"]["JV information"]
# }
#
# subsidiaries = data["subsidiary_jv_info"]["subsidiary"]
# for subsidiary in subsidiaries:
#     subsidiary_info = {
#         "subsidiary_name": subsidiary["subsidiary_name"],
#         "Date_of_Creation": subsidiary["Date of Creation"],
#         "Interest": subsidiary["Interest"],
#         "Location": subsidiary["Location"]
#     }
#     subsidiary_jv_info_data["subsidiary"].append(subsidiary_info)
#
# print(subsidiary_jv_info_data)