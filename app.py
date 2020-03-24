from flask import Flask
from flask import render_template

from scraper import scraper
from map_utils import Guanajuato


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
	gto = Guanajuato()
	totals = gto.totals
	gto_map = gto.generate_map()

	return render_template('index.html', totals=totals, svg_fig=gto_map)

@app.route('/about')
def about():
	return render_template('about.html')


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
