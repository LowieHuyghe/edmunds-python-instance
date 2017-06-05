
from edmunds.profiler.drivers.callgraph import CallGraph
from edmunds.profiler.drivers.stream import Stream
from edmunds.profiler.drivers.blackfireio import BlackfireIo


APP = {

    'debug': True,

    'profiler':
    {
        'enabled': False,
        'instances':
        [
            {
                'name': 'stream',
                'driver': Stream,
            },
            {
                'name': 'callgraph',
                'driver': CallGraph,
            },
            {
                'name': 'blackfireio',
                'driver': BlackfireIo,
            },
        ],
    },

}
