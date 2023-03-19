from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # TODO: Get the list of to-do items from a database or file
    # For now, just return a list of dummy items
    items = ['Item 1', 'Item 2', 'Item 3']
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    # Get the item from the form data
    item = request.form['item']

    # TODO: Add the new to-do item to a database or file

    # For now, just add the item to the items list
    items = ['Item 1', 'Item 2', 'Item 3', item]

    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
