import responder

api = responder.API()


@api.route('/')
def index(req, resp):
    resp.content = api.template('home/index.html')


api.run()
