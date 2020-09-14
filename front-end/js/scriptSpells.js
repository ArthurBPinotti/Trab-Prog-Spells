$(document).ready(function () {
    $("#conteudoInicial").removeClass("invisible");
    $("#link_listar_spells").click(function () {
        $.ajax({
            url: 'http://localhost:5000/listar_spells',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar_spells, // chama a função listar_spells para processar o resultado
            error: function () {
                alert("erro ao ler dados, verifique o backend");
            }
        });
        function listar_spells(resultado) {
            alert(resultado);

        }
    })
});