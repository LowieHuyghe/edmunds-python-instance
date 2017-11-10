
from edmunds.gae.runtimeenvironment import RuntimeEnvironment as GaeRuntimeEnvironment
from edmunds.storage.drivers.file import File
if GaeRuntimeEnvironment.is_gae():
    from edmunds.storage.drivers.googlecloudstorage import GoogleCloudStorage as DynamicDriver
else:
    from edmunds.storage.drivers.file import File as DynamicDriver


APP = {

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
                'name': 'dynamic',
                'driver': DynamicDriver,
            },
            {
                'name': 'local',
                'driver': File,
            },
        ],
    },

}
