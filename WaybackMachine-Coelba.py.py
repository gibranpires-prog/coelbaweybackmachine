import requests
from datetime import datetime
import time

urls = [
    "https://www.neoenergia.com/documents/d/guest/fornecedores-homologados-materiais-rede",
    "https://www.neoenergia.com/documents/d/guest/fornecedores-homologados-materiais-rede1",
    "https://www.neoenergia.com/web/bahia",
    "https://www.neoenergia.com/web/bahia/sua-casa/normas-tecnicas",
    "https://www.neoenergia.com/fornecedores",
    "https://portalouvidoria.neoenergia.com/?empresa=1",
    "https://hoca.appsinapsisenergia.com/",
    "https://www.neoenergia.com/web/bahia/incorporacao-de-redes",
    "https://www.neoenergia.com/web/bahia/antecipacao-de-obras-da-distribuidora",
    "https://www.neoenergia.com/web/bahia/seu-negocio/projetistas-prestadores-de-servico",
]

def save_to_wayback(url, index, total ):
    print(f"\n🔄 ({index}/{total}) Tentando salvar: {url}")
    try:
        # Adicionado timeout de 60 segundos para nao travar o script
        response = requests.get("https://web.archive.org/save/" + url, timeout=60 )
        if response.status_code == 200:
            print(f"✅ Sucesso ao salvar {url}")
        else:
            print(f"⚠️ O site respondeu com codigo {response.status_code}, mas o processo continuara.")
    except Exception as e:
        print(f"❌ Erro ao processar {url}: {e}")

if __name__ == "__main__":
    inicio = datetime.now()
    print("🕒 Inicio:", inicio.strftime("%d/%m/%Y %H:%M:%S"))
    
    for i, url in enumerate(urls, start=1):
        save_to_wayback(url, i, len(urls))
        time.sleep(5)  # Aumentado para 5 segundos para ser mais gentil com o servidor
        
    fim = datetime.now()
    print(f"\n🎉 Processamento concluido em: {fim - inicio}")
