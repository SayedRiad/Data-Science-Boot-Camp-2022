!pip install requests-html

from requests_html import HTMLSession
session = HTMLSession()

url = "https://www.bangla-kobita.com/"
r = session.get(url)
r.status_code

def all_poems(url, poem_name, poet_name):
  updated_url = url + poet_name + "/" + poem_name + "/"
  r = session.get(updated_url)
  #print(updated_url)
  poem_name_pattern = "body > div.container > div.row.body-content > div.col-md-8 > div:nth-child(5) > h1 > span"
  poet_name_text = "body > div.container > div.row.body-content > div.col-md-8 > div:nth-child(5) > div.author-name > a > span"
  poem = "body > div.container > div.row.body-content > div.col-md-8 > div:nth-child(5) > div.post-content.noselect"
  reading_time = "body > div.container > div.row.body-content > div.col-md-8 > div:nth-child(5) > div.post-summary"
  
  p_p = r.html.find(poem_name_pattern, first=True).text
  p_n = r.html.find(poet_name_text, first=True).text
  p = r.html.find(poem, first=True).text
  r_t = r.html.find(reading_time, first=True).text

  with open(f"{poet_name}/{poem_name}.txt", "w") as f:
      f.write(f"{p_p}\n{p_n}\n{p}\n\n{r_t}")

kabita = {"nazrulislam" : {"rubaiyat-e-omar-khayyam-26-to-30","1400-shal","akorun-piya","sokal-sondhya","onadrita","onaamika","onurodh","obsor","ovishap","orghyo"}, "rabindranath": {"akas","akormar-bibhrat","yudara","okkhomota","okkhoma","aychana","ostsokhi","yusamay","odhikar","yabusan"}, "jasimuddin": {"aunurodh","kabor","kobita","kollanye","kosmani","golpoburo","desh","nimontron","bidaay","rakhal-chale"}, "jibanananda": {"1333","jsudipneel14","oghran","jsudipneel11","onibar","onirban","ondhokar","oborodh","obosheshe","bidal"}, "madhusudan": {"kashiram-das","shakuntala","artha","amra","aasha","italy","koptakkonod","kobi","kobita","shoni"}}
url = "https://www.bangla-kobita.com/"
for i in kabita:
  for j in kabita[i]:
    all_poems(url, j, i)
  