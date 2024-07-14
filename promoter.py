import json
from jinja2 import Template

# Correctly handle the file path
file_path = r'saksham_op.json'
template_path = r'promoter.tex'
output_file_path = r'output.tex'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

promoter_data = data["promoters"]


names = [promoter["name"] for promoter in promoter_data["promoters"]]
experiences = [promoter["experience"] for promoter in promoter_data["promoters"]]

# Creating the new dictionary
promoters_dict = {
    "names": names,
    "experiences": experiences
}
#
# Printing the new dictionary
print(promoters_dict)
# Read the template file
with open(template_path, 'r') as file:
    template_str = file.read()

# Render the template
template = Template(template_str)
rendered_str = template.render(promoters_dict=promoters_dict)

# Write the rendered template to the output file
with open(output_file_path, "w") as f:
    f.write(rendered_str)

print("LaTeX file has been generated and saved as output.tex")

print(rendered_str)