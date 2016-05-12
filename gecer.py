#!/usr/bin/env python3
# GeCer v0.1
#     Gerador de Certificados
#
# Copyright 2016 - Paulo Sérgio Jr <paulo.psw@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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

