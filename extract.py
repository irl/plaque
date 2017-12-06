import json
import re
import glob
from bs4 import BeautifulSoup

plaques = []

for scraped in glob.glob("*.html"):
  with open(scraped) as s:
    m = re.findall(r"CommemorativePlaque/([a-zA-Z]+)\.jpg", s.read())

    if len(m) > 0:
      image = m[0]


    s.seek(0)

    soup = BeautifulSoup(s, "lxml")
    pabout = None
    
    #soup = BeautifulSoup(s, from_encoding="iso-8859-1")
  
    aspnet_form = soup.find('form')
    
    paras = aspnet_form.find_all('p')
  
    # the following results from most pages having 5 paras, some 6, one 7, one 8 and a few 0 - i.e. non-existent entries
    
    if len (paras) == 0:
      pass # do nothing
  
    elif len(paras) == 8:
  
      pname = paras[0].text.strip()
      ploc = paras[4].text.split(':')[1].strip()
      parea = paras[5].text.split(':')[1].strip()
      ptype = paras[6].text.split(':')[1].strip()
      pabout = paras[7].text.split(':')[1].strip()
  
    else: 
      pname = paras[0].text.strip()
      ploc = paras[1].text.split(':')[1].strip()
      parea = paras[2].text.split(':')[1].strip()
      ptype = paras[3].text.split(':')[1].strip()
  
      if len (paras) >= 5:
        pabout = paras[4].text.split(':')[1].strip()
  
      if len (paras) >= 6:
        pabout += "\n" + paras[5].text.split(':')[1].strip()
  
      if len(paras) >= 7:
        pabout += "\n" + paras[6].text.split(':')[1].strip()
      
    file_text = {'name': pname,
                 'location': ploc,
                 'area': parea,
                 'type': ptype,
                 'about': pabout,
                 'image': image + ".jpg"}
    plaques.append(file_text)

print(json.dumps({"plaques": plaques}))
