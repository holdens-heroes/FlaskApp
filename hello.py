from tests import TestClass
from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True

# print __name__

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
	test_class = TestClass("good luvin'")
	test_class.run_test()
	return render_template('hello.html', name=name)

@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return "Posted"
	else:
		return "Getted"

if __name__ == "__main__":
	app.run()