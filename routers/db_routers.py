class Authdb():

    route_app_labels = ['auth', 'contenttypes', 'sessions', 'admin']

    def db_for_read(self, model, **hints):

        if model._meta.app_label in self.route_app_labels:
            return 'users'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label in self.route_app_labels:
            return 'users'
        return None

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label in self.route_app_labels:
            return db == 'users'
        return None

class Blue:
    route_app_labels = ['blue']

    def db_for_read(self, model, **hints):

        if model._meta.app_label in self.route_app_labels:
            return 'blue'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label in self.route_app_labels:
            return 'blue'
        return None

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label in self.route_app_labels:
            return db == 'blue'
        return None

class Grey():
    route_app_labels = ['grey']

    def db_for_read(self, model, **hints):

        if model._meta.app_label in self.route_app_labels:
            return 'grey'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label in self.route_app_labels:
            return 'grey'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label in self.route_app_labels:
            return db == 'grey'
        return None