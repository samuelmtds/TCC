from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from time import time
from time import sleep
from random import randint

headers = {"Accept-Language": "pt-BR, en;q=0.5"}

# Defininando o range da página
pages = [str(i) for i in range(1,10000,50)]
print("Páginas que serão raspadas", pages)

# Lista dos dados que serão raspados
names = []
years = []
certificates = []
runtimes = []
genres = []
imdb_ratings = []
metascores = []
votes = []
list_gross = []

# Definindo as variaveis que irão monitorarar o loop
start_time = time()
requests = 0
contador = 1

# Qualquer página que está no intervalor defininido no range que irá entrar no loop
for page in pages:
        # Criando o request da página
        response = get('https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31&sort=num_votes,desc&start=' + page + '&ref_=adv_nxt', headers = headers)
        print('Estamos na página - >',page)
        
        # O tempo de pausa no loop
        sleep(randint(8,15))

        # Monitorando os requests 
        requests += 1
        elapsed_time = time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))

        # Retorna o erro caso haja um status fora de 200
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))

        # Parseando a url do request através BeautifulSoup
        page_html = BeautifulSoup(response.text, 'html.parser')

        # Seleciona os 50 containers dos filmes de uma única página 
        mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

        # Extraindo a informação da lista de 50 filmes
        for container in mv_containers:
            # Se o filme possui Metascore, então iremos extrair:
            if container.find('div', class_ = 'ratings-metascore') is not None:
                
                # Nome
                name = container.h3.a.text
                names.append(name)
                print(contador,name)

                # Ano
                year = container.h3.find('span', class_ = 'lister-item-year').text
                years.append(year)

                # Classificação Indicativa
                spans_certificate = container.find_all('span', class_ = 'certificate')
                size_certificate = len(spans_certificate)
                if size_certificate == 1 :
                    certificate = container.find('span', class_ = 'certificate').text
                    certificates.append(certificate)
                else:
                    certificate = 0
                    certificates.append(certificate)

                # Tempo de filme
                runtime = container.find('span', class_ = 'runtime').text
                runtimes.append(runtime)

                # Gênero
                genre = container.find('span', class_ = 'genre').text
                tratamento_genre = genre.replace('\n', '')
                genres.append(tratamento_genre)

                # IMDB rating
                imdb = container.strong.text
                imdb_ratings.append(imdb)

                # Metascore
                m_score = container.find('span', class_ = 'metascore').text
                metascores.append(int(m_score))

                # Número de votos
                vote = container.find('span', attrs = {'name':'nv'})['data-value']
                votes.append(int(vote))

                # Bilheteria
                spans_gross = container.find_all('span', attrs = {'name':'nv'})
                size_gross = len(spans_gross)
                if size_gross == 2 :
                    gross = container.find('span', attrs = {'name':'nv'}).find_next_sibling('span', attrs = {'name':'nv'})['data-value']
                    tratamento_gross = (gross).replace('.','')
                    list_gross.append(int(tratamento_gross))
                else:
                    gross = 0
                    list_gross.append(gross)

                #Para saber quantos filmes foram coletados no scrap
                contador += 1

webscrapping_df = pd.DataFrame({
        'Filme': names,
        'Ano': years,
        'Classificação Indicativa':certificates,
        'Tempo de filme' : runtimes,
        'Gênero': genres,
        'Imdb': imdb_ratings,
        'Metascore': metascores,
        'Votos': votes,
        'Bilheteria' : list_gross,
        })
        
print(webscrapping_df.info())
print(webscrapping_df)

webscrapping_df.to_excel(r'./imdb_web_scrapping_v4.xlsx', index = False, header=True)