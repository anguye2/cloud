"""
    AN NGUYEN
    A simple Python Flask MVC webapp for Food Carts
    A user can be able to view, submit and delete a food cart location
"""
import flask
from flask.views import MethodView
from index import Index
from view import View
from add import Add


app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/view/',
                view_func=View.as_view('view'),
                methods=['GET'])

app.add_url_rule('/add/',
                view_func=Add.as_view('add'),
                methods=['GET', 'POST'])

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)