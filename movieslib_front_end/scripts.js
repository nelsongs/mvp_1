/*
  --------------------------------------------------------------------------------------
  Obter a lista de filmes existentes no banco de dados via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/filmes';
  fetch(url, {
    method: 'get'
  })
    .then((response) => response.json())
    .then((data) => {
      data.filmes.forEach(item => insertList(item.titulo, item.tipo, item.media, item.info))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()

/*
  --------------------------------------------------------------------------------------
  Colocar um filme na lista via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (titulo, tipo, media, info) => {
  const formData = new FormData();
  formData.append('titulo', titulo);
  formData.append('tipo', tipo);
  formData.append('media', media);
  formData.append('info', info);

  let url = 'http://127.0.0.1:5000/filme';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
  
  document.getElementById("input-titulo").focus();  
}


/*
  --------------------------------------------------------------------------------------
  Cria um botão "close" para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertButton = (parent) => {
  let span = document.createElement("span");
//  let txt = document.createTextNode("\u00D7");
//  let txt = document.createTextNode("\u2327");
  let txt = document.createTextNode("\u24CD");
//  let txt = document.createTextNode("\u2573");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}


/*
  --------------------------------------------------------------------------------------
  Remover um item da lista ao clicar no botão "close"
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const titulo = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Tem certeza?")) {
        div.remove()
        deleteItem(titulo)
        alert("Removido!")
      }
    }
  }
}


/*
  --------------------------------------------------------------------------------------
  Deletar um filme da lista via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (titulo) => {
  console.log(titulo)
  let url = 'http://127.0.0.1:5000/filme?titulo=' + titulo;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    })
}


/*
  ---------------------------------------------------------------------------------------
  Adicionar um novo filme com titulo, tipo, media e informações sobre o filme 
  ---------------------------------------------------------------------------------------
*/
const newMovie = () => {
  let titulo = document.getElementById("input-titulo").value;
  let tipo = document.getElementById("input-tipo").value;
  let media = document.getElementById("input-media").value;
  let info = document.getElementById("input-info").value;

  if (!titulo) {
    alert("Informe o título do filme!");
  } else if (!tipo) {
    alert("Selecione o tipo do filme ou insira outro tipo!");
  } else if (!media) {
    alert("Selecione a mídia do filme ou insira outro tipo de mídia!");
  } else {
    insertList(titulo, tipo, media, info);
    postItem(titulo, tipo, media, info);
//    alert("Filme adicionado!");
  }
  
}

/*
  --------------------------------------------------------------------------------------
  Insere items na lista e a apresenta
  --------------------------------------------------------------------------------------
*/

const insertList = (titulo, tipo, media, info) => {
  var filme = [titulo, tipo, media, info];

  var table = document.getElementById('filmes-table');
  var row = table.insertRow();

  for (var i = 0; i < filme.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = filme[i];
  }
  insertButton(row.insertCell(-1))
  document.getElementById("input-titulo").value = "";
  document.getElementById("input-tipo").value = "";
  document.getElementById("input-media").value = "";
  document.getElementById("input-info"). value = "";

  removeElement()

}


/*
  ---------------------------------------------------------------------------------------
  Fechar a aplicação 
  ---------------------------------------------------------------------------------------
*/
function closeApp () {
  if (confirm("Deseja encerrar a aplicação?")) {
    window.close();
  }
  
}
