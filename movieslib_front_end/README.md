# Front End da aplicação MoviesLib
## _MVP-1 do Curso de Engenharia de Software da PUC Rio_

Este projeto faz parte do escopo da aplicação desenvolvida para o MVP-1 da Disciplina **Desenvolvimento Full Stack Básico**.

O Front End foi desenvolvido utilizando **HTML5**, **CSS3** e **Javascript**.

Trata-se de uma aplicação minimalista, de 1 página apenas, contendo uma aplicação simples de cadastramento e gerenciamento de filmes.

A idéia da aplicação é seguir o direcionamento de interligá-la a uma aplicação de _Back End_ que gerencia a base de dados que guarda persistentemente os dados inseridos pela aplicação de _Front End_. 

## Características:
- Simplista
- 1 página apenas
- **HTML5** (_index.html_) com estruturação básica para conter uma grade dividida em 4 áreas
- Toda a formatação da página é realizada por meio do arquivo **CSS3** _styles.css_, empregando o conceito de Grid
- Uso da linguagem **Javascript**, presente no arquivo _scripts.js_ para responder aos eventos de cadastramento, exibição e eliminação de items

> As rotinas Javascript desta aplicação
> interfaceiam, via protocolos HTML POST e GET,
> com a aplicação de _Back End_ escrita em linguagem **Python**
> a qual, por sua vez, encapsula as funcionalidades necessárias
> para gerenciar a persistência dos dados em uma base de dados **SQLite3**. 

---
## Como executar

Simplesmente baixe (clone) as duas pastas do projeto, **movieslib_front_end** e **movieslib_back_end** a partir do meu repositário público [MVP_1](https://github.com/nelsongs/mvp_1/) no **GitHUB**. Leia o arquivo **_README.md_** presente na raiz do diretório **movieslib_back_end** para rodar a aplicação de **Back End** que abrirá e gerenciará a base de dados **SQLite3**.

Coma a aplicação de **Back End** rodando, vá à raiz do diretório **movieslib_front_end** e execute o arquivo _index.html_, clicando-o duas vezes com o seu mouse.

Se já houver dados na base de dados, estes serão exibidos na tela de exibição de dados, no painel direito da página web. 

Você pode inserir novos items no painel de entrada de dados, à esquqerda. Basta clicar no primeiro campo, inserir o título do filme. No campo para o tipo de filme, você clica na setinha para baixo que aparece no campo e escolhe um tipo de filme. Caso não encontre o tipo de filme na lista suspensa que aparece, basta você escrever diretamente no campo.

Faça o mesmo procedimento para o tipo de mídia em que se encontra o filme. Por fim, você tem até 2000 caracteres para inserir uma descrição breve do filme no campo seguinte. 

Com os dados todos inseridos, basta clicar no botão **Inserir** para ter seus novos dados exibidos na lista de exibição no painel direito, bem como a sua inserção na base de dados _SQLite3_, por meio da aplicação de **Back End** escrita em _Python_.

Note que, após a entrada dos dados, sua exibição no painel direito e sua gravação nabase de dados, o cursor se posiciona no campo Titulo do filme para nova entrada de dados.

Caso deseje encerrar a aplicação, basta clicar no botão **Sair**.

Boa sorte!
