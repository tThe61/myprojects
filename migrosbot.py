import requests
from bs4 import BeautifulSoup as bs

toplamurun = 0

print("""

  __  __ ___ ____ ____   ___  ____    ____   ___ _____ 
 |  \/  |_ _/ ___|  _ \ / _ \/ ___|  | __ ) / _ \_   _|
 | |\/| || | |  _| |_) | | | \___ \  |  _ \| | | || |  
 | |  | || | |_| |  _ <| |_| |___) | | |_) | |_| || |  
 |_|  |_|___\____|_| \_\\___/|____/  |____/ \___/ |_|  
                                                       

""")


aranan_url = "https://www.migros.com.tr/arama?q="

aranacak_urun = input("urun:")

r = requests.get(aranan_url+aranacak_urun)
soup = bs(r.content,"html.parser")

pages = len(soup.find_all("ul",attrs={"class":"pagination"})[0].find_all("li")) - 1

for pageNumber in range(1,pages+1):
    pageRequest = requests.get("https://www.migros.com.tr/arama?q="+aranacak_urun+"&sayfa="+str(pageNumber))
    pageSource = bs(pageRequest.content,"html.parser")
    urunler = pageSource.find_all("div",attrs={"class":"product-card"})
    
    for urun in urunler:
    	name = urun.find("h5",attrs={"class":"product-card-title"}).text
    	
    	price = urun.find("div",attrs={"class":"price-tag"}).find("span",attrs={"class":"value"}).text.strip()
    	
    	print(name,price,sep="\n")
    	print("#"*30)
    	
    	toplamurun+=1
    	
print("Toplam {} urun bulundu".format(toplamurun))
    	
