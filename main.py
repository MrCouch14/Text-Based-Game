import random

# stats
hunger = 100
thirst = 100
rations = 5
health = 100
objective = 0
insanity = 0
survived_encounters = 0

def calculate_stats():
    global hunger, thirst, objective, insanity, survived_encounters
    hunger -= 10
    thirst -= 15
    objective += 1
    insanity += 1
    survived_encounters += 1

def handle_events():
    global hunger, thirst, health, objective, insanity, rations
    event = random.randint(1, 8)
    if event == 1: # Berry Bush Encounter
        print('You come across a bush of berries.')
        while True:
            response = input('Should you eat the berries? (yes/no): ').lower()
            if response == 'yes':
                outcome = random.randint(1, 2)
                if outcome == 1:
                    hunger += 5
                    print('You eat the berries and regain some hunger.')
                    break
                elif outcome == 2:
                    health -= 20
                    print('You eat the berries and fall ill.')
                break
            elif response == 'no':
                print('You move on.')
                break
            else:
                print('Invalid response. Please type "yes" or "no".')

    elif event == 2: # Uneven Terrain Encounter
        print('You come across uneven and steep terrain, traversing it could hurt you but would be much faster.')
        while True:
            response = input('What should you do next? (traverse the terrain/walk around): ').lower()
            if response == 'traverse the terrain':
                outcome = random.randint(1, 3)
                if outcome in [1, 2]:
                    health -= 20
                    objective += 1
                    print('You fall down, gaining multiple small cuts and bruises but make it across.')
                elif outcome == 3:
                    objective += 1
                    print('You made it across just fine.')
                break
            elif response == 'walk around':
                objective -= 1
                print('You walk around the uneven terrain taking a very long time.')
                break
            else:
                print('Invalid response. Please type "traverse the terrain" or "walk around".')

    elif event == 3: # Deer Encounter
        print('You spot a deer grazing nearby. It hasn’t noticed you yet.')
        while True:
            response = input('Do you try to hunt the deer or let it go? (hunt/let go): ').lower()
            if response == 'hunt':
                insanity += 1
                outcome = random.randint(1, 2)
                if outcome == 1:
                    hunger += 20
                    print('You successfully hunt the deer and cook its meat, relieving your hunger.')
                elif outcome == 2:
                    health -= 10
                    print('You fail to hunt the deer, and it kicks you as it escapes. You’re slightly injured.')
                break
            elif response == 'let go':
                print('You decide to let the deer go and move on peacefully.')
                break
            else:
                print('Invalid response. Please type "hunt" or "let go".')
    elif event == 4: # Abandoned Cottage Encounter
        print('You come across an old abandoned cottage')
        while True:
            response = input('Do you investigate the cottage? (yes/no)').lower()
            if response == 'yes':
                if insanity > 15:
                    rations += 2
                    objective -= 1
                    print('You search the cottage and find various supplies, increasing your rations but taking some time.')
                    break
                else:
                    insanity += 1
                    print('You search the cabin only to find nothing but blood stained floorboards and half eaten rotting food.')
                    break
            elif response == 'no':
                print('You press on, no need to waste time.')
                break
            else:
                print('Invalid response. Please type "yes" or "no"')
    elif event == 5: # River Encounter
        print('You come across a shallow river.')
        while True:
            response = input('Should you try to cross it or turn around? (cross/turn around)').lower()
            if response == 'cross':
                outcome = random.randint(1, 2)
                if outcome == 1:
                    print('You successfully make it across the river.')
                    break
                elif outcome == 2:
                    objective -= 4
                    print('The river current carries you far away, you have no clue where you are.')
                    break
            elif response == 'turn around':
                objective -= 2
                print('You turn around, getting even more lost in the process.')
                break
            else:
                print('Invalid response. Please type "cross" or "turn around"')
    elif event == 6: # Fog Encounter
        print('At late night a thick fog sets in.')
        while True:
            response = input('Do you continue trying to find your way or camp out for the night? (camp/continue on)').lower()
            if response == 'camp':
                outcome = random.randint(1, 2)
                if outcome == 1:
                    print('You wake up later feeling no different than when you went to bed.')
                    break
                elif outcome == 2:
                    health += 20
                    insanity -= 2
                    print('You wake up feeling well rested.')
                    break
            elif response == 'continue on':
                outcome = random.randint(1, 3)
                if outcome in [1, 2]:
                    objective -= 2
                    insanity += 1
                    print('You get lost and sleep deprived.')
                    break
                elif outcome == 3:
                    print('You are somehow able to find your way.')
                    break
            else:
                print('Invalid response. Please type "camp" or "continue on"')
    elif event == 7: # Creek Encounter
        print('You come across a small creek, it looks a little dirty.')
        while True:
            response = input('Do you drink from the creek? (yes/no)').lower()
            if response == 'yes':
                outcome = random.randint(1, 3)
                if outcome in [1, 2]:
                    health -= 20
                    thirst += 20
                    print('You drink from the creek and fall ill.')
                    break
                elif outcome == 3:
                    thirst += 30
                    print('You drink from the creek and quench some of your thirst.')
                    break
            elif response == 'no':
                print('You move on.')
                break
            else:
                print('Invalid response. Please type "yes" or "no"')
    elif event == 8: # Rustling Bushes Encounter
        print('You hear rustling in some nearby bushes.')
        while True:
            response = input('Should you investigate the bushes? (yes/no)').lower()
            if response == 'yes':
                if insanity > 20:
                    outcome = random.randint(1, 9)
                    if outcome in [1, 6]: # Animal in the bush
                        print('You come across a small animal.')
                        response = input('Should you cook and eat it? (yes/no)')
                        if response == 'yes':
                            outcome = random.randint(1, 2)
                            if outcome == 1: 
                                hunger += 25
                                print('You eat the animal and regain some hunger.')
                                break
                            elif outcome == 2:
                                hunger += 25
                                health -= 15
                                print('You eat the animal but get sick from it not being prepared properly.')
                                break
                        elif response == 'no':
                            print('You move on.')
                            break
                        else:
                            print('Invalid response. Please type "yes" or "no"')
                    elif outcome in [7, 8]: # Gnome in the bush
                        insanity -= 6
                        print('You find a small gnome in the bush, you are unsure if it is even real but it oddly fills you with determination to see this through.')
                    elif outcome == 9: # Eli in the bush
                        hunger += 50
                        thirst += 50
                        insanity -= 6
                        print('You reach your hand out to see what is inside of the bush, out of nowhere a blonde haired man steps out. He says "Hey its me, Eli! I finally found you! I have been looking to try to give you this record, give it a listen!" He hands you a large record case, the front reads "OK Computer". Curious isnt it. He then winks and exclaims "Catch you later!", laughs, and runs off. You strangely feel much better.')
                        break
                else: # Wendigo in the bush
                    health -= 1000
                    print('When you reach out your hand to investigate the bushes, a sense of pure terror and dread overwhelmes you when you touch an antler. From the bush emerges an otherworldy hulking beast. It has a vaguely humanoid appearance, completely unnaturally slouched over, it ressembles a deer more than anything. Its head however has no skin at all, it is a bare skull, stained with blood. As you run for your life there is nothing you can do as its almost like it can predit your every mo-')
                    break
            elif response == 'no':
                insanity += 1
                print('You continue walking, a little paranoid.')
                break
            else:
                print('Invalid response. Please type "yes" or "no"')

print('You are lost in a forest alone, you have basic supplies with you but nothing else. Your only objective is to find your way home and stay alive.')

# game loop
response = ""
while response != 'quit':
    current_situation = f'This is your current Situation: Hunger: {hunger}, Thirst: {thirst}, Rations: {rations}, Health: {health}, Objective: {objective}, Insanity: {insanity}'
    print(current_situation)
    response = input('What should you do? (advance, consume rations, quit): ').lower()
    if response == 'advance':
        handle_events()
        calculate_stats()
    elif response == 'consume rations':
        if rations > 0:
            if hunger <= 90 or thirst <= 90:
                hunger += 10
                thirst += 10
                rations -= 1
                print('You consume a ration and feel a bit better.')
            else:
                print('You are already full!')
        else:
            print('You have no rations left!')
    elif response == 'quit':
        print('You quit the game. Goodbye!')
    else:
        print('Invalid response.')

    # Check if the player is still alive
    if hunger <= 0 or thirst <= 0 or health <= 0:
        print(f'You succumb to the harsh forest conditions... You survived {survived_encounters} encounters!')
        break
    # Check if the player has won
    if objective == 15:
        print('You make it back to town safely! (Hope you enjoyed playing! :)')
        break