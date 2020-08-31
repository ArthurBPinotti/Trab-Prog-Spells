from config import *


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
            "desc": self.desc
        }


if __name__ == "__main__":
    db.create_all()
    novo = Spell(name="CounterSpell", level=3, school="abjuração", castTime="1 reação",
                 range=18, components="S", duration="Instantâneo", concentration=False, classe="Sorcerer, Warlock, Wizard", desc="Você tenta interromper uma criatura no processo de lançar um feitiço. Se a criatura está lançando um feitiço de 3º nível ou inferior, o feitiço falha e não tem efeito. Se ele está lançando um feitiço de 4 º nível ou superior, faça um teste de habilidade usando sua habilidade de lançar feitiços. A CD é igual a 10 + o nível do feitiço. Com um sucesso, o feitiço da criatura falha e não tem efeito. Em níveis mais altos: Quando você conjura esta magia usando um slot de magia de 4º nível ou superior, a magia interrompida não tem efeito se seu nível for menor ou igual ao nível do slot de magia que você usou.")
    db.session.add(novo)
    db.session.commit()
    todos = db.session.query(Spell).all()
