    # src/main/routes.py
    from flask import Blueprint

    # 1. Creamos un "Blueprint". Es como un mini-módulo de Flask.
    #    Le damos un nombre ('main') para identificarlo.
    main = Blueprint('main', __name__)

    # 2. Tu ruta original ahora se "adhiere" a este Blueprint.
    @main.route("/")
    def hello():
        return "DevOps test desde la nueva estructura!"