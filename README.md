# Sistema de estoque de matéria prima

## Projeto elaborado como etapa do processo seletivo de estágio Tech da startup Seu Boné

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
* [Git](https://git-scm.com)
* [Python 3](https://www.python.org/)
* [Django](https://www.djangoproject.com/). 
* Além disto é bom ter um editor para trabalhar com o código, como [VSCode](https://code.visualstudio.com/)

### Iniciando o servidor
#### Clone este repositório

git clone <https://github.com/malubritoc/processo_seubone>


#### Acesse a pasta do projeto no terminal/cmd

cd processo_seubone

#### Execute a aplicação em modo de desenvolvimento

python manage.py runserver

##### O servidor inciará na porta 8000 - acesse <http://localhost:8000>

### Observações sobre a função ˜Filtrar˜: 
<h4>A função ˜Filtrar" ainda está pendente de modificações para sua plena execução, vez que ainda apresenta alguns bugs de visualização. Considerando isso, vale esclarecer as orientações de uso da função nos moldes atuais:

a) Primeiramente, o usuário deve escolher o parâmetro pelo qual deseja filtrar os itens: "Referência", "Tecido" ou "Cor", clicando no respectivo botão (lembrando que, até o momento atual, só é possível realizar essa ação com um único parâmetro);

a.1 Neste momento, será possível visualizar o bug citado anteriormente, pois devem aparecer três campos vazios, ao invés de somente um.

b) Nesse sentido, para obter o resultado desejado, o usuário deve digitar/selecionar o conteúdo do parâmetro no campo vazio de input respectiva à posição do parâmetro selecionado (respeitando, portanto, a ordem 1-Referência, 2-Tecido, 3-Cor, logo, caso queira filtrar pela referência deve ser utilizado o primeiro campo - o mais á esquerda; pelo tecido, o segundo campo - o do meio; e, pela cor, o terceiro campo - o mais à direita);

a.2 Outro bug de visualização é que, após inputar o conteúdo do parâmetro, não haverão novos botões, apenas os que já apareciam a priori.

c) Diante disso, o usuário deve então clicar novamente no botão referente ao parâmetro selecionado no item a).

Dessa forma, será realizada a execução da filtragem conforme o parâmetro desejado, estando prejudicada somente o aspecto visual da funcionalidade

        
