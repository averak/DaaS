from flask import Flask
from controller import judge_api
from controller import eval_api
from controller import katakanize_api

app = Flask(__name__)
app.register_blueprint(judge_api.app, url_prefix='/')
app.register_blueprint(eval_api.app, url_prefix='/')
app.register_blueprint(katakanize_api.app, url_prefix='/')

if __name__ == "__main__":
    app.run()
