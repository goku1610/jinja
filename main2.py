import json
from jinja2 import Environment, FileSystemLoader

# Promoters JSON data
promoters_json = '''
{
  "names": [
    "Mr. Jayanti Patel", "Mr. Ashish Soparkar", "Mr. Natwarlal Patel", "Mr. Ramesh Patel",
    "Mr. Anand Patel", "Mr. Ankit Patel", "Mr. Karana Patel", "Mr. Darshan Patel",
    "Mr. Maulik Patel", "Mr. Kaushal Soparkar", "Shri Manubhai K. Patel", "Prof. (Dr.) Ganapati Yadav",
    "Ms. Urvashi Dhirubhai Shah", "Dr. Varesh Sinha", "Mr. Nikunt Raval"
  ],
  "experiences": [
    "47 yrs of experience in Overseas corporate affairs & finance. B.E (Chemical)",
    "46 yrs of experience in Overseas corporate affairs & finance. B.E (Chemical)",
    "45 yrs of experience in Overseas technical matters & marketing in Agrochemical division. MSc degree",
    "44 yrs of experience in Overseas purchasing function & liaisons with govt. / regulatory bodies. B.A degree",
    "35 yrs of experience in Overseas pigments marketing, manufacturing. BSc degree",
    "Over a decade in the chemical industry. Bachelorâ€™s degree in Chemical Engineering from S.P. University, Anand, a Masterâ€™s in Engineering from Griffith, Australia, and a Global MBA from SP Jain Centre of Management. Assumed the role of Chairman and Managing Director on August 14, 2023.",
    "Over a decade and a half of experience in Agrochemical operations. Diploma in Chemical Engineering from Nirma University and a Bachelorâ€™s degree in Chemical Engineering from Drexel University, USA. Assumed the role of Executive Director on August 14, 2023.",
    "Over a decade of experience in Pigment operations. Bachelorâ€™s degree in Chemical Engineering from Nirma University, a Masterâ€™s degree in Engineering Management from Griffith University, Australia, and an MBA from the New York Institute of Technology (NYIT) USA. Assumed the role of Executive Director on August 14, 2023.",
    "More than 16 years of experience in the chemical industry. BE (Chemical) from S.P. University, Anand, Masters of Science (Chemical Engineering) from University of Southern California, USA and MBA from Long Island University, USA.",
    "More than 15 years of experience in the chemical industry. B.S. (Chemical) from University of New Haven, USA and M.S. (Engineering Management) from Northeastern University, USA.",
    "More than 37 years of experience in the field of Forex, Treasury and Credit Management. Chartered Accountant.",
    "Padmashri Awardee, academician with B. Chem. Eng. Ph.D. (Tech.), D.Sc. (Hon. Causa, DYPK), FTWAS, FNA, FASc, FNASc, FNAE, FRSC (UK), FISTE , FIChemE (UK), FIIChE. Chairman, Research Council, CSIR-CSMCRI, member of RC of IICT Hyderabad and NIIST Trivandrum. Chairman, Advisory of DST-National Centre for Catalysis Research, IIT-Madras and international PAC in Chemical Sciences of DST. Chairman, Waste Management Expert Committee, DST-Govt of India, and serves on Boards of two companies as independent Director. Member of Maharashtra Innovation Council.",
    "Bachelor of Arts (BA) Degree with Economics and having First class First rank of Gujarat University. Advocate by profession and practicing with Income Tax appellate Tribunal since last 15 years.",
    "Master in Science (Mathematical Statistics) from Lucknow University and Doctor of Philosophy (Ph.D.) in Statistics. Joined the Indian Administrative Service in 1977 and retired in 2014. Held various eminent positions including Collector of Jamnagar, Managing Director in various Gujarat Government companies, Additional Chief Secretary and Chief Secretary â€“ Government of Gujarat. Served as State Election Commissioner from 2014 to 2019.",
    "Advocate practising in securities & Corporate Laws, Land Laws, Banking Law, Tax Law and Commercial Laws. Standing Counsel for the Union of India in the High Court of Gujarat from 2015 till 2023. Partner at Raval & Raval Advocates and Sr. Standing Counsel for the Income Tax Department and Customs, Excise, GST and DRI Department."
  ]
}
'''

# Load JSON data
promoters = json.loads(promoters_json)

# Combine names and experiences into a list of tuples
promoters_data = list(zip(promoters['names'], promoters['experiences']))

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader('./'))
template = env.get_template('template.tex')

# Render template with data
rendered_tex = template.render(promoters=promoters_data)

# Print the LaTeX output
print(rendered_tex)
