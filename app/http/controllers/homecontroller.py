
from edmunds.http.controller import Controller


class HomeController(Controller):
    """
    My Home Controller
    """

    def get_index(self):
        """
        Index page
        """

        app_name = self.app.config('app.name')
        self.response.assign('app_name', app_name)

        return self.response.render_template('home.index.html')
