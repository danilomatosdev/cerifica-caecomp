from PIL import Image, ImageDraw, ImageFont
import os

# Caminhos dos arquivos
TEMPLATE_PATH = "AUTO-PALE5H.png"
FONT_PATH = os.path.abspath("Barlow/Barlow-Medium.ttf")
FONT_BOLD_PATH = os.path.abspath("Barlow/Barlow-Medium.ttf")  # Caminho para a fonte em negrito
OUTPUT_FOLDER = "PALESTRAS/TODOS"
LISTA_PATH = "PALESTRANTES9.txt"  # Arquivo com os nomes

# Criar pasta de saída, se não existir
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Fonte e tamanho do texto
FONT_SIZE = 50
font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
font_bold = ImageFont.truetype(FONT_BOLD_PATH, FONT_SIZE)

# Dados fixos
NOME_PALESTRA = "Rally da Computação"
DIA_EVENTO = "13"  # Data do evento (dia)

# Função para quebrar o texto em múltiplas linhas
def quebrar_texto(texto, largura_maxima, font, font_bold, draw):
    linhas = []
    palavras = texto.split()
    linha_atual = ""
    
    for palavra in palavras:
        largura_palavra = draw.textbbox((0, 0), linha_atual + " " + palavra, font)[2] if linha_atual else draw.textbbox((0, 0), palavra, font)[2]
        
        if largura_palavra <= largura_maxima:
            linha_atual += " " + palavra
        else:
            if linha_atual:
                linhas.append((linha_atual.strip(), font))
            linha_atual = palavra
    
    if linha_atual:
        linhas.append((linha_atual.strip(), font))

    return linhas

# Função para centralizar o texto dentro do box
def centralizar_texto_no_box(draw, linhas, largura_imagem, altura_imagem, largura_box, altura_box, font):
    altura_total = sum([draw.textbbox((0, 0), linha, font)[3] - draw.textbbox((0, 0), linha, font)[1] for linha, _ in linhas])
    y_pos = (altura_imagem - altura_total) // 2

    for linha, fonte in linhas:
        text_width = draw.textbbox((0, 0), linha, fonte)[2] - draw.textbbox((0, 0), linha, fonte)[0]
        x_pos = (largura_imagem - text_width) // 2
        
        draw.text((x_pos, y_pos), linha, fill="#133dbc", font=fonte)
        y_pos += draw.textbbox((0, 0), linha, fonte)[3] - draw.textbbox((0, 0), linha, fonte)[1]

# Lendo os nomes do arquivo lista.txt
with open(LISTA_PATH, "r", encoding="utf-8") as arquivo:
    nomes = [linha.strip() for linha in arquivo.readlines() if linha.strip()]

# Gerar um certificado para cada nome
for nome_palestrante in nomes:
    # Carregar a imagem do certificado
    image = Image.open(TEMPLATE_PATH)
    draw = ImageDraw.Draw(image)

    # Texto do certificado
    texto_certificado = (
        f"Certificamos que {nome_palestrante} participou como ouvinte da palestra:\n"
        f"{NOME_PALESTRA} na 4ª Semana Integrada das Engenharias (SIENG) do "
        f"Centro Acadêmico de Engenharia da Computação (CAECOMP) na "
        f"Universidade do Estado de Minas Gerais, realizado dia {DIA_EVENTO} de fevereiro de 2025."
    )

    # Definir as dimensões do box
    largura_imagem, altura_imagem = image.size
    largura_box = largura_imagem - 500  

    # Quebrar o texto em linhas
    linhas = quebrar_texto(texto_certificado, largura_box, font, font_bold, draw)

    # Aplicar negrito no nome do palestrante
    for i in range(len(linhas)):
        linha, fonte = linhas[i]
        if nome_palestrante in linha or NOME_PALESTRA in linha or DIA_EVENTO in linha:
            linhas[i] = (linha, font_bold)

    # Centralizar o texto no box
    centralizar_texto_no_box(draw, linhas, largura_imagem, altura_imagem, largura_box, 100, font)

    # Salvar certificado gerado como PDF
    output_pdf_path = os.path.join(OUTPUT_FOLDER, f"{nome_palestrante}.pdf")
    image.convert("RGB").save(output_pdf_path, "PDF", resolution=100.0)

    print(f"Certificado gerado: {output_pdf_path}")

print("\n✅ Todos os certificados foram gerados e salvos como PDF!")
