
from bootstrap.myapp import bootstrap
from app.console.manager import Manager

app = bootstrap()
manager = Manager(app)
manager.init(__file__)
