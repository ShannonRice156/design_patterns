'''A Module which holds all code associated with logging'''
import time


class logging():
    '''A class that provides logging functionality for functions.'''
    _instance = None
    _enabled = False

    def __new__(cls):
        '''Returns an instance of this class or creates one if there isnt an instance. There will only ever be one instance of this class'''
        if cls._instance is None:
            cls._instance = super(logging, cls).__new__(cls)
        return cls._instance

    def toggle_logging(self, enabled: bool) -> None:
        '''Set the enabled property to the enabled param passed in'''
        self._enabled = enabled

    def log(self, func: object) -> object:
        """Returns a new function that wraps the original function and logs its start and end times"""
        def wrapper(*args, **kwargs) -> None:
            def log_data(*args, **kwargs) -> object:
                print(f"{func} call started at {time.time()}")
                ret = func(*args, **kwargs)
                print(f"{func} call finished at {time.time()}")
                return ret

            if self._enabled:
                return log_data(*args, **kwargs)
            else:
                return func(*args, **kwargs)

        return wrapper
