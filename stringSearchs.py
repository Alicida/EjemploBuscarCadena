from os import path
from datetime import date
from datetime import datetime
import xlsxwriter
import pandas as pd
import urllib.request
import requests
from requests.exceptions import HTTPError


def buscartexto(fname):
   
    dataCrudo = pd.read_csv("ListaUrls.csv", sep=',')
    data = dataCrudo.fillna(value="Vacio")
    data['Resultado'] = "Vacio"
    print(data)
    for index, link in data.iterrows():
        try:
            print(link['URL'])
            req = urllib.request.Request(
                link['URL'],
                data=None,
                headers={
                    'User-Agent': 'Mozilla/5.0 '
                    '(Macintosh; Intel Mac OS X 10_9_3) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/35.0.1916.47 Safari/537.36'
                }
            )
            fp = urllib.request.urlopen(req)
        except:
            pass
        else:
            mybytes = fp.read()
            mystr = mybytes.decode("utf8", errors="ignore")
            substring = fname
            if substring in mystr:
                link['Resultado'] = 'Encontrado'
            else:
                link['Resultado'] = 'No encontrado'
            fp.close()
    today = date.today()
    now = datetime.now()
    strnow = str(today)+"_"+str(now.hour)+str(now.minute)+str(now.second)
    data.to_excel("ResultadoBusqueda"+strnow+".xlsx")
    if path.exists("ResultadoBusqueda"+strnow+".xlsx"):
        print('Archivo listo')
    else:
        print('Algo salió mal')
