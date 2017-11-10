
from edmunds.gae.gaetestcase import GaeTestCase as EdmundsGaeTestCase, gae_can_run
from bootstrap.myapp import bootstrap
import os


class GaeTestCase(EdmundsGaeTestCase):
    """
    A UnitTest Gae Test Case
    """

    def create_application(self, environment='testing'):
        """
        Create the application for testing
        :param environment: Environment
        :type environment:  str
        :return:            Application
        :rtype:             edmunds.application.Application
        """

        os.environ['APP_ENV'] = environment

        return bootstrap()
