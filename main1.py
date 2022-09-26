import requests as req
from bs4 import BeautifulSoup
import json
import tqdm
import time



data={
    "data":[]
}

url='https://samara.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=Python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&search_field=name&area=113&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

resp=req.get(url,headers=headers)
soup=BeautifulSoup(resp.text,"lxml")
tags=soup.find_all(attrs={"data-qa":"serp-item__title"})
for iter in tqdm.tqdm(tags):
    time.sleep(2)
        
    url_object="https://samara.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&search_field=name&area=113&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=100"
    resp_object=req.get(url_object,headers=headers)
    soup_object=BeautifulSoup(resp_object.text,"lxml")
    tag_price=soup_object.find(attrs={"data-qa":"vacancy-serp__vacancy-compensation"}).text
    tag_region=soup_object.find(attrs={"data-qa":"vacancy-serp__vacancy-address"}).text
    tag_experience=soup_object.find(attrs={"data-qa":"vacancy-serp__vacancy_snippet_requirement"}).text
    data["data"].append({"Title":iter.text,"Salary":tag_price,"Region":tag_region,"Experience":tag_experience})
    print(iter.text,tag_price,tag_region,tag_experience)
    
    

    with open("data.json", "w",encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False)
