from tkinter.filedialog import askdirectory
import os

# Retirar o caminho do diretorio pelo usuário
caminho = askdirectory(title="Selecione a pasta")

# Criando a lista dos arquivos dentro do diretorio selecionado
lista_arquivos = os.listdir(caminho)

# Listar as pastas e os arquivos a serem inseridos nela
locais = {
    "Imagens": [".png", ".jpg", ".jpeg"],
    "Planilhas": [".xlsx", ".xls", ".xlsm"],
    "PDFs": [".pdf", ".ods"],
    "csv": [".csv"],
    "Texto": [".txt"]
}

# Loop para passar em todos os arquivos e colocar nas respectivas pastas
for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

print("Arquivos em suas devidas pastas!")
