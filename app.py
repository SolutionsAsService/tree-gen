from flask import Flask, render_template, send_file
from io import BytesIO
import tree_generator as generator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/palm_tree/<int:variation>')
def palm_tree_image(variation):
    image = generator.generate_palm_tree(variation)
    img_io = BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/shrubbery/<int:variation>')
def shrubbery_image(variation):
    image = generator.generate_shrubbery(variation)
    img_io = BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/green_tree/<int:variation>')
def green_tree_image(variation):
    image = generator.generate_green_tree(variation)
    img_io = BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)