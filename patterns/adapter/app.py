#!/usr/bin/env python

from implementations import MallardDuck, WildTurkey, TurkeyAdapter

if __name__ == '__main__':
    d = MallardDuck()
    print '\nThe Duck says...'
    d.quack()
    d.fly()

    t = WildTurkey()
    print '\nThe Turkey says...'
    t.gobble()
    t.fly()

    # Now we use the adapter to show how a Turkey can be made to
    # behave like a Duck (expose the same methods, and fly the same
    # distance):
    td = TurkeyAdapter(t)
    print '\nThe TurkeyAdapter says...'
    td.quack()
    td.fly()