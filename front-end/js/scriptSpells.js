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
    $("#btn_add_spell").click(function () {
        //obter dados do formulário
        name = $("#name_spell").val();
        level = $("#level").val();
        school = $("#school").val();
        castTime = $("#castTime").val();
        range = $("#range").val();
        components = $("#components").val();
        duration = $("#duration").val();
        concentration = $("#concentration").val();
        classe = $("#class_spell").val();
        desc = $("#desc").val();
        //dados pra envio(json)
        dados = JSON.stringify({
            name: name,
            level: level,
            school: school,
            castTime: castTime,
            range: range,
            components: components,
            duration: duration,
            concentration: concentration,
            classe: classe,
            desc: desc
        });
        // enviar ao back-end
        $.ajax({
            url: 'http://localhost:5000/adicionar_spell',
            type: 'POST',
            contentType: 'application/json',
            dataType: 'json',
            data: dados,
            success: adicoinarSpell,
            erro: erroAdicionarSpell
        });
        function adicoinarSpell(resposta) {
            //msg de sucesso
            if (resposta.resultado == "ok") {
                alert("Spell Adicionado Com Sucesso")
                //limpar campos form
                $("#name_spell").val("");
                $("#level").val("");
                $("#school").val("");
                $("#castTime").val("");
                $("#range").val();
                $("#components").val("");
                $("#duration").val("");
                $("#concentration").val("");
                $("#class_spell").val("");
                $("#desc").val("");
            } else {
                alert("erro na comunicação")
            }

        }
        function erroAdicionarSpell(resposta) {
            alert("Houve um erro na chamada ao back-end")
        }
    });
});