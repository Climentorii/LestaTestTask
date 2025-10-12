import random as r
from scripts.characters.Character import Character
from scripts.characters.EnemyTypes import Goblin, Skeleton, Golem, Ghost, Slime, Dragon
from scripts.perks.PerkTypes import Poison, Shield, StoneSkin, HiddenAttack, Rush, Rage
from scripts.characters.EnemyTypes import Enemy


enemy_chances_dict = {
    Goblin: 0.2, 
    Skeleton: 0.2, 
    Golem: 0.17, 
    Ghost: 0.17, 
    Slime: 0.17, 
    Dragon: 0.06
}

def count_chance_of_shot(attacker_agility: int, defender_agility: int):

    sum_agility = attacker_agility + defender_agility
    chance_agility = r.randint(1, sum_agility)

    return True if (chance_agility > defender_agility) else False

class GameEngine:

    def __init__(self):

        self.is_player_turn : bool
        self.player_turn_count : int
        self.main_player : Character
        self.current_enemy : Enemy
        self.level_dict = {'Rogue': 0, 'Warrior': 0, 'Barbarian': 0}
        self.defeated_enemies_count = 0
        self.enemy_chances_dict = enemy_chances_dict

    def add_main_player(self, main_player: Character):
        self.main_player = main_player
        self.level_dict[self.main_player.name] += 1
        
    def initialize_fight(self, current_enemy: Enemy):

        self.current_enemy = current_enemy
        self.is_player_turn =  True if (self.main_player.agility >= self.current_enemy.agility) else False
        self.player_turn_count = 1
        self.main_player

    def calculate_damage_with_perks(self, attacker: Character, defender: Character) -> int:
        result_damage = 0
        for perk in attacker.perks_list:
            if perk.is_attack:
                result_damage += perk.count_damage(attacker, defender)
        
        for perk in defender.perks_list:
            if not perk.is_attack:
                result_damage += perk.count_damage(attacker, defender)

        return result_damage

    def is_character_alive(self, character: Character):
        if character.health <= 0:
            return False
        return True

    def compile_character_turn(self, current_player: Character, enemy: Character, text: str) -> str:

        if count_chance_of_shot(current_player.agility, enemy.agility):
            
            result_damage_from_perks = self.calculate_damage_with_perks(current_player, enemy)
            character_damage = current_player.deal_damage()
            enemy.get_damage(character_damage, result_damage_from_perks, current_player.weapon.attack_type)
            text = f"{current_player.name} ударил {enemy.name}, нанеся ему {result_damage_from_perks + character_damage} урона."
        else:
            text = f"{current_player.name} не попал по {enemy.name}."
        current_player.turnCount += 1

        return text


    def level_up_rogue_1(self):

        self.level_dict['Rogue'] += 1
        self.main_player.perks_list.append(HiddenAttack())

    def level_up_rogue_2(self):

        self.level_dict['Rogue'] += 1
        self.main_player.agility += 1

    def level_up_rogue_3(self):

        self.level_dict['Rogue'] += 1
        self.main_player.perks_list.append(Poison())

    def level_up_warrior_1(self):

        self.level_dict['Warrior'] += 1
        self.main_player.perks_list.append(Rush())

    def level_up_warrior_2(self):

        self.level_dict['Warrior'] += 1
        self.main_player.perks_list.append(Shield())

    def level_up_warrior_3(self):

        self.level_dict['Warrior'] += 1
        self.main_player.power += 1

    def level_up_barbarian_1(self):

        self.level_dict['Barbarian'] += 1
        self.main_player.perks_list.append(Rage())

    def level_up_barbarian_2(self):

        self.level_dict['Barbarian'] += 1
        self.main_player.perks_list.append(StoneSkin())

    def level_up_barbarian_3(self):

        self.level_dict['Barbarian'] += 1
        self.main_player.stamina += 1

    def level_up(self, className: str, level: int):
        
        className += "_" + str(level)
        print(className)
        methodName = f"level_up_{className}"
        if hasattr(self, methodName):
            method = getattr(self, methodName)
            method()

        self.main_player.max_health += self.main_player.stamina
        self.main_player.health = self.main_player.max_health

    def count_sum_level(self) -> int:
        return sum(self.level_dict.values())
    
    def recount_chances(self, numberOfDefeatedEnemies: int):
        for key in self.enemy_chances_dict:  
            if key != Dragon:
                self.enemy_chances_dict[key] -= 0.01 * numberOfDefeatedEnemies
            else:
                enemy_chances_dict[key] += 0.05 * numberOfDefeatedEnemies


    def spawn_enemy(self) -> Enemy:
        enemyClasses = list(self.enemy_chances_dict.keys())
        enemyWeights = list(self.enemy_chances_dict.values())
        enemy = r.choices(enemyClasses, weights=enemyWeights, k=1)[0]
        return enemy()
