class CedictRouter:
    """
    A router to control all database operations on models in the
    cedict application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read dictionary models go to cedictpostgres.
        """
        if model._meta.app_label == 'cedictionary':
            return 'cedictpostgres'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write dictionaries models go to cedictpostgres.
        """
        if model._meta.app_label == 'cedictionary':
            return 'cedictpostgres'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the dictionaries app is involved.
        """
        if obj1._meta.app_label == 'cedictionary' or \
           obj2._meta.app_label == 'cedictionary':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the dictionaries app only appears in the 'cedictpostgres'
        database.
        """
        if app_label == 'cedictionary':
            return db == 'cedictpostgres'
        return None
