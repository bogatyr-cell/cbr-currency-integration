from Frontend.database.install_DB import install as DB_Start
from Frontend.parse.install_parse import install as Parse_Start
from flask import Flask, render_template, jsonify
from Frontend.scheduler.init_scheduler import install as Start_Scheduler
import threading

Flask_init = Flask(__name__)


@Flask_init.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    DB_Start()
    Parse_Start()
    threading.Thread(target=Start_Scheduler, daemon=True).start()

    from waitress import serve
    print("🚀 Сервер запущен на http://127.0.0.1:5000")
    serve(Flask_init, host='0.0.0.0', port=5000)