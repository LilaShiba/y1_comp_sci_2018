class Player(object):
    def play_turn(self, warrior):
    	if warrior.feel().is_enemy():
      		warrior.attack_()
    	else:
      		warrior.walk_()