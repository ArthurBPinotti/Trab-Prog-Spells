from config import *


class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(254))

    def json(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Classe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(254))

    def json(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Spell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(254))
    level = db.Column(db.Integer)
    school = db.Column(db.String(254))
    castTime = db.Column(db.String(254))
    range = db.Column(db.Integer)
    components = db.Column(db.String(254))
    duration = db.Column(db.String(254))
    concentration = db.Column(db.Boolean)
    classe = db.Column(db.String(254))
    desc = db.Column(db.String(254))
    school_id = db.Column(db.Integer, db.ForeignKey(School.id), nullable=False)
    school_info = db.relationship("School")
    classe_id = db.Column(db.Integer, db.ForeignKey(Classe.id), nullable=False)
    classe_info = db.relationship("Classe")

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level,
            "school": self.school,
            "castTime": self.castTime,
            "range": self.range,
            "components": self.components,
            "duration": self.duration,
            "concentration": self.concentration,
            "classe": self.classe,
            "desc": self.desc,
            "school_id": self.school_id,
            "school_info": self.school.json(),
            "classe_id": self.classe_id,
            "classe_info": self.classe_info.json()
        }


if __name__ == "__main__":
    db.create_all()

    novaEscola = School(name="Abjuration")
    novaClasse = Classe(name="Warlock")
    novo = Spell(name="CounterSpell", level=3, school="abjuração", castTime="1 reação",
                 range=18, components="S", duration="Instantâneo", concentration=False,
                 classe="Sorcerer, Warlock, Wizard", desc="Você tenta interromper uma criatura no processo de lançar um feitiço. Se a criatura está lançando um feitiço de 3º nível ou inferior, o feitiço falha e não tem efeito. Se ele está lançando um feitiço de 4 º nível ou superior, faça um teste de habilidade usando sua habilidade de lançar feitiços. A CD é igual a 10 + o nível do feitiço. Com um sucesso, o feitiço da criatura falha e não tem efeito. Em níveis mais altos: Quando você conjura esta magia usando um slot de magia de 4º nível ou superior, a magia interrompida não tem efeito se seu nível for menor ou igual ao nível do slot de magia que você usou.",
                 school_info=novaEscola, classe_info=novaClasse)

    db.session.add(novo)
    db.session.add(novaEscola)
    db.session.add(novaClasse)
    db.session.commit()
    Spells = db.session.query(Spell).all()
    Schools = db.session.query(School).all()
    Classes = db.session.query(Classe).all()

    print(Spells)
    print(Schools)
    print(Classes)
