"""
    Show list of Food carts
"""
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class View(MethodView):
    def get(self):
        model = gbmodel.get_model()
        foodcart = [dict(name=row[0], address=row[1], city=row[2], state=row[3], zip=row[4], hour=row[5], phone=row[6], rating=row[7]) for row in model.select()]
        return render_template('view.html',foodcart=foodcart)