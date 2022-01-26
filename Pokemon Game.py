+   import random,pickle,time


#-----------------Pokemon Class----------------------------
class Pokemon:
    def __init__(self,pokemon_name,health):
        self.health = health
        self.name = pokemon_name

        #Each pokemon's move set
        self.moves = {"Tackle": 10, "Scratch":15}


##        def faint():
##            print(self.name,"has fainted")
#------------------Player Class--------------------
class Player:
##    def __init__(self,player_name,exp,gold,pokemon_list):
##        self.name = player_name
##        self.exp = exp
##        self.gold = gold
##        self.pokemon = pokemon_list

    #All values are intizilized but are changed using set and get methods
    def __init__(self):
        self.name = ""
        self.exp = 0
        self.gold = 0
        
        #The list of pokemon each player has
        #total number of pokemon each player has is equal to the size of the list
        self.pokemon_list = []

        #Every pokemon encountered is stored here5
        self.pokedex = []

        #The dictionary(list) of items each player has
        self.items = {}

    def set_name(self,name):
        self.name = name


    #Adds pokemon to the list of pokemon the player currently has
    def add_pokemon(self,pokemon_name,health):
        pokemon = Pokemon(pokemon_name,health)
        self.pokemon_list.append((pokemon))

    #Add to pokedex
    def add_to_pokedex(self,pokemon_name):
        pokemon = Pokemon(pokemon_name,000)
        self.pokedex.append(pokemon.name)

    #Add to bag
    def add_item(self,item_name,quantity):
        self.items[item_name] = quantity



        
#-----------------Choose Your pokemon----------------------
def choose_starter():
    print("Well",player.name,"it's now time for you to choose your very first starter pokemon")
    print('--------------------------------------------------------------------------------')
    print('There are 3 choices : Bulbasaur, Charmander and Squirtle')
    choice = input('Choose starter : ')
    choice = choice.lower()
    #Default health for starter pokemon is 100
    if choice == 'bulbasaur':
        catch_pokemon('Bulbasaur',100,250);
    elif choice == 'charmander':
        catch_pokemon('Charmander',100,250);
    elif choice == 'squirtle':
        catch_pokemon('Squirtle',100,250);
    else:
        print('**\nThat is not a starter pokemon please type <y> try again\n**')
        error = input('Enter : ')
        error = error.lower()
        if error == 'y' or error == 'yes':
            choose_starter()
        else:
            print('Press <n> to exit ')
            secret = input('Enter : ') #Secret easter egg to unlock pikachu
            secret = secret.lower()
            if secret == 'n':
                exit()
            else:
                catch_pokemon('Pikachu',100,500);
                
    print("Well",player.name,"now with your new starter you are on your way to become a pokemon master")
    print("Before you go let me give a couple of items to help you on your journey \nYou have gained 5 pokeballs\nYou have gained 5 potions")
    print("Use pokeballs to catch other pokemon and potions to heal your own pokemon\n")
    player.add_item("Pokeball",5)
    player.add_item("Potion",5)

#------------------------------Catch pokemon----------------------------------    
def catch_pokemon(pokemon_name,health,gold):
    print("        ────────▄███████████▄────────")
    print("        ─────▄███▓▓▓▓▓▓▓▓▓▓▓███▄─────")
    print("        ────███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███────")
    print("        ───██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██───")
    print("        ──██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██──")
    print("        ─██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██─")
    print("        ██▓▓▓▓▓▓▓▓▓███████▓▓▓▓▓▓▓▓▓██")
    print("        ██▓▓▓▓▓▓▓▓██░░░░░██▓▓▓▓▓▓▓▓██")
    print("        ██▓▓▓▓▓▓▓██░░███░░██▓▓▓▓▓▓▓██")
    print("        ███████████░░███░░███████████")
    print("        ██░░░░░░░██░░███░░██░░░░░░░██")
    print("        ██░░░░░░░░██░░░░░██░░░░░░░░██")
    print("        ██░░░░░░░░░███████░░░░░░░░░██")
    print("        ─██░░░░░░░░░░░░░░░░░░░░░░░██─")
    print("        ──██░░░░░░░░░░░░░░░░░░░░░██──")
    print("        ───██░░░░░░░░░░░░░░░░░░░██───")
    print("        ────███░░░░░░░░░░░░░░░███────")
    print("        ─────▀███░░░░░░░░░░░███▀─────")
    print("        ────────▀███████████▀────────")
    player.add_pokemon(pokemon_name,health)
    player.add_to_pokedex(pokemon_name)
    player.gold += gold
    print("\tYou have caught",pokemon_name ,"and he has been added to your pokedex, and you have also gained", gold,"gold.\n")


