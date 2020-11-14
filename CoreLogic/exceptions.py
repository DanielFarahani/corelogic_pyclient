from requests.exceptions import HTTPError
import logging

def http_exception_handler(f):
    def log_error(error):
    """
        Logs error.
        :param error: error being logged
    """
        if hasattr(error, 'message'):
            logging.error(error.message)
        else:
            logging.error(error)
            
    def wrapper(*args, **kwargs):
    """
        Decorator to keep try catch block dry for all API calls.
        :param f: function being wrapped
        :return:
    """
        try:
            response = f(*args, **kwargs)
            response.raise_for_status()
            return response.json()
        except HTTPError as error:
            log_error(error)
        except Exception as error:
            log_error(error)
            
    return wrapper