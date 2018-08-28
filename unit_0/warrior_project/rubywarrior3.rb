class Player
  def play_turn(warrior)
  	if warrior.feel.empty? == true && warrior.health < 16
    		warrior.rest!
    elsif warrior.feel.empty? == false
    		warrior.attack!
    else
    	warrior.walk!
    end

  end
end