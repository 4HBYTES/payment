class Health(object):
    """
    Represents a Health object used by the HealthDetails resource.
    """

    def __init__(self, status, environment, application, timestamp):
        self.status = status
        self.environment = environment
        self.application = application
        self.timestamp = timestamp
