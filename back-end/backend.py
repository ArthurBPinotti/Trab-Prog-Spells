from config import *
from modelo import Spell
from modelo import School
from modelo import Source


@app.route("/")
def padrao():
    return "Teste"


@app.route("/listar_spells")
def listar_spells():
    spells = db.session.query(Spell).all()
    retorno = []
    for s in spells:
        retorno.append(s.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


@app.route("/listar_schools")
def listar_schools():
    schools = db.session.query(School).all()
    retorno = []
    for s in schools:
        retorno.append(s.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


@app.route("/listar_sources")
def listar_sources():
    sources = db.session.query(Source).all()
    retorno = []
    for s in sources:
        retorno.append(s.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


@app.route("/adicionar_spell", methods=["POST"])
def adicionar_spell():
    dados = request.get_json()
    if dados["concentration"] == "1":
        dados["concentration"] = True
    else:
        dados["concentration"] = False
    novo_spell = Spell(**dados)
    db.session.add(novo_spell)
    db.session.commit()
    return{"resultado": "ok"}


@app.route("/excluir_spell/<int:spell_id>", methods=['DELETE'])
def excluir_spell(spell_id):

    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Spell.query.filter(Spell.id == spell_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


@app.route("/excluir_school/<int:school_id>", methods=['DELETE'])
def excluir_school(school_id):

    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Spell.query.filter(School.id == school_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


@app.route("/excluir_source/<int:source_id>", methods=['DELETE'])
def excluir_source(source_id):

    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Spell.query.filter(Source.id == source_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


app.run(debug=True)