#-----------------Start game-----------
def start():
    start_game = input('Type y/yes to play :')
    start_game = start_game.lower()
    if start_game == 'y' or start_game == 'yes':
        print('Loading...')
        time.sleep(1)
        print('Have you played before ?')
        choice = input('Yes or No? <y/n>:')
        choice = choice.lower()
        if choice == 'y' or choice == 'yes':
            pass
            #load()
            #room()
        elif choice == 'n' or choice == 'no':
            print('Hello there my name is Professor Oak. What is your name? ')
            player.set_name(input("Enter name: "))
        else:
            print("**\nInvlaid option please try again\n**")
            start()
    elif start_game == "n" or start_game == "no":
        exit()
    else:
        print("**\nInvlaid option please try again\n**")
        start()


#-------------------Game Hub--------------
def hub():
    print("There are 3 options from here \n1 - Go to town \n2 - Go into the forest \n3 - Go home ")
    choice = int(input('Enter : '))
    if choice == 1:
        town()
    elif choice == 2:
        explore()
    elif choice == 3:
        home()
    else:
        print("**\nInvlaid option please try again\n**")
        hub()


#------------------------Explore--------------------
def explore():
        print('\tExploring...')
        time.sleep(2)
        random_pokemon = Pokemon(random.choice(gen1),random.randint(50,300))
        print('\tA wild',random_pokemon.name,'with',random_pokemon.health,'health has appeared')
        player.add_to_pokedex(random_pokemon.name)
        current_pokemon = player.pokemon_list[0]
        print("\tYou have thrown out",current_pokemon.name)
        battle_menu(random_pokemon,current_pokemon)


#------------------Battle Menu--------------
def battle_menu(pokemon_rand,current_pokemon):

    original_health = pokemon_rand.health
 
    
    print("\t-------------")
    print("\t|Fight   Bag|")
    print("\t|Pokemon Run|")
    print("\t-------------")
    
    choice = input('\tEnter instruction: ')
    choice = choice.lower()
    if choice == 'fight':
        fight(pokemon_rand,current_pokemon)
        
    elif choice == 'pokemon':
       current_pokemon = switch_pokemon()
       battle_menu(pokemon_rand,current_pokemon)
       
    elif choice == 'bag':
        chosen_item = bag()
        if chosen_item == "Pokeball":
            #100% Catch rate iif health is below 50
            if(pokemon_rand.health <= 50):
                catch_pokemon(pokemon_rand.name,original_health,100)#
                hub()

            #1/3 catch rate is health is less than 100
            elif(pokemon_rand.health <= 100):
                chance = random.randint(1,3)
                if(chance == 1):
                    catch_pokemon(pokemon_rand.name,original_health,100)
                    hub()
                else:
                    print(pokemon_rand.name,"has broken out")
                    battle_menu(pokemon_rand,current_pokemon)
            #1/5 catch rate is health is above 100
            elif(pokemon_rand.health > 100):
                chance = random.randint(1,5)
                if(chance == 1):
                    catch_pokemon(pokemon_rand.name,original_health,100)
                    hub() 
                else:
                    print(pokemon_rand.name,"has broken out")
                    battle_menu(pokemon_rand,current_pokemon)
        elif chosen_item == "Potion":
            current_pokemon.health += 30
            print(current_pokemon.name, "has been healed and now has", current_pokemon.health,"health")
        else:
            print(chosen_item)


    elif choice == 'run':
        chance = random.randint(2)
        if chance == 1:
            start()
        else:
            print('\tCould not run away')
            battle_menu(pokemon_rand,current_pokemon)
            
    else:
        print("**\nInvlaid option please try again\n**")
        battle_menu(pokemon_rand,current_pokemon)


