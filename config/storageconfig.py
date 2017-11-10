
from edmunds.gae.runtimeenvironment import RuntimeEnvironment as GaeRuntimeEnvironment
from edmunds.storage.drivers.googlecloudstorage import GoogleCloudStorage
from edmunds.storage.drivers.file import File


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
                'driver': File if not GaeRuntimeEnvironment.is_gae() else GoogleCloudStorage,
            },
            {
                'name': 'local',
                'driver': File,
            },
        ],
    },

}
