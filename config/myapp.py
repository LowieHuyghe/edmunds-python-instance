
from app.exceptions.handler import Handler as ExceptionHandler
from edmunds.gae.runtimeenvironment import RuntimeEnvironment as GaeRuntimeEnvironment
if GaeRuntimeEnvironment().is_gae():
    from edmunds.log.drivers.googleappengine import GoogleAppEngine as LogDriver
    from edmunds.storage.drivers.googlecloudstorage import GoogleCloudStorage as StorageDriver
else:
    from edmunds.log.drivers.file import File as LogDriver
    from edmunds.storage.drivers.file import File as StorageDriver


APP = {

    # ------------------------------------------------------------
    # General
    # ------------------------------------------------------------
    #
    # General application configuration is defined here.
    #

    'name': 'My App',



    # ------------------------------------------------------------
    # Exceptions
    # ------------------------------------------------------------
    #
    # Exception-handling is configured here. They can be handled
    # with custom handlers when provided.
    #

    'exceptions':
    {
        'handler': ExceptionHandler,
    },



    # ------------------------------------------------------------
    # Storage
    # ------------------------------------------------------------
    #
    # Storage is configured here.
    #

    'storage':
    {
        'instances':
        [
            {
                'name': 'file',
                'driver': StorageDriver,
            },
        ],
    },



    # ------------------------------------------------------------
    # Localization
    # ------------------------------------------------------------
    #
    # Localization is configured here.
    #
    # Location Drivers:
    # from edmunds.localization.location.drivers.googleappengine import GoogleAppEngine
    # from edmunds.localization.location.drivers.maxmindcitydatabase import MaxMindCityDatabase
    # from edmunds.localization.location.drivers.maxmindenterprisedatabase import MaxMindEnterpriseDatabase
    # from edmunds.localization.location.drivers.maxmindwebservice import MaxMindWebService
    #
    # Translations Drivers:
    # from edmunds.localization.translations.drivers.configtranslator import ConfigTranslator
    #

    'localization': {
        'enabled': False,

        'locale': {
            'fallback': 'en_US',
            'supported': ['en_US', 'en', 'nl_BE', 'nl'],
        },

        'location': {
            'enabled': False,
            'instances': [
                #
            ],
        },

        'translations': {
            'enabled': False,
            'instances': [
                #
            ],
        },
    },



    # ------------------------------------------------------------
    # Logging
    # ------------------------------------------------------------
    #
    # Logging is configured here.
    # Drivers:
    # from edmunds.log.drivers.file import File
    # from edmunds.log.drivers.stream import Stream
    # from edmunds.log.drivers.syslog import SysLog
    # from edmunds.log.drivers.timedfile import TimedFile
    #

    'log':
    {
        'enabled': True,
        'instances':
        [
            {
                'name': 'file',
                'driver': LogDriver,
            },
        ],
    },



    # ------------------------------------------------------------
    # Profiling
    # ------------------------------------------------------------
    #
    # Profiling is configured here. This can be moved to
    # .env.local for example if that is more convenient.
    # Drivers:
    # from edmunds.profiler.drivers.callgraph import CallGraph
    # from edmunds.profiler.drivers.stream import Stream
    # from edmunds.profiler.drivers.blackfireio import BlackfireIo
    #

    'profiler':
    {
        'enabled': False,
        'instances':
        [
            #
        ],
    },

}
