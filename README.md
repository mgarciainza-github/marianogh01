# marianogh01: Instrucciones básicas
Instrucciones para set up de git en ubuntu con github (26 de mayo de 2023)
Estoy en la laptop Yoga510 desde cero
1) en un terminal: ssh-keygen (puede omitirse si uno ya tiene una clave generada...)
2) copiar el contenido de ./ssh/id_rsa.pub
3) abrir github.com, click en usuario >> settings >> SSH and GPG keys >> New SSH Key: pegar la clave
4) ssh -T git@github.com debe devolver: Hi mgarciainza-github! You've successfully authenticated, but GitHub does not provide shell access.
5) crear directorio en PC local y entrar
6) en web github.com ir a repositorio a clonar, click en "Code", Local, SSH y copiar 
7) git clone pegar_aca_repo_ssh
8) cd nombre_repo
9) git status
10) si es la primera vez es necesario: git config --global user.name "MGI"
11) si es la primera vez es necesario: git config --global user.email "mgi...@..com"
12) git add archivo.py
13) git commit -m "Se agregó archivo de python"
14) git remote (no lo hice es para saber a dónde hacer el push?? ver: https://www.freecodecamp.org/espanol/news/guia-para-principiantes-de-git-y-github/ )
15) git push


# Ejemplo creación de repo: marianogh02

Acabo de crear un repo nuevo online.

Para empezar github me dice que haga lo siguiente:

echo "# marianogh02" >> README.md

git init

git add README.md

git commit -m "first commit"

git branch -M main

git remote add origin git@github.com:mgarciainza-github/marianogh02.git

git push -u origin main

#############################################################################
Comandos git más usados: https://www.siteground.es/kb/comandos-git-mas-usados/?gclid=Cj0KCQjw98ujBhCgARIsAD7QeAh0jCd60oRunjJq5-KHTBet57HNOMK7lMmpQxRSz3I2oH89vvFdnSgaAtF3EALw_wcB
#############################################################################

Para clonar este repositorio en otra máquina:
git clone git@github.com:mgarciainza-github/marianogh02.git 
(no es necesario "mkdir marianogh02", clone crea la carpeta)


