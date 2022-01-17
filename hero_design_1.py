
class Hero:
    """Features of all Heroes."""
    def __init__(self, name, health, damage, shields, speed):
        """Initialize attributes of all NPCs."""
        self.name = name
        self.health = health
        self.damage = damage
        self.shields = shields
        self.speed = speed        
    
    def modify_health(self, health):
        self.health = health
        print(f"Health is {self.health}.")
        return self.health
    
    def modify_damage(self, damage):
        self.damage = damage
        print(f"Damage is {self.damage}.")
        return self.damage
    
    def modify_shields(self, shield_points_lost):
        self.shields = self.shields + shield_points_lost
        #print(f"Shields are {self.shields}.")
        return self.shields
    
    def modify_speed(self, speed):
        self.speed = speed
        print(f"Speed is {self.speed}.")
        return self.speed
    

#Create inherited classes for roles Support, Tank, and Damage.

class Support(Hero):    
    """Specify heroes in the Support role."""
    def __init__(self, name, health, damage, speed, heals_per_second, *shields):
        """Initialize attributes from the parent class Hero."""
        super().__init__(name, health, damage, shields, speed)
        #Shields is *kwargs since it's set at 50 for all Support heroes.
        self.shields = 50        
        self.heals_per_second = heals_per_second        
    
    def shields_hit_support(self):
        """Decrease in shields for the Support class."""
        support_shields_lost = -10        
        self.shields = Hero.modify_shields(self, support_shields_lost)
        

def hero_stats(hero_name):
    """Print the stats of the hero."""
    for h, values in hero_name.__dict__.items():       
        print(f"{h.title()}: {values}")

print("Tank 1 Stats:")
hero_1 = Hero("Tank 1", 100, 80, 100, 35)
hero_stats(hero_1)
print("\n")
print("Supp1 Stats:")
support_hero = Support("Supp1", 60, 10, "Very Fast", 5)
support_hero.shields_hit_support()
hero_stats(support_hero)






