import bases

class MallardDuck(bases.Duck):
    def quack(self):
        print 'Quack'

    def fly(self):
        print "I'm flying"


class WildTurkey(bases.Turkey):
    def gobble(self):
        print 'Gobble gobble'

    def fly(self):
        print "I'm flying a short distance"


class TurkeyAdapter(bases.Duck):
    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        """Expose quack(), but make a call that Turkey understands."""
        self.turkey.gobble()

    def fly(self):
        """Support fly(), but Turkeys only fly 1/5 as far as Ducks."""
        for _ in range(5):
            self.turkey.fly()