from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import pandas as pd

class GetField():
    
    def __init__ (self, searchItem):
        self.searchItem = searchItem
        
    def GetTotalPages(self):
        url         =    f"https://lista.mercadolivre.com.br/{self.searchItem}"
        page        =    requests.get(url).text
        doc         =    BeautifulSoup(page, "html.parser")
        pageQtyRaw  =    str(doc.find(class_="andes-pagination__page-count"))
        try:
            return (pageQtyRaw.split(">")[2]).split("<")[0]
        except:
            return 1
            
            
    def Pricing(self,text):
        strText = str(text)
        firstSplit = strText.split('class="price-tag-text-sr-only">')
        secSplit = firstSplit[1].split(" reais")
        actualText = secSplit[0]
        if "Antes:" in actualText:
            actualText = actualText.split(" ")[1]
        if "centavos" in secSplit[1]:
            cents = f".{secSplit[1].split('con ')[1].split(' centavos')[0]}"  
            actualText = actualText + cents
        else: actualText = actualText + ".00"
            
        return actualText
    
    def Description(self,text):
        strText = str(text)
        firstSplit = strText.split('"ui-search-item__title shops__item-title">')
        secSplit = firstSplit[1].split("</h2>")
        actualText = secSplit[0]
        return actualText
    
    def Link(self, text):
        strText = str(text)
        firstSplit = strText.split('https://')
        secSplit = firstSplit[1].split('" class="')
        actualText = "https://" + secSplit[0]
        return actualText
    
    def GetAll(self):
        listall = []
        listToAppen = []
        pageQty = self.GetTotalPages()
        for i in tqdm(range(int(pageQty))):
            pageNumber = int(i)*50+1
            url2 = f"https://lista.mercadolivre.com.br/{self.searchItem}/{self.searchItem}_Desde_{pageNumber}_NoIndex_True"
            page2 = requests.get(url2).text
            doc2 = BeautifulSoup(page2, "html.parser")
            page_text2 = doc2.find_all(class_="ui-search-result__content-wrapper shops__result-content-wrapper")
            for text in page_text2:
                listToAppen.append(self.Description(text))
                listToAppen.append(self.Pricing(text))
                listToAppen.append(self.Link(text))
                listall.append(listToAppen)
                listToAppen = []
        return listall
        
    def GetAllDataFrame(self):
        df = pd.DataFrame(self.GetAll(), columns=['Description','Price','Link'])
        return df
