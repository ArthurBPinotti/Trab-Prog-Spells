from config import *
from modelo import Spell


@app.route("/")
def padrao():
    return "Teste"


@app.route("/listar_spells")
def listar_spells():
    spells = db.session.query(Spell).add()
    retorno = []
    for s in spells:
        retorno.append(s.json)
    return jsonify(retorno)


@app.route("/incluir_spell", methods=["post"])
def incluir_spell():
    dados = resquest.get_json()
    novo_spell = Spell(**dados)
    db.session.add(novo_spell)
    db.session.commint()
    return{"resultado": "ok"}


app.run(debug=True)