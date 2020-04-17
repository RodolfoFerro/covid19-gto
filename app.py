from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template
from datetime import datetime

from map_utils import Guanajuato
from scraper import run_and_save


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


sched = BackgroundScheduler(daemon=False)
sched.add_job(run_and_save, 'interval',
              minutes=20, next_run_time=datetime.now())
sched.start()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
