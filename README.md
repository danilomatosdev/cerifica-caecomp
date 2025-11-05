# cerifica-caecomp

# 🧾 Gerador Automático de Certificados – SIENG / CAECOMP

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pillow](https://img.shields.io/badge/Lib-Pillow-yellow.svg)
![Status](https://img.shields.io/badge/Status-Ativo-success.svg)
![License](https://img.shields.io/badge/Licença-Livre-lightgrey.svg)

---

## 🎯 Objetivo

Este projeto automatiza a **geração de certificados personalizados em PDF** a partir de uma lista de nomes, utilizando um **template base** e **fontes customizadas**.  

Foi desenvolvido para a **4ª Semana Integrada das Engenharias (SIENG)** do **Centro Acadêmico de Engenharia da Computação (CAECOMP)**, mas pode ser facilmente adaptado para outros eventos, cursos ou palestras.

---

## ⚙️ Como Funciona

1. Lê um arquivo de texto (`PALESTRANTES9.txt`) com os nomes dos participantes.  
2. Usa uma imagem base (`AUTO-PALE5H.png`) como template de certificado.  
3. Renderiza o texto sobre o template com a biblioteca **Pillow (PIL)**, aplicando:
   - Quebra automática de linhas conforme o limite de largura.  
   - Centralização vertical e horizontal do texto.  
   - Fonte em **negrito** para destacar nome, palestra e data.  
4. Gera automaticamente um **PDF individual** para cada participante na pasta `PALESTRAS/TODOS`.

---

## 🧠 Recursos Principais

- 💡 **Centralização e quebra automática de texto**
- 🔠 **Fontes personalizadas** (ex: família *Barlow*)
- 🖼️ **Saída em alta qualidade** pronta para impressão
- ⚡ **Geração em massa** a partir de lista de nomes
- 📄 **Exportação automática** em formato PDF

---

## 📁 Estrutura Recomendada do Projeto
📦 projeto-certificados
┣ 📄 gerar_certificados.py
┣ 🖼️ AUTO-PALE5H.png
┣ 📂 Barlow/
┃ ┗ Barlow-Medium.ttf
┣ 📂 PALESTRAS/
┃ ┗ 📂 TODOS/
┗ 📄 PALESTRANTES9.txt

# 🧰 Dependências

- [Pillow](https://pypi.org/project/Pillow/) – Manipulação e renderização de imagens

Instalação:
```bash
pip install pillow

basta executar o script principal na raiz do projeto:
python gerar_certificados.py

Os certificados serão gerados automaticamente na pasta:
PALESTRAS/TODOS/

Personalização

Você pode alterar facilmente os seguintes parâmetros no código:

Variável	Descrição	Exemplo
TEMPLATE_PATH	Caminho da imagem base do certificado	"AUTO-PALE5H.png"
LISTA_PATH	Lista de nomes a serem processados	"PALESTRANTES9.txt"
NOME_PALESTRA	Nome da palestra ou evento	"Rally da Computação"
DIA_EVENTO	Data do evento	"13"
FONT_PATH	Caminho da fonte utilizada	"Barlow/Barlow-Medium.ttf"


Exemplo de Saída

Cada certificado é gerado automaticamente com o nome do participante centralizado e salvo como PDF:

PALESTRAS/TODOS/
 ┣ João Silva.pdf
 ┣ Maria Souza.pdf
 ┣ Pedro Santos.pdf
 ┗ ...

Créditos

Projeto desenvolvido por Danilo de Jesus Matos - Presidente do CAECOMP – UEMG Divinópolis 2024-25
Evento: 4ª Semana Integrada das Engenharias (SIENG 2025)
