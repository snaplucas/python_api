from flask import Flask

app = Flask("wtf")
app.config.from_object('settings')

import views
