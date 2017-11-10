
from edmunds.gae.runtimeenvironment import RuntimeEnvironment as GaeRuntimeEnvironment
from edmunds.log.drivers.googleappengine import GoogleAppEngine
from edmunds.log.drivers.file import File


APP = {

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
                'name': 'dynamic',
                'driver': File if not GaeRuntimeEnvironment.is_gae() else GoogleAppEngine,
            },
        ],
    },

}
