class Player
  def play_turn(warrior)
    @health = warrior.health unless @health

    #2 options when the space is empty
    if warrior.feel.empty? 
      #option 1 rest if health < 20 and we are not under attack
      if warrior.health < 20 && warrior.health >= @health
        warrior.rest!
     #otherwise walk
      else warrior.walk! 
      end
    #if the space is not empty we attack  
    else warrior.attack! 
    end

    @health = warrior.health
  end #play_turn
end #class