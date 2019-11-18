class ConnectionsRouter(object):
    """
    A router to control all database operations on models in the
    connections application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read connections models go to connectionspostgres.
        """
        if model._meta.app_label == 'connections':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write connections models go to connectionspostgres.
        """
        if model._meta.app_label == 'connections':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the connections app is involved.
        """
        if obj1._meta.app_label == 'connections' or \
           obj2._meta.app_label == 'connections':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the connections app only appears in the 'connectionspostgres'
        database.
        """
        if app_label == 'connections':
            return db == 'connectionspostgres'
        return True