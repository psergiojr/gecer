from subprocess import call

# Endereço do arquivo de nomes:
arq_nomes = 'nomes.txt'
# Endereço do template SVG:
arq_template = 'template.svg'

# Lendo o arquivo para uma string de template
with open(arq_template, encoding='utf-8') as tmp:
    template = tmp.read()


with open(arq_nomes, encoding='utf-8') as nomes:
    for nome in nomes:
        nomearq = 'certif_' + nome.replace('\n', '') + '.svg'

        with open(nomearq, mode='w', encoding='utf-8') as arqSVG:
            arqSVG.write( template.format(nome.replace('\n', '')) )

        call(['inkscape', '-f', nomearq, '-A', nomearq.replace('.svg', '.pdf')])

