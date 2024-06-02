import logging

import asgi_correlation_id

logger = logging.getLogger(__name__)


def configure_logging():
    console_handler = logging.StreamHandler()
    # Added correlation id in the filter
    console_handler.addFilter(asgi_correlation_id.CorrelationIdFilter())
    logging.basicConfig(
        handlers=[console_handler],
        level="INFO",
        format="%(asctime)s [%(levelname)s] [%(correlation_id)s] %(name)s: %(message)s | %(data)s"
    )


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'correlation_id': {
            '()': 'asgi_correlation_id.CorrelationIdFilter',
            'uuid_length': 32,
            'default_value': '-',
        },
    },
    'formatters': {
        'web': {
            'class': 'logging.Formatter',
            'datefmt': '%H:%M:%S',
            'format': '%(levelname)s ... [%(correlation_id)s] %(name)s %(message)s',
        },
    },
    'handlers': {
        'web': {
            'class': 'logging.StreamHandler',
            'filters': ['correlation_id'],
            'formatter': 'web',
        },
    },
    'loggers': {
        'my_project': {
            'handlers': ['web'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
