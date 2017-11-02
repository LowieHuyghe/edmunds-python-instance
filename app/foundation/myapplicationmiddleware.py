
from edmunds.foundation.applicationmiddleware import ApplicationMiddleware


class MyApplicationMiddleware(ApplicationMiddleware):
    """
    My Application Middleware
    """

    def handle(self, environment, start_response):
        """
        Handle the middleware
        :param environment:     The environment
        :type  environment:     Environment
        :param start_response:  The application
        :type  start_response:  flask.Response
        """

        return super(MyApplicationMiddleware, self).handle(environment, start_response)
