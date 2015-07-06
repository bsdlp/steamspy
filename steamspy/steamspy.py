from classdirectory import ClassDirectory
import .methods


class SteamSpy(object):
    def __init__(self):
        cd = ClassDirectory(methods)
        for method in cd.find(parent=methods.APIHelper):
            _method_name = method.__class__.__name__.lower()
            setattr(self, _method_name, method)
