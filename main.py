from pathlib import Path

# Pasta de downloads
origem = Path.home() / "Downloads"

# Loop pelos arquivos
for arquivo in origem.iterdir():
    if arquivo.is_file():
        # Pega a extensão (ex: .pdf)
        extensao = arquivo.suffix.lower()
        
        # Ignora arquivos sem extensão ou ocultos
        if not extensao: continue
            
        # Define a pasta de destino (ex: Downloads/PDFs)
        # O [1:] remove o ponto do .pdf
        destino = origem / f"{extensao[1:].upper()}s"
        destino.mkdir(exist_ok=True)
        
        # Move o arquivo
        arquivo.rename(destino / arquivo.name)
        print(f"Movido: {arquivo.name}")