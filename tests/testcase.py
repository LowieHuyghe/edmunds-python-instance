
from edmunds.foundation.testing.testcase import TestCase as EdmundsTestCase
from bootstrap.myapp import bootstrap


class TestCase(EdmundsTestCase):
    """
    A UnitTest Test Case
    """

    def create_application(self):
        """
        Create the application for testing
        """

        return bootstrap()
