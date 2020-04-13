from flask import Flask
from flask import render_template

from map_utils import Guanajuato


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    gto = Guanajuato()
    resumen = gto.data['resumen']
    estados = gto.data['estados']
    gto_map = gto.generate_map_data()

    return render_template(
        'index.html',
        resumen=resumen,
        mapdata=gto_map,
        estados=estados,
        timestamp=gto.data['timestamp']
    )


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
