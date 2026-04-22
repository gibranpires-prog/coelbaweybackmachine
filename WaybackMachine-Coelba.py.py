import requests
from datetime import datetime
import time

# Lista com os links a serem salvos
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

def save_to_wayback(url, index, total):
    print(f"\n🔄 ({index}/{total}) Salvando: {url}")
    response = requests.get("https://web.archive.org/save/" + url)
    if response.status_code == 200:
        print(f"✅ Sucesso ao salvar {url}")
    else:
        print(f"❌ Falha ao salvar {url} - Código: {response.status_code}")

if __name__ == "__main__":
    inicio = datetime.now()
    print("🕒 Início:", inicio.strftime("%d/%m/%Y %H:%M:%S"))
    print(f"🔧 Total de links: {len(urls)}")

    for i, url in enumerate(urls, start=1):
        save_to_wayback(url, i, len(urls))
        time.sleep(2)  # Pequeno intervalo para evitar bloqueio

    fim = datetime.now()
    duracao = fim - inicio
    print("\n🎉 Todos os links foram processados!")
    print("🕓 Fim:", fim.strftime("%d/%m/%Y %H:%M:%S"))
    print(f"⏱️ Duração total: {duracao}")

# input("\nPressione Enter para sair...")
