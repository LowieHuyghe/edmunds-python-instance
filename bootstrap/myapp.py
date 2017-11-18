
from edmunds.application import Application
from app.providers.myserviceprovider import MyServiceProvider
from app.foundation.myapplicationmiddleware import MyApplicationMiddleware
from edmunds.database.providers.migrateserviceprovider import MigrateServiceProvider
from app.http import routes


def bootstrap():
    """
    Bootstrap the Application
    :return:    The bootstrapped application
    :rtype:     Application
    """

    base_import_name = '.'.join(__name__.split('.')[:-2])

    # Make application
    app = Application(
        base_import_name,
        static_url_path='',
        static_folder='resources/static',
        template_folder='resources/templates'
    )

    # Service Providers
    app.register(MyServiceProvider)
    # app.register(MigrateServiceProvider)

    # Routes
    routes.route(app)

    # Middleware
    app.middleware(MyApplicationMiddleware)

    return app
