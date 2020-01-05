# https://lassala.net/2010/11/04/a-good-example-of-liskov-substitution-principle/

class IPersistedResource:

    def load(self):
        pass

    def persist(self):
        pass


class ApplicationSettings(IPersistedResource):

    def load(self):
        print("This is for application load settings....")

    def persist(self):
        print("This is for application persist settings.....")


class UserSettings(IPersistedResource):

    def load(self):
        print("This is for user load settingss....")

    def persist(self):
        print("This is for user persist settings...")


class NewSettings(IPersistedResource):

    def load(self):
        print("This is for new load settings...")

    def persist(self):
        raise NotImplementedError



# newsettings  = NewSettings()
# newsettings.load()
# newsettings.persist()

# it is clear that "NewSettings" is NOT substitutable by its
# "IPersistedResource" interface; if we call Persist on it, the app blows up, so we need change the method
# to take that one problem into consideration. One could say “well, let’s change the Persist method on that
# class so it won’t throw an exception anymore”. Hmm, having a method on a class that when called won’t do
# what its name implies is just bad… really, really bad.

# Write this down: anytime you see code that takes in some sort of baseclass or interface and then
# performs a check such as “if (someObject is SomeType)”, there’s a very good chance that that’s an
# LSP violation. I’ve done that, and I know so have you, let’s be honest.

"""To fix this we will create separate class for each method"""


class ILoadResource:

    def load(self):
        pass


class IPersistedResource:

    def persist(self):
        pass

# when you implement this NewSettings only inherite required class


class NewSettings(ILoadResource):

    def load(self):
        print("This is for new load settings...")


class UserSettings(ILoadResource, IPersistedResource):

    def load(self):
        print("This is for user load settingss....")

    def persist(self):
        print("This is for user persist settings...")


newsettings  = NewSettings()
newsettings.load()


usersettings = UserSettings()
usersettings.persist()
usersettings.load()