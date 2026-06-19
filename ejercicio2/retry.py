def retry(times: int = 3, exceptions: tuple = (Exception,)):
    """
    Decorator factory that retries the decorated function on failure.

    Args:
        times:      maximum number of attempts (including the first one).
                    With times=1 there are no retries: raises on the first error.
        exceptions: tuple of exception types that trigger a retry.
                    If the function raises a type NOT listed here, the exception
                    propagates immediately without retrying.

    Usage:
        @retry(times=3, exceptions=(ValueError, ConnectionError))
        def unstable():
            ...

    Requirements:
    - Use functools.wraps to preserve __name__ and __doc__ of the original function.
    - If all attempts are exhausted, re-raise the last exception received.
    - The decorator must forward *args and **kwargs to the wrapped function.
    """

    for i,j in exceptions:
            

        


        
            
