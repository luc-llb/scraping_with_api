# Api utilizando Scraping
Esse projeto é dividido em 4 partes:
 1. Um teste de Scraping, obtendo dois PDFs do sute gov.br;
 2. Um teste de conversão de dados, extraindo as tabelas dos PDFs obtidos;
 3. Um teste de banco de dados, utilizando SQL;
 4. Um teste de desenvolvimento fullstack, utilizando o banco de dados anterior, uma API implementada em Python e um interface de usuário feita com Vue.js.


 ## Tecnologias utilizadas
 - Python;
 - SQL (MySQL);
 - Vue.js + Typescript;


 ## 📑 Como utilizar esse projeto


 ### 🛠 Ferramentas necessárias
 É importante que antes de tentar utilizar esse projeto você tenha instalado em sua máquina:
  - O Node.js, para utilizar a interface web do 4º teste;
  - O Python, preferencialmente na versão 3+, uma vez que a maior parte do projeto utiliza dessa linguagem;
  - Um SGDB que suporte SQL feito para MySQL, caso queira realizar o uso local, recomendo o Xampp que foi utilizado nesse projeto.


### 👩‍💻 Rodando os desafios
Cada parte do projeto que faz o uso do Python tem seu próprio arquivo `requirements.txt`, onde estão as dependências necessárias para seu funcionamento.


1. Crie um ambiente virtual `venv` para instalar as dependências:
```bash
python -m venv .venv
```


2. Ative o ambiente virtual:
```bash
source .venv/Scripts/activate
```
Caso esteja utilizando o VS Code, não se esqueça de selecionar o executável do python salvo em `.venv/Scripts/python.exe` como interpretador.
 - Para isso pressione **Ctrl+Shift+P** e procure por _"Python: select interpreter"ou similar.


3. Instale as dependências das seções que desejar:
```bash
pip install -r 1-scrpaing/requirements.txt 2-data_conversion/requirements.txt 4-front_and_back/back/requirements.txt
```


4. Caso deseje utilizar o banco de dados do terceiro desafio, utilize o script `create.sql` disponível na pasta `3-data_base` para criar a estrutura do banco (não foram compartilhados nenhum dos dados utilizados nessa etapa).


### 💻 Utilizando a aplicação web
É importante que você siga os passos acima para conseguir utilizar a aplicação web.


1. Para utilizar o back-end/api é necessário que o banco de dados esteja funcionando.


2. Cheque o arquivo `4-front_and_back/back/database.py` e tenha certeza que o usuário e senha para se conectar ao banco são as mesmas utilizadas.


3. Para levantar a API, utilize os comandos:
```bash
cd 4-front_and_back/
uvicorn back.main:app --reload
```
É importante que o uso do comando seja feito de fora da pasta `back/` uma vez que é esperado que essa pasta funcione como um pacote do python.


4. Após ter a API rodando, para rodar a interface web utilize os comandos:
```bash
cd front/interface/
npm install
npm run dev
```