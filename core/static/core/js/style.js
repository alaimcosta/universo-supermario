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

