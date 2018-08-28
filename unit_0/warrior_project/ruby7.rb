# Beating level 5 was simple by using a var for the space we inspect
class Player
  MIN_HEALTH = 15
  
  def play_turn(warrior)
    @last_known_health ||= warrior.health
    @direction ||= :forward
    feel_space = warrior.feel @direction

    if feel_space.empty?      
      if should_flee? warrior 
        @direction = :backward
        warrior.walk! @direction
      elsif should_rest? warrior
        warrior.rest!
      else
        warrior.walk! @direction
      end
    elsif feel_space.captive?
      warrior.rescue! @direction
    elsif feel_space.wall?
      @direction = :forward
      warrior.pivot!
    else
      warrior.attack!
    end
    @last_known_health = warrior.health
  end
 
  private

  def should_flee? warrior
    !safe?(warrior) && (warrior.health < 7)
  end

  def should_rest? warrior
    bad_health = warrior.health < MIN_HEALTH
    safe?(warrior) && bad_health
  end
  
  def safe? warrior
    warrior.health >= @last_known_health
  end
end