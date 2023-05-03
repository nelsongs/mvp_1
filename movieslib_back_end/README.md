# API do Back End da aplicação MoviesLib
## *MVP-1 do Curso de Engenharia de Software da PUC Rio*

Este projeto faz parte do escopo da aplicação desenvolvida para o MVP-1 da Disciplina **Desenvolvimento Full Stack Básico** do Curso de Engenharia de Software da PUC Rio. 

O projeto demonstra um pequeno aplicativo de desenvolvimento *Full Stack básico*, com a porção back end tendo a sua API de encapsulamento das funcionalidades de base de dados implementadas utilizando a linguagem de programação Python3.

A aplicação é minimalista, apenas para demonstrar o uso do conceito de *full stack* no desenvolvimento de uma aplicação web.

O script principal em Python, chamado de **app.py**, encapsula ainda, por meio de bibliotecas, a API de documentação open source **Swagger**, que padroniza a integração dos processos de definir, criar e documentar a aplicação, possuindo recuros como *endpoints*, dados recebidos, dados retornados, código HTTP e métodos de autenticação, entre outros. Apenas funcionalidades mínimas do **Swagger** são utilizados nesta aplicação.



## Como executar 

Clone as duas pastas do projeto, **movieslib_front_end** e **movieslib_back_end** a partir do meu repositário público [MVP_1](https://github.com/nelsongs/mvp_1/) no **GitHUB**.

Abra um Terminal ou Shell e vá para o diretório movieslib_back_end. A partir de lá, crie um ambiente virtual Python para rodar essa aplicação, da seguinte forma:

---
- python -m venv env
---

Esse comando criará o ambiente virtual onde essa aplicação será executada, resolvendo problemas de conflito entre ambientes python distintos que você possa ter.

Após criado o ambiente virtual, será necessário ativá-lo. Para isso, dependendo do seu Sistema Operacional, você utilizará um dos *scripts* presentes no diretório **env/Scripts** (ou **env\Scripts** no Windows). Provavelmente nos sistemas Unix-like, como o Mac OSX e o Linux, o comando seria:

---
- env/Scripts/activate
---

Para o caso específico do Windows, no qual você normalmente usa o PowerShell, o comando é:

---
- env\Scripts\Activate.ps1
---

Pronto, o ambiente virtual python deverá estar rodando, o qual você poderá confirmar pela **(env)** no início da sua linha de comando.

Se precisar desativar o ambiente virtual por qualquqer motivo, utilize o comando **env/deactivate ou env\deactivate** (Windows).

Em seguida, instale as bibliotecas listadas no arquivo `requirements.txt`, presente no mesmo diretório onde você se encontra com o Terminal/Shell aberto. As bibliotecas presentes nesse arquivo são dependências que a aplicação em python necessita. Instale-as por meio do seguinte comando:

---
- pip install -r requirements.txt
---

Na sequência, para executar a API que criará e gerenciará a base de dados, execute o seguinte comando:

---
- (env)$ flask run --host 0.0.0.0 --port 5000
---

Esse comando fará com que o servidor de dados SQLite3 espere requisições no endereço 127.0.0.1, na porta 5000. As requisições serão entregues por meio da aplicação de front end e serão recebidas e tratadas pela aplicação de back end, interfaceando com a camada de base de dados da aplicação.

Portanto, para que essa aplicação de ***back end*** rode e fique esperando requisições por parte da porção cliente (***front end***), é necessário abrir uma página no navegador, com o seguinte endereço:

---
- http://127.0.0.1:5000
---

Alternativamente você pode utilizar o endereço:

---
- http://localhost:5000
---

O navegador deve mostrar a página inicial **APIdoc**, na qual você encontra o ***Swagger*** e mais dois aplicativos semelhantes. Estamos dando preferência ao ***Swagger*** para fazer essa verificação inicial da aplicação, mas fique à vontade para usar qualquer dos três.

Feito isso, você agora pode rodar a aplicação front end, conforme explicitado no arquivo README.md daquele aplicativo, em ***movieslib_front_end***. Você poderá inserir dados e verificar o comportamento da aplicação.

Se estiver com a janela do Terminal/Shell ainda aberta, você poderá acompanhar o retorno dos códigos de execução no Terminal/Shell e verificar os dados sendo inseridos/deletados etc., clicando no db.sqlite3 dentro do diretório database.

Para dar um *refreh* no banco de dados, clique no ícone de refresh do banco de dados, na parte superior esquerda da tela de visualização dos dados. 

Boa sorte!
