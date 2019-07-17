import pyodbc 
import xml.etree.cElementTree as ET
import datetime

date = datetime.datetime.now()
filename = date.strftime("%Y_%m_%d_%H_%M.xml")

# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=server_name;'
#                       'Database=db_name;'
#                       'Trusted_Connection=yes;')

# cursor = conn.cursor()
# cursor.execute('SELECT * FROM db_name.Table')

# for row in cursor:
#     print(row)


root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

tree = ET.ElementTree(root)
tree.write("parsed_" + filename)
