
from app.exceptions.handler import Handler as ExceptionHandler


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

}
