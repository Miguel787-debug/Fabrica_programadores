import bs4
import requests
import os

'''
exist_ok=True Verificar se a pasta ja existe no sistema através do nome. 
'''

os.makedirs('XKCD', exist_ok=True) 
for e in range(1,10):
    url = "https://xkcd.com/" + str(e) 
    XKCD = requests.get(url)  
    XKCD.raise_for_status()
    soup = bs4.BeautifulSoup(XKCD.text, 'html.parser') 
    
    comic_elem = soup.select('#comic img')[0] 
    comic_url = 'http:' + comic_elem.get('src')
    print(f'Baixando a imagem {comic_url}...') 
    res = requests.get(comic_url) 
    res.raise_for_status
    image_file = os.path.join('XKCD', os.path.basename(comic_url))
    
    with open(image_file, 'wb') as f:
        f.write(res.content)
    print(f'imagem salva em {image_file}')





