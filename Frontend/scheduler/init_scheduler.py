import schedule
from Frontend.parse.install_parse import init as Parse_start



def install():
    schedule.every().day.at("00:00").do(Parse_start)
    while True:
        schedule.run_pending()