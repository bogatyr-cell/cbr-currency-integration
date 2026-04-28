from Backend.database.install_DB import init_db as DB_Start
from Backend.parse.install_parse import install as Parse_Start
from flask import Flask, render_template, jsonify
from Backend.scheduler.init_scheduler import install as Start_Scheduler
import threading
import os
from dotenv import load_dotenv

load_dotenv()


Flask_init = Flask(__name__)


@Flask_init.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    DB_Start(os.getenv("database_name"))
    Parse_Start(os.getenv("database_name"))
    threading.Thread(target=Start_Scheduler, daemon=True).start()
    print(f"Привет! Название проекта {os.getenv("project_name")}")
    from waitress import serve
    print("🚀 Сервер запущен на http://127.0.0.1:5000")
    serve(Flask_init, host='0.0.0.0', port=5000)