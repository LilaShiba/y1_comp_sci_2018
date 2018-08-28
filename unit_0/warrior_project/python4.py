class Player(object): 
    def play_turn(self, warrior):
    
    	if  warrior.feel().is_empty():
    		if warrior.health() < 20 and warrior.health() >= self.health:
    			warrior.rest_()
    		else:
    			warrior.walk_()
    	else:
    		warrior.attack_()
    	self.health = warrior.health()
    	