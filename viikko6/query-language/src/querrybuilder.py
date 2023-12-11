from matchers import  PlaysIn, HasAtLeast, HasFewerThan, All, Not, And, Or



class QuerryBuilder():
    def __init__(self, stack = And() ):
        self._querry = stack

    def playsIn(self, team): 
        return QuerryBuilder(And(self._querry, PlaysIn(team)))
    
    def hasAtLeast(self, value, attr): 
        return QuerryBuilder(And(self._querry, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr): 
        return QuerryBuilder(And(self._querry, HasFewerThan(value, attr)))
        
    def all(self):
        return QuerryBuilder(And(self._querry, All()))
    
    def Not(self, matcher):
        return QuerryBuilder(And(self._querry, Not(matcher)))
    
    def oneOf(self, q1, q2):
        return QuerryBuilder(Or(q1, q2))
    
    def build(self):
        return self._querry 