#---------------------Switch pokemon-----------
def switch_pokemon():
    list_pokemon = []
    for pokemon in player.pokemon_list:
       list_pokemon.append(pokemon.name)
    print(list_pokemon)
       #put in calss as print method
    choose_pokemon = input("Choose which pokemon to send out:")
    for i in range (len(player.pokemon_list)):
        if player.pokemon_list[i].name.lower() == choose_pokemon.lower():
            print("\tYou have thrown out",player.pokemon_list[i].name)
            return player.pokemon_list[i]
    print("Cannot find pokemon")
    
    
#-----------------Bag-----------------------
def bag():
    for item,number in player.items.items():
        print("\t",item,number)
    choose_item = input("\tChoose item:")
    for item in player.items:
        if choose_item.lower() == item.lower():
            return item
    return "No items found"




#--------------------Fight--------------------
def fight(pokemon_rand,current_pokemon):
    list_moves = list(current_pokemon.moves.keys())
    number_moves = list(current_pokemon.moves.values())
    print("\t------------------------------------------")
    print("\t|1 - ",list_moves[0],"(",number_moves[0],")     2 - ",list_moves[1],"(",number_moves[1],")|")
    print("\t|3 - ......           4 - Back          |")
    print("\t------------------------------------------")
    pick = input('\tEnter: ')

    if current_pokemon.health <= 0:
        print("\t",current_pokemon.name,"has fainted please choose a another pokemon to fight with")
        battle_menu(pokemon_rand,current_pokemon)

    if pick == '1':
        print ('\t',current_pokemon.name,'used Tackle')
        current_pokemon.moves.update({list_moves[0]:number_moves[0]-1})
        #Tackle deals 50 damage
        pokemon_rand.health -= 50
        if pokemon_rand.health <= 0 :
            faint(pokemon_rand)
        else:
            print('\t',pokemon_rand.name,'has',pokemon_rand.health,'health left')
            print("\t",pokemon_rand.name, "used headbutt it did 10 damage")
            current_pokemon.health -=10
            print("\t",current_pokemon.name, "has",current_pokemon.health,"health left")
            fight(pokemon_rand,current_pokemon)


    elif pick == '2':
        print ('\t',current_pokemon.name,'used Scratch')
        current_pokemon.moves.update({list_moves[1]:number_moves[1]-1})
        #Scratch deals 35 damage
        pokemon_rand.health -= 35
        if pokemon_rand.health <= 0 :
            faint(pokemon_rand)
        else:
            print('\t',pokemon_rand.name,'has',pokemon_rand.health,'health left')
            print("\t",pokemon_rand.name, "used headbutt it did 10 damage")
            current_pokemon.health -=10

            print("\t",current_pokemon.name, "has",current_pokemon.health,"health left")
            fight(pokemon_rand,current_pokemon)


    else:
        leave = input('\tAre you trying to go back to Battle menu: ')
        leave = leave.lower()
        if leave == 'y' or leave == 'yes':
            battle_menu(pokemon_rand,current_pokemon)
        else:
            fight(pokemon_rand,current_pokemon)




#-------------------------Pokemon Fainted --------------------------------
def faint(pokemon_rand):
    
    print('\tYou have made',pokemon_rand.name,'faint')
    print('\thave gained 250 gold')
    player.gold += 250
    hub()


#--------------Save game--------------
def save():
    print("What do you want to call this save")
#--------------Globals----------------

#List of all generation one pokemon 
gen1 = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran","Nidorina","Nidoqueen","Nidoran","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
player = Player()#Player is allowed to be global as there can only be one player at a given time 

#------------------------
##player.set_name("No")
##print(player.player_name)
##player.add_pokemon("bulbasaur",100)
##player.add_pokemon("charmander",100)
##
##for pokemon in player.pokemon_list:
##    print(pokemon.pokemon_name,pokemon.health)




#need to use pointers to load game data

start()
choose_starter()
hub()
#--------------------------------------------------        
##p1 = pokemon("Char", 49)
##print(p1.name)
