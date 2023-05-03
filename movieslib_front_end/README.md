# Front End da aplicação MoviesLib
## *MVP-1 do Curso de Engenharia de Software da PUC Rio*

Este projeto faz parte do escopo da aplicação desenvolvida para o MVP-1 da Disciplina **Desenvolvimento Full Stack Básico**.

Foi desenvolvido utilizando **HTML5**, **CSS3** e **Javascript** puros, sem utilização de frameworks ou bibliotecas.

Trata-se de uma aplicação minimalista, de 1 página apenas, contendo uma aplicação simples de cadastramento e gerenciamento de filmes.

Visa ser a interface do usuário com a aplicação completa (*Full Stack*), que se utiliza de uma outra aplicação de *Back End* rodando em paralelo e responsável por executar a persistência e o gerenciamento da base de dados que suporta a aplicação. 

## Características:

- Simplista
- 1 página apenas
- *index.html* com estruturação básica para conter uma grade dividida em 4 áreas
- Toda a formatação da página é realizada por meio do arquivo **CSS3** _styles.css_, empregando o conceito de Grid
- Uso da linguagem **Javascript**, presente no arquivo *scripts.js* para responder aos eventos de cadastramento, exibição e eliminação de items da base de dados

> As rotinas Javascript desta aplicação  
> interfaceiam, via protocolos HTML POST e GET,  
> com a aplicação de _Back End_ escrita em linguagem **Python**  
> a qual, por sua vez, encapsula as funcionalidades necessárias  
> para gerenciar a persistência dos dados em uma base de dados **SQLite3**. 

---
## Como executar

Simplesmente baixe (clone) as duas pastas do projeto, **movieslib_front_end** e **movieslib_back_end** a partir do meu repositário público [MVP_1](https://github.com/nelsongs/mvp_1/) no **GitHUB**. Leia o arquivo ***README.md***, presente na raiz do diretório **movieslib_back_end**, que orienta como executar a aplicação de **Back End**, responsável por abrir e gerenciar a base de dados **SQLite3**, que suporta a persistência dos dados da aplicação.

Com a aplicação de **Back End** rodando, vá à raiz do diretório **movieslib_front_end** e execute o arquivo ***index.html***, clicando-o duas vezes com o seu mouse.

Se já houver dados na base de dados, estes serão exibidos na tela de exibição de dados, no painel direito da página web. 

Você pode inserir novos items no painel de entrada de dados, à esquerda. Basta clicar no primeiro campo e inserir o título do filme. No campo para o tipo de filme, clique na setinha para baixo que aparece no campo e escolha um tipo de filme. Caso não encontre o tipo de filme na lista suspensa, basta você escrever diretamente no campo de entrada de dados.

Faça o mesmo procedimento para o tipo de mídia em que se encontra o filme. 

Por fim, no último campo, você tem até 2000 caracteres para inserir uma descrição breve do filme. 

Com os dados todos inseridos, basta clicar no botão **Inserir** para ter seus novos dados exibidos na lista de exibição no painel direito, bem como a sua inserção na base de dados *SQLite3*, por meio da aplicação de **Back End** escrita em *Python*.

Note que, após a entrada dos dados, sua exibição no painel direito e sua gravação na base de dados, o cursor se posiciona no campo Titulo do filme para nova entrada de dados.

Caso deseje encerrar a aplicação, basta clicar no botão **Sair**.

Boa sorte!
