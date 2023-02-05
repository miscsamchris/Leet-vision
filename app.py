from TransGraphtion import app,db,redirect,url_for
import requests
from flask import render_template
@app.route("/")
def home():
    return """
<html>
<head>

</head>

<body>
<frame src="https://2fe2-103-156-19-229.in.ngrok.io/d-solo/3Ez7RxA4k/new-dashboard?orgId=1&from=1675535529047&to=1675557129047&panelId=2" width="450" height="200" frameborder="0"></frame>
</body>
</html>

"""

@app.route("/train")
def trainmodel():
    pass
if __name__=="__main__":
    db.create_all()
    app.run(threaded=True)  