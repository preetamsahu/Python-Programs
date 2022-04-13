import pandas as pd
import xml.etree.ElementTree as et #helps to parse down
#to get the entire tree
tree=et.parse('studentdata.xml')#entire tree structure in xml parsed in tree object
#we can get the root node
rn=tree.getroot()
# print(rn)
cnames=['name','email','grade','age']
rows=[]
for n in rn:
    nm=n.attrib.get('name')
    em=n.find('email').text
    gr=n.find('grade').text
    ag=n.find('age').text
    rows.append({
        'name':nm,
        'email':em,
        'grade':gr,
        'age':ag
    })
df=pd.DataFrame(rows,columns=cnames)
print(df)