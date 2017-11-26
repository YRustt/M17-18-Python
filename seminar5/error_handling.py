
import logging

logging.basicConfig(filename="handle_error.log", level=logging.ERROR)
log = logging.getLogger("ex")


class handle_error_context:
    def __init__(self, re_raise=True, log_traceback=True, exc_type=Exception):
        self._re_raise = re_raise
        self._log_traceback = log_traceback
        self._exc_type = exc_type if isinstance(exc_type, tuple) else (exc_type,)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._log_traceback and exc_tb:
            log.exception(exc_tb)

        return not self._re_raise if isinstance(exc_val, self._exc_type) else False


class handle_error:
    def __init__(self, re_raise=True, log_traceback=True, exc_type=Exception):
        self._re_raise = re_raise
        self._log_traceback = log_traceback
        self._exc_type = exc_type

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with handle_error_context(self._re_raise, self._log_traceback, self._exc_type):
                return func(*args, **kwargs)

        return wrapper
