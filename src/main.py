from flask import Flask, request, jsonify
from views import get_main_page, search_transactions, search_by_phone
from reports import category_expenses_report

app = Flask(__name__)

@app.route('/main', methods=['GET'])
def main_page():
    date_str = request.args.get('date')
    return get_main_page(date_str)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    return search_transactions(query)

@app.route('/search_phone', methods=['GET'])
def search_phone():
    return search_by_phone()

@app.route('/category_report', methods=['GET'])
def category_report():
    category = request.args.get('category')
    return category_expenses_report(category)

if __name__ == '__main__':
    app.run(debug=True)
