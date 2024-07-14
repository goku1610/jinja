import json
from jinja2 import Template

# File paths
json_file_path = 'saksham_op.json'
latex_template_path = 'peer_ratings.tex'

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Extracting peer ratings from the data
peer_ratings = data["peer_ratings"]

company_names = [promoter["company_name"] for promoter in peer_ratings["ratings"]]
long_term_ratings = [promoter["long_term_rating"] for promoter in peer_ratings["ratings"]]
short_term_ratings = [promoter["short_term_rating"] for promoter in peer_ratings["ratings"]]
commentary = peer_ratings["commentary"]

# Creating the new dictionary for peer ratings
peer_ratings_dict = {
    "company_name": company_names,
    "long_term_rating": long_term_ratings,
    "short_term_rating": short_term_ratings
}

# Prepare the data for LaTeX template
peer_ratings_data = []
for i in range(len(company_names)):
    peer_ratings_data.append({
        "company_name": company_names[i],
        "long_term_rating": long_term_ratings[i],
        "short_term_rating": short_term_ratings[i]
    })

# Reading the LaTeX template from the file
with open(latex_template_path, 'r') as file:
    latex_template = file.read()

# Rendering the LaTeX document
template = Template(latex_template)
rendered_latex = template.render(peer_ratings=peer_ratings_data, commentary=commentary)

# Printing the rendered LaTeX document
print(rendered_latex)
