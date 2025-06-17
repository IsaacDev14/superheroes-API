# app.py

from app import create_app, db
from app.models import Hero, Power, HeroPower

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Hero": Hero,
        "Power": Power,
        "HeroPower": HeroPower
    }
