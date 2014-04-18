import abc


class Duck():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def quack():
        return

    @abc.abstractmethod
    def fly():
        return


class Turkey():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def gobble():
        return

    @abc.abstractmethod
    def fly():
        return
