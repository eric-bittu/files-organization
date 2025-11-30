from pathlib import Path

# Pasta de downloads
pasta = ""
origem = Path.home() / pasta

# Loop pelos arquivos
def organizar():
    for arquivo in origem.iterdir():
        if arquivo.is_file():
        # Obtém a extensão do arquivo
            extensao = arquivo.suffix.lower()
        
        # Ignora arquivos sem extensão ou ocultos
            if not extensao: continue
            
        # Define a pasta de destino
            destino = origem / f"{extensao[1:].upper()}s"
            destino.mkdir(exist_ok=True)
        
        # Move o arquivo
            arquivo.rename(destino / arquivo.name)
            print(f"Movido: {arquivo.name}")