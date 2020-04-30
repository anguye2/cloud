from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Add(MethodView):
    def get(self):
        return render_template('add.html')

    def post(self):
        """
        Accepts POST requests and gets the data from the form
        Redirect to index when completed.
        """
        model = gbmodel.get_model()

        model.insert(request.form.get('name', type=str), request.form.get('address', type=str), request.form.get('city', type=str), 
        request.form.get('state', type=str), request.form.get('zipcode', type=str), request.form.get('hour', type=str), 
        request.form.get('phone', type=str), request.form.get('rating', type=str))
        return redirect(url_for('index'))
