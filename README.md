# gecer
Gerador de certificados com templates SVG

**[Português]**

Um script que lê um arquivo txt e gera um documento para cada nome a partir de um template SVG com placeholders. Projetado para gerar certificados de conclusão de curso. Um nome em cada linha.

## Como usar

Os arquivos `nomes.txt` e `template.svg` vêm com exemplos de uso.

No arquivo `nomes.txt` coloque os nomes e informações complementares:

    Curso: Informática Básica
    Início: 01/05/2016
    Fim: 27/05/2016
    Carga horária: 30h
    
    Maria Joaquina Dalvarenga
    Pietro José Aquino
    Lourdes Roberta de Oliveira
    
    ------------
    
    Curso: Jardinagem
    Início: 09/05/2016
    Fim: 31/05/2016
    Carga horária: 45h
    
    Nícolas Norberto Nunes
    Olivério Eriberto Teixeira
    Francisco Ferreira Fagundes Filho

Para organização, são permitidas linhas de separação com hífens "-----" e linhas em branco, que são ignoradas pelo programa. Os campos são identificados pelo formato **Campo: Valor do campo**, e são substituídas no template SVG pelo placeholder **{campo}** (sempre em letras minúsculas). Qualquer linha em outro formato é considerada como um nome.

O texto é lido e executado em sequência, portanto ao adicionar/modificar o valor de um campo, ele valerá para todos os documentos gerados a partir daquela linha até ser modificado novamente.

## Requisitos

- Python 3
- Inkscape (para a geração de arquivos PDF)

Obs: Por default, o script assume que o Inkscape está instalado no sistema com as configurações padrão em português. Se o caminho (path) do programa Inkscape for diferente é necessário modificar a variável `inkscape_path` no início do arquivo `gecer.py`.

-----

**[English]**

A python script that reads a txt file with names and generates (both SVG and PDF) documents from a SVG template with placeholders.

Requires Inkscape to generate the PDF files.
