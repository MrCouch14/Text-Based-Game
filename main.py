import random

# stats
hunger = 100
thirst = 100
rations = 5
health = 100
objective = 0
insanity = 0
survived_encounters = 0

# status effects
guide = False
shotgun = False
time_until_cleared = 0

def apply_status_effects():
    global hunger, thirst, objective, insanity, health, guide, time_until_cleared
    if guide == True:
        time_until_cleared += 1
        insanity -= 3
        objective += 2
        if time_until_cleared == 3:
            guide = False
            print('Your guide has left!')

def calculate_stats():
    global hunger, thirst, objective, insanity, survived_encounters
    hunger -= 10
    thirst -= 15
    objective += 1
    insanity += 1
    survived_encounters += 1
    apply_status_effects()

def get_user_input(prompt, valid_responses):
    #Helper function to get and validate user input.
    while True:
        response = input(prompt).strip().lower()
        if response in valid_responses:
            return response
        print(f'Invalid response. Please type one of {valid_responses}.')

def handle_events():
    global hunger, thirst, health, objective, insanity, rations, guide, shotgun, time_until_cleared
    
    if insanity < 15:
        event = random.randint(1, 10)

        if event == 1:  # Berry Bush Encounter
            print('You come across a bush of berries.')
            response = get_user_input('Should you eat the berries? (yes/no): ', ['yes', 'no'])
            if response == 'yes':
                outcome = random.randint(1, 2)
                if outcome == 1:
                    hunger += 5
                    print('You eat the berries and regain some hunger.')
                else:
                    health -= 20
                    print('You eat the berries and fall ill.')
            else:
                print('You move on.')

        elif event == 2:  # Uneven Terrain Encounter
            print('You come across uneven and steep terrain. Traversing it could hurt you but would be much faster.')
            response = get_user_input('What should you do next? (traverse the terrain/walk around): ', 
                                      ['traverse the terrain', 'walk around'])
            if response == 'traverse the terrain':
                outcome = random.randint(1, 3)
                if outcome in [1, 2]:
                    health -= 20
                    objective += 1
                    print('You fall down, gaining multiple small cuts and bruises but make it across.')
                else:
                    objective += 1
                    print('You made it across just fine.')
            else:
                objective -= 1
                print('You walk around the uneven terrain, taking a very long time.')

        elif event == 3:  # Deer Encounter
            print('You spot a deer grazing nearby. It hasn’t noticed you yet.')
            response = get_user_input('Do you try to hunt the deer or let it go? (hunt/let go): ', ['hunt', 'let go'])
            if response == 'hunt':
                insanity += 1
                outcome = random.randint(1, 2)
                if outcome == 1:
                    hunger += 20
                    print('You successfully hunt the deer and cook its meat, relieving your hunger.')
                else:
                    health -= 10
                    print('You fail to hunt the deer, and it kicks you as it escapes. You’re slightly injured.')
            else:
                print('You decide to let the deer go and move on peacefully.')

        elif event == 4:  # Abandoned Cottage Encounter
            print('You come across an old abandoned cottage.')
            response = get_user_input('Do you investigate the cottage? (yes/no): ', ['yes', 'no'])
            if response == 'yes':
                outcome = random.randint(1, 5)
                if outcome in [1, 4]:
                    rations += 3
                    objective -= 1
                    print('You search the cottage and find various supplies, increasing your rations but taking some time.')
                elif outcome == 5:
                    objective += 5
                    print('You find a map of the nearby area, greatly increasing your chance of finding your way out.')
                else:
                    insanity += 1
                    print('You search the cabin only to find nothing but blood-stained floorboards and half-eaten rotting food.')
            else:
                print('You press on, no need to waste time.')

        elif event == 5:  # River Encounter
            print('You come across a shallow river.')
            response = get_user_input('Should you try to cross it or turn around? (cross/turn around): ', ['cross', 'turn around'])
            if response == 'cross':
                outcome = random.randint(1, 2)
                if outcome == 1:
                    print('You successfully make it across the river.')
                else:
                    objective -= 4
                    print('The river current carries you far away, and you have no clue where you are.')
            else:
                objective -= 2
                print('You turn around, getting even more lost in the process.')

        elif event == 6:  # Fog Encounter
            print('At late night, a thick fog sets in.')
            response = get_user_input('Do you continue trying to find your way or camp out for the night? (camp/continue on): ', ['camp', 'continue on'])
            if response == 'camp':
                outcome = random.randint(1, 2)
                if outcome == 1:
                    print('You wake up later feeling no different than when you went to bed.')
                else:
                    health += 20
                    insanity -= 2
                    print('You wake up feeling well-rested.')
            else:
                outcome = random.randint(1, 3)
                if outcome in [1, 2]:
                    objective -= 2
                    insanity += 1
                    print('You get lost and sleep-deprived.')
                else:
                    print('You are somehow able to find your way.')

        elif event == 7:  # Creek Encounter
            print('You come across a small creek, but it looks a little dirty.')
            response = get_user_input('Do you drink from the creek? (yes/no): ', ['yes', 'no'])
            if response == 'yes':
                outcome = random.randint(1, 3)
                if outcome in [1, 2]:
                    health -= 20
                    thirst += 20
                    print('You drink from the creek and fall ill.')
                else:
                    thirst += 30
                    print('You drink from the creek and quench some of your thirst.')
            else:
                print('You move on.')

        elif event == 8: # Rustling Bushes Encounter
            print('You hear rustling in some nearby bushes.')
            response = get_user_input('Should you investigate the bushes? (yes/no):', ['yes', 'no'])
            if response == 'yes':
                if insanity > 20:
                    outcome = random.randint(1, 9)
                    if outcome in [1, 6]: # Animal in the bush
                        print('You come across a small animal.')
                        response = get_user_input('Should you cook and eat it? (yes/no):', ['yes', 'no'])
                        if response == 'yes':
                            outcome = random.randint(1, 2)
                            if outcome == 1: 
                                hunger += 25
                                print('You eat the animal and regain some hunger.')
                            elif outcome == 2:
                                hunger += 25
                                health -= 15
                                print('You eat the animal but get sick from it not being prepared properly.')
                        elif response == 'no':
                            print('You move on.')
                        else:
                            print('Invalid response. Please type "yes" or "no"')
                    elif outcome in [7, 8]: # Gnome in the bush
                        insanity -= 6
                        print('You find a small garden gnome in the bush, you are unsure if it is even real but it oddly fills you with determination to see this through.')
                    elif outcome == 9: # Eli in the bush
                        hunger += 50
                        thirst += 50
                        insanity -= 6
                        print('You reach your hand out to see what is inside of the bush, out of nowhere a blonde haired man steps out. He says "Hey its me, Eli! I finally found you! I have been looking to try to give you this record, give it a listen!" He hands you a large record case. Curious isnt it. He then winks and exclaims "Catch you later!", laughs, and runs off. You strangely feel much better.')
                else: # Wendigo in the bush
                    health -= 1000
                    print('When you reach out your hand to investigate the bushes, a sense of pure terror and dread overwhelmes you when you touch an antler. From the bush emerges an otherworldy hulking beast. It has a vaguely humanoid appearance, completely unnaturally slouched over, it ressembles a deer more than anything. Its head however has no skin at all, it is a bare skull, stained with blood. As you run for your life there is nothing you can do as its almost like it can predit your every mo-')
            elif response == 'no':
                insanity += 1
                print('You continue walking, a little paranoid.')

        elif event == 9: # Old Man Encounter
            print('Along your path you spot a frail looking old man.')
            response = get_user_input('Do you approach him? (yes/no):', ['yes', 'no'])
            if response == 'yes':
                outcome = random.randint(1, 5)
                if outcome in [1, 3]:
                    print('You approach the old man, he looks a little shifty however he waves at you with a smile on his face. "Where you from sunny? So nice to finally see a new face! I moved out here by myself with my family to escape the draft years ago and havent left since. I am a bit unsure the exact way out of the forest but I could provide you with food and shelter for the night if you would like that! Ever since my wife died I have been very lonely.')
                    response = input('Do you follow him? (yes/no)')
                    if response == 'yes':
                        print('You head to his cabin for the night.')
                        outcome = random.randint(1, 4)
                        if outcome == [1, 3]:
                            health += 50
                            hunger += 40
                            thirst += 40
                            insanity -= 5
                            objective -= 2
                            print('The old man leads you to his cottage where he gives you a nice warm meal and a comfortable place to sleep for the night, just as he promised.')
                        elif outcome == 4:
                            health -= 1000
                            print('The old man leads you to his cottage where everything seems normal at first. You head to bed but in what feels like moments are abruptly woken up with the old man leaning over you at the foot of the bed. Knife in hand. "I am sorry it had to come to this but I am just so hungry out here." The old man stabs you crazily, killing you.')
                    elif response == 'no':
                        print('You politely decline his offer despite his insistence and leave.')
                    else:
                        print('Invalid response. Please type "yes" or "no"')
                elif outcome in [4, 5]:
                    print('The old man waves to you excitedly. "Nice to meet a fellow traveller! I was just heading back home from camping out in these forests. I live just nearby! I can take you back to town if you want!"')
                    response = get_user_input('Do you follow him? (yes/no):', ['yes', 'no'])
                    if response == 'yes':
                        outcome = random.randint(1, 3)
                        if outcome in [1, 2]:
                            time_until_cleared = 0
                            guide = True
                            print('This guy knows what he is talking about! (For your next few turns you will gain a guide, giving you a higher chance of finding your way out of the forest.)')
                        elif outcome == 3:
                            objective -= 4
                            print('This old man is clearly crazy and leads you in circles, you eventually ditch him.')
                    else:
                        print('Invalid response. Please type "yes" or "no"')
            elif response == 'no':
                print('You pass him up, turning around before he notices you. Who knows what kind of pereson he is anyway.')

        elif event == 10: # Shotgun Encounter
            print('You find a loaded shotgun on the ground and put it in your backpack, while weary of why this might be here you pick it up as it could come in handy later.')
            shotgun = True
    else:
        health -= 1000
        print('You are beginning to go crazy, this forest is not what it seems. As you continue walking you see multiple deer carcases with their insides carved out on your path. It looks unnatural, no predator should be able to naturally do this. Thats when you hear rustling behind you. You turn around just to see a hulking creature, its appearance is almost half human half deer, just a lot larger than either creature. A sense of complete dread washes over you. The creature lunges at you and its blood soaked antlers stab into you, killing you instantly.')

print('You are lost in a forest alone, unsure of how you got here. you have basic supplies with you but nothing else. Your only objective is to find your way home and stay alive.')

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