
import requests
import re

search_url = "https://online.aberdeencity.gov.uk/Services/CommemorativePlaque/PlaqueResult.aspx?Sub=0&Type=0&Area=0&Name=&Page="

plaque_ids = []

for search_page in range(1, 6):
  r = requests.get(search_url + str(search_page))
  m = re.findall(r"PlaqueDetail\.aspx\?Id=([0-9]+)", r.text)
  plaque_ids.extend(m)

plaque_url = "https://online.aberdeencity.gov.uk/Services/CommemorativePlaque/PlaqueDetail.aspx?Id="

for plaque_id in plaque_ids:
  r = requests.get(plaque_url + plaque_id)
  with open("plaque_" + plaque_id + ".html", "w") as o:
    o.write(r.text)
