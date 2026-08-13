import fitz  # PyMuPDF
import requests
import re
import os
import zipfile
import time

def main():
    pdf_path = "faturas.pdf"
    if not os.path.exists(pdf_path):
        print(f"Erro: O ficheiro '{pdf_path}' não foi encontrado. Faz upload de um ficheiro com este nome!")
        return

    # Criar pasta temporária para as faturas
    os.makedirs("faturas_descarregadas", exist_ok=True)

    print("A abrir o ficheiro PDF principal...")
    doc = fitz.open(pdf_path)
    
    links_encontrados = {}
    
    # Extrair todos os links
    print("A procurar links nas páginas...")
    for page_num in range(len(doc)):
        page = doc[page_num]
        links = page.get_links()
        for link in links:
            if "uri" in link:
                uri = link["uri"]
                
                # Tentar encontrar o texto (ex: AIUC-1234-PT) por cima do link
                rect = link["from"]
                text = page.get_textbox(rect).strip()
                
                # Se não encontrar texto, damos um nome genérico
                if not text:
                    text = f"Fatura_Pagina{page_num+1}_{len(links_encontrados)+1}"
                
                # Limpar caracteres inválidos para nomes de ficheiros
                text = re.sub(r'[\\/*?:"<>|]', "", text)
                
                # Guardar link se ainda não for repetido
                if uri not in links_encontrados:
                    links_encontrados[uri] = text

    print(f"Foram encontrados {len(links_encontrados)} links únicos.")
    
    # Descarregar cada ficheiro
    sucesso = 0
    for i, (url, filename) in enumerate(links_encontrados.items()):
        if not filename.lower().endswith(".pdf"):
            filename += ".pdf"
            
        print(f"[{i+1}/{len(links_encontrados)}] A descarregar: {filename}")
        try:
            # Fingir ser um browser normal para evitar que o site bloqueie
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
            response = requests.get(url, headers=headers, timeout=15)
            
            if response.status_code == 200:
                with open(os.path.join("faturas_descarregadas", filename), "wb") as f:
                    f.write(response.content)
                sucesso += 1
            else:
                print(f"  -> Erro: Código HTTP {response.status_code}")
                
        except Exception as e:
            print(f"  -> Erro ao descarregar: {e}")
            
        time.sleep(1) # Pausa de 1 segundo para não sobrecarregar o site
        
    # Criar o ficheiro ZIP final
    print("\nA criar o ficheiro ZIP...")
    with zipfile.ZipFile("todas_as_faturas.zip", "w") as zipf:
        for root, _, files in os.walk("faturas_descarregadas"):
            for file in files:
                zipf.write(os.path.join(root, file), file)
                
    print(f"\nConcluído! {sucesso} faturas foram descarregadas.")

if __name__ == "__main__":
    main()
