
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
    # Logging
    # ------------------------------------------------------------
    #
    # Logging is configured here.
    # Drivers:
    # from Edmunds.Log.Drivers.File import File
    # from Edmunds.Log.Drivers.Stream import Stream
    # from Edmunds.Log.Drivers.SysLog import SysLog
    # from Edmunds.Log.Drivers.TimedFile import TimedFile
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
    # from Edmunds.Profiler.Drivers.CallGraph import CallGraph
    # from Edmunds.Profiler.Drivers.Stream import Stream
    # from Edmunds.Profiler.Drivers.BlackfireIo import BlackfireIo
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
