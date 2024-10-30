from flask import Blueprint, render_template, request, redirect, url_for
from models.base import Session
from models.tuor import Tuor

tuor_route = Blueprint("tuors", __name__)

@tuor_route.get("/")
def index():
    return redirect(url_for("tuors.menu"))

@tuor_route.get("/menu/")
def menu():
    with Session() as session:
        tuors = session.query(Tuor).all()
        context = {
            "tuors": tuors,
            "title": "Меню турів",
        }
        return render_template("menu.html", **context)

@tuor_route.post("/add_tuor/")
def add_tuor():
    with Session() as session:
        name = request.form.get("name")
        price = request.form.get("price")

        tuor = Tuor(name=name, price=price)
        session.add(tuor)
        session.commit()
        return redirect(url_for("tuors.menu"))

@tuor_route.get("/tuor/del/<int:id>/")
def del_tuor(id):
    with Session() as session:
        tuor = session.query(Tuor).where(Tuor.id == id).first()
        if tuor:
            session.delete(tuor)
            session.commit()
            return redirect(url_for("tuors.menu"))
