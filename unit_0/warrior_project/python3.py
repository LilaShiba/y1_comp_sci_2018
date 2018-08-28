class Player(object):
    def play_turn(self, warrior):
    	if warrior.health() < 15 and warrior.feel().is_empty():
    		warrior.rest_()
    	elif warrior.feel().is_enemy():
      		warrior.attack_()
    	else:
      		warrior.walk_()