from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')
@app.route('/clothing/')
def clothing():
    products = [
        {"name": "Футболка", "price": 20},
        {"name": "Джинсы", "price": 50},
        {"name": "Платье", "price": 80}
    ]
    return render_template('category.html', category_title='Одежда', products=products)

@app.route('/jacket/')
def jacket():
    product = {"name": "Куртка", "price": 100, "description": "Теплая зимняя куртка"}
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)