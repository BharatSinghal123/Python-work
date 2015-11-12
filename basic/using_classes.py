class greater:

    def __init__(self, name):
        self.name = name

    def greet(self, loud=False):
        if loud:
            print 'Bharat, %s!' % self.name.upper()
        else:
            print 'Singhal, %s' % self.name

g = greater('Fred')  
g.greet()            
g.greet(loud=True) 
