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
        function listar_spells(spells) {
            // inicializar um acumulador
            linhas = ""
            // percorrer as plantas retornadas em json
            for (var i in spells) {

                // montar uma linha da tabela de plantas
                lin = "<tr>" +
                    "<td>" + spells[i].name + "</td >" +
                    "<td>" + spells[i].level + "</td>" +
                    "<td>" + spells[i].school + "</td>" +
                    "<td>" + spells[i].castTime + "</td>" +
                    "<td>" + spells[i].range + "</td>" +
                    "<td>" + spells[i].components + "</td>" +
                    "<td>" + spells[i].duration + "</td>" +
                    "<td>" + spells[i].concentration + "</td>" +
                    "<td>" + spells[i].classe + "</td>" +
                    "</tr >"
                // adicionar a linha da tabela em um acumulador
                linhas = linhas + lin;

            }
            // colocar as linhas na tabela
            $("#corpoTabelaSpells").html(linhas);
            // esconder todos os elementos da tela
            $("#conteudoInicial").addClass("invisible");
            $("#tabelaSpells").addClass("invisible");
            //exibir tabela
            $("#tabelaSpells").removeClass("invisible");
        }
    });
    $("#link_inicio").click(function () {

        $("#tabelaSpells").addClass("invisible");
        $("#conteudoInicial").addClass("invisible");

        $("#conteudoInicial").removeClass("invisible");

    })
});