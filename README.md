# Sintatica Verso Super Mario
Este é um projeto de treinamento simples que tem como objetivo armazenar alguns dados dos principais jogos do Universo Super Mario. 

## Apresentação
![tela inicial](https://user-images.githubusercontent.com/71519298/214593576-ab4167ee-6e68-4e33-bd1e-474ffec28fe1.png)

## Requisitos para rodar o projeto

### Tecnologias
Python<br>
Django<br>
BootsTrap<br>
HTML<br>
CSS<br>
JavaScript<br>
### Setup de ambiente
- Utilizamos a IDE `VScode` no desenvolvimento

### Como rodar na minha máquina?
- Clone o projeto `git clone git@github.com:alaimcosta/universo-supermario.git`
- Abri o projeto no VScode
- Pronto!!

## Site
### Estrutura do projeto
- O projeto utiliza a linguagem de programação `Python3`, o framework `Django`, alinguagem de marcação `HTML`, estilização com `CSS` e `JavaScript` para desenvolver a lógica. 
- A estrutura do projeto está baseado na imagem seguinte:


### Como me localizar no projeto?
* Todos os arquivos do projeto estão em
    * core
      * migrations
      * static
         * core
            * css
               * `style.css` 
            * js
               * `style.js`
      * templates
         * `ìndex.html`
         * `template.html`
    * `projetosuper`
    * `venv`
    * `db.sqlite3`
    * `manage.py`

### Como funciona a estrutura do JavaScript?
```javascript
function validar(){
    var nomePlayer = document.getElementById("task_name");


    if(nomePlayer.value == ""){
        alert("Informe o nome do Jogo")
        nomePlayer.focus();
    }
}

function validar(){
    var person = document.getElementById("task_personagem");

    if(person.value == ""){
        alert("Insira o nome do personagem do jogo")
        person.focus();
    }
}
```

## Autor
| [<img src="https://user-images.githubusercontent.com/71519298/188052888-7d822b41-2950-4e4b-b6e7-0863dc9ef67d.jpg" width=115><br><sub>Alaim Costa</sub>](https://github.com/alaimcosta) |
| :---: |
