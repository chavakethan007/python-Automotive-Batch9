import xml.etree.ElementTree as et
# XML built-in module

a = et.parse(r"C:\Users\chava\OneDrive\Documents\python-Automotive-Batch9\Python\medicalissues.xml")   # Parse XML file
b = a.getroot()                     # Fetch root element

diseases = []

# Loop through each problem tag
for problem in b.findall('problem'):
    c = problem.find("Issue").text
    diseases.append(c)

# Sort alphabetically
diseases.sort()

print("Diseases:")
for i in diseases:
    print(i)
