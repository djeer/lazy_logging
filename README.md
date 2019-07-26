Logging for lazyass

Use cases:

#### I want pretty human-readable logs in stdout:
`
logger = logger_factory()
`

#### I want json-formatted logs in stdout to use with glef docker driver:
`
logger = logger_factory(json_stdout=True)
`

#### I want to save json-formatted logs to file and collect them with filebeat:
`
logger = logger_factory(log_dir='/var/logs', log_file='myapp')
`

#### I want to do the same in django settings.py:

```
LOGGING_CONFIG = None  # <- default django config
LOG_DIR = '/var/logs'
LOG_FILE = 'myapp'
configure_django_logging()
```
