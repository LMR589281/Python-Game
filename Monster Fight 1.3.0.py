#Monster Fight 2.0
import time #time.sleep(5)
import random #player_damage=random.randint(3,7)
import webbrowser #webbrowser.open('https://support.t-mobile.com/docs/DOC-5325')
hit_points=20
monster_health=250
fire_attack=1
ice_attack=2
air_attack=3
earth_attack=5
healing_items=5
knife=0
armour=0
mercy=3
talk=3
flee=3
wins=0
losses=0
###########################################################
print("The Monster Stands Before You")
while hit_points >0 and monster_health >0 and flee>0 and talk>0 and mercy>0:
    print("Your Health Is",hit_points)
    print("The Monster's Health Is",monster_health)
    one=input("""
    1)Fight    2)Magic
    3)Items   4)Mercy
    """)
    if armour==1:
            monster_damage=random.randint(1,5)
    else:
            monster_damage=random.randint(3,7)
    if one=="1":
        fight=input("\n   1)Attack 1(More Reliable, But Less Damage)\n   2)Attack2(Less Reliable, But More Damage)\n   ")
        if fight=="1":
            if knife==1:
                player_damage=random.randint(6,8)
                if player_damage==8:
                    print("\nCritical Hit")
                else:
                    print("\nYou Did",player_damage,"Damage To The Monster")
            else:     
                player_damage=random.randint(4,6)
                if player_damage==6:
                    print("\nCritical Hit")
                else:
                    print("\nYou Did",player_damage,"Damage To The Monster")
            monster_health = monster_health-player_damage       
            print("The Monster Did",monster_damage,"Damage To You\n")
            hit_points=hit_points-monster_damage
        elif fight=="2":
            if knife==1:
                player_damage=random.randint(4,10)
                if player_damage==8:
                    print("\nCritical Hit")
                else:
                    print("\nYou Did",player_damage,"Damage To The Monster")
            else:
                player_damage=random.randint(2,8)
                if player_damage==8:
                    print("\nCritical Hit")
                else:
                    print("\nYou Did",player_damage,"Damage To The Monster")
            monster_health = monster_health-player_damage       
            print("The Monster Did",monster_damage,"Damage To You\n")
            hit_points=hit_points-monster_damage
        else:
            print("Enter 1 Or 2\n")
###########################################################   
    elif one=="2":
        magic=input("\n    1)Fire   2)Ice\n    3)Air    4)Earth\n    ")
        if magic=="1":
            if fire_attack >= 1:
                print("You Summed A Wave Of Fire For 60 Damage")
                monster_health=monster_health-60
                fire_attack=fire_attack-1
                print("The Monster Did",monster_damage,"Damage To You\n")
                hit_points=hit_points-monster_damage
            else:
                print("You Have No Fire Spells Left\n")
        elif magic=="2":
            if ice_attack >=1:
                print("You Summed A Wave Of Ice For 40 Damage")
                monster_health=monster_health-40
                ice_attack=ice_attack-1
                print("The Monster Did",monster_damage,"Damage To You\n")
                hit_points=hit_points-monster_damage
            else:
                print("You Have No Ice Spells Left\n")
        elif magic=="3":
            if air_attack >=1:
                print("You Summed A Wave Of Air For 20 Damage")
                monster_health=monster_health-20
                air_attack=air_attack-1
                print("The Monster Did",monster_damage,"Damage To You\n")
                hit_points=hit_points-monster_damage
            else:
                print("You Have No Air Spells Left\n")
        elif magic=="4":
            if earth_attack >=1:
                print("You Summed A Wave Of Earth For 5 Damage")
                monster_health=monster_health-5
                earth_attack=earth_attack-1
                print("The Monster Did",monster_damage,"Damage To You\n")
                hit_points=hit_points-monster_damage
            else:
                print("You Have No Earth Spells Left\n")
        else:
            print("Nothing Happened\n")
###########################################################        
    elif one=="3":
        items=input("\n    1)Healing    2)Ball\n    3)Knife       4)Armour\n    ")
        if items=="1":
            if healing_items >= 1:
                        healed=random.randint(8,13)
                        if healed>=8 and healed <=10:
                            print("\nYou Ate An Apple And Healed",healed,"Hit Points")
                            hit_points=hit_points+healed
                        elif healed==11 or healed==12:
                            print("\nYou Ate An Peach And Healed",healed,"Hit Points")
                            hit_points=hit_points+healed
                        elif healed==13:
                            print("\nYou Ate An Sandwitch And Healed 13 Hit Points")
                            hit_points=hit_points+healed
                        else:
                            print("\nHow Did You Get Here?")
                        healing_items=healing_items-1
                        print("You Only Have",healing_items,"Healing Items Left")
                        print("The Monster Did",monster_damage,"Damage To You\n")
                        hit_points=hit_points-monster_damage
            else:
                print("\nYou Have No Healing Items Left\n")
        elif items=="2":
            print("You Through The Ball At The Monster, It Throughs It Back")
            time.sleep(3)
            print("Yay?\n")
        elif items=="3":
            if knife==0:
                print("You Equipped The Knife And Your Attack Upgraded")
                knife=knife+1
                print("The Monster Did",monster_damage,"Damage To You\n")
                hit_points=hit_points-monster_damage
            else:
                print("You Have Already Equipped The Knife")
        elif items=="4":
            if armour==0:
                print("You Equipped The Armour And Your Defence Upgraded")
                armour=armour+1            
                print("The Monster Did",monster_damage,"Damage To You\n")
                hit_points=hit_points-monster_damage
            else:
                print("You Have Already Equipped The Armour")
        else:
            print("Enter 1,2,3 Or 4\n")
###########################################################                    
    elif one=="4":
        spare=input("\n    1)Mercy    2)Talk\n    3)Flee\n    ")
        if spare=="1":
            if mercy==1:
                print("You Spared The Monster\n")
                print("It Finaly Got What You Said")
                mercy=mercy-1
            else:
                print("\nYou Tryed To Spare The Monster")
                print("It Did Not Understand You")
                mercy=mercy-1
                print("The Monster Did",monster_damage,"Damage To You\n")
                hit_points=hit_points-monster_damage
               
        elif spare=="2":
            if talk==1:
                print("You Talked To The Monster\n")
                print("It Finaly Got What You Said")
                talk=talk-1
            else:
                print("\nYou Talked To The Monster")
                print("It Did Not Understand You")
                talk=talk-1
                print("The Monster Did",monster_damage,"Damage To You\n")
                hit_points=hit_points-monster_damage
            
        elif spare=="3":
            if flee==1:
                print("You Got Away\n")
                flee=flee-1
            else:
                print("\nYou Tryed To Flee The Monster")
                flee=flee-1
                print("The Monster Did",monster_damage,"Damage To You\n")
                hit_points=hit_points-monster_damage   
        else:
            print("Please Enter 1,2 Or 3\n")
###########################################################
    else:
        print("Please Enter 1,2,3 Or 3\n")
###########################################################
print("Battle Ended")
if flee==0:
    print("You Ran Away")
elif talk==0:
    print("You Talked To The Monster And Stoped The Fighting")
elif mercy==0:
    print("You Spared The Monster And Stopped Fighting")
elif hit_points <= 0:
    print("You Died")
    print("Game Over")
    losses=losses+1
elif monster_health <= 0:
    print("You Killed The Monster")
    print("Well Done")
    wins=wins+1
else:
    print("How did you get here?")
    print("I know your just a dirty hacker, arn't you.")
input("Press Enter To End")
