
from edmunds.gae.runtimeenvironment import RuntimeEnvironment as GaeRuntimeEnvironment
from app.providers.myserviceprovider import MyServiceProvider
from app.foundation.myapplicationmiddleware import MyApplicationMiddleware
from app.http import routes


def bootstrap():
    """
    Bootstrap the Application
    :return:    The bootstrapped application
    :rtype:     Application
    """

    base_import_name = '.'.join(__name__.split('.')[:-2])

    # Runtime Environment
    is_gae = GaeRuntimeEnvironment().is_gae()

    # Make application
    static_url_path = ''
    static_folder = 'resources/static'
    template_folder = 'resources/templates'

    if is_gae:
        from edmunds.gae.application import Application as GaeApplication
        app = GaeApplication(base_import_name, static_url_path=static_url_path, static_folder=static_folder,
                             template_folder=template_folder)
    else:
        from edmunds.application import Application
        app = Application(base_import_name, static_url_path=static_url_path, static_folder=static_folder,
                          template_folder=template_folder)

    # Service Providers
    app.register(MyServiceProvider)

    # Routes
    routes.route(app)

    # Middleware
    app.middleware(MyApplicationMiddleware)

    return app
