import schedule
from Backend.parse.install_parse import install as Parse_start



def install():
    schedule.every().day.at("00:00").do(Parse_start)
    while True:
        schedule.run_pending()