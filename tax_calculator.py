from sys import path
path.append('./Gilbo-API/')
path.append('./Gilbo-API/deps/')
import Gilbo as G


#
# Objects #
#

# Ammo #
stamina = G.item('Stamina', "Your body's natural energy.", 0)
spray_can = G.item('Pepper Spray', 'A can of pepper spray.', 10)

# Buffs/Heals #
# Buffs
black_suit_buff = G.stat_item('Mysterious Orange Liquid', 'A mysterious orange liquid that was used by the Man in the Black Suit.', 1000, 10, 0, 25, 5, -10)
msg = G.stat_item('MSG', 'Super Salt. Seriously bad for you, but a seriously wild ride.', 5, 2, 0, 10, 0, 10)
# Add function to summon General Tso's chicken if consumed
tso_chicken = G.stat_item("General Tso's Chicken", "Nothing incites a fighting spirit like the effigy of General Tso's Chicken. Why did the General only have one?", 20, 3, 30)

# Heals
noodles = G.heal_item('Noodles', "A cup of Alton Brown's world-famous noodles.", 10, 10)
msg_noodles = G.heal_item('MSG Noodles', "Alton Brown's noodles, now with 150% more MSG. It seems to good to be true, so you'll probably pay for it later...", 2, 20)
lo_mein = G.heal_item('Lo Mein', "Alton Brown's signature Lo Mein. You'd slurp the noodles if he weren't watching.", 7, 15)
sushi_roll = G.heal_item('California Roll', 'California Roll hand-crafted by Alton Brown. You can smell the seacost.', 5, 5)

# Debuffs
surprise_debuff = G.stat_item("Caught By Surprise", "Someone was caught by surprise and suffered the consequence.", 0, 1, -5, -5, -5, -7)
defense_down = G.stat_item ('Defense Down', "The bearer's defense has been lowered.", 0, 3, -5, 0, -10)
enrage_debuff = G.stat_item('Enraged', 'The bearer has been taunted, leaving them stronger, but also reckless.', 0, 2, 0, 10, -15, 5)
irritated_eyes = G.stat_item('Irritated Eyes', "The bearer's eyes have been irritated by some chemical, causing them to miss attacks and present openings in their defense.", 0, 2, 0, -6, -10)

# Attacks #
# For katana
quick_draw = G.ammo_attack('Quick Draw', 'Draw your sword from its sheath at lightning speed.', 5, stamina, 3, 100, surprise_debuff)
cross_slash = G.ammo_attack('Cross Slash', 'Quickly slash twice at your oppnent, weakening their defense.', 6, stamina, 1, 100, defense_down)
parry = G.attack('Parry', 'Parry an attack from your opponent, enraging them while leaving them defenseless.', 2, 100, enrage_debuff)
sword_dance = G.attack('Sword Dance', 'Weave around the enemy slicing so thinly it would appear to be a dance.', 8)

# For black belt
charge = G.attack('Charge', 'Charge towards the enemy with great force', 10)
flying_kick = G.attack('Flying Scissor Kick', 'Leap at the enemy with a Scissor Kick.', 20, 65)
high_kick = G.attack('High Kick', 'Lean back and kick high with your good leg.', 15, 85)
low_sweep = G.ammo_attack('Low Sweep', 'Sweep your leg and temporarily disarm the apponent.', 8, stamina, 1, 100, surprise_debuff)

# For pre-buff blacksuit
shin_kick = G.attack('Shin Kick', "Kick your opponent's shin.", 8)
pepper_spray = G.ammo_attack('Use Pepper Spray', "Shoot pepper spray into the eyes of your opponent.", 2, spray_can, 1, 90, irritated_eyes)
throw_chair = G.attack('Throw Chair', 'Grab a nearby chair and throw it at the opponent.', 25, 60)
punch = G.attack('Punch', 'Deliver a flurry of punches to your opponent.', 13, 90)

# For buffed blacksuit
bash = G.attack('Skull Bash', 'Bash your head into the oppnent.', 11)
throw_table = G.attack('Throw Table', 'Throw a table at your opponent.', 30, 45)

# Weapons #
# User Weapons
chop_sticks = G.weapon('Chop Sticks', 'A pair of chopsticks you had used to eat your meal. If you believe in yourself, who knows what might happen?', 1, [sword_dance, quick_draw, cross_slash, parry, charge, flying_kick, low_sweep, high_kick, punch, shin_kick, pepper_spray, throw_chair, bash, throw_table], 5, 5, 5, 5, 1) # generate random attack from ALL attacks defined
katana = G.weapon('Katana', 'A weapon proven deadly when used in the right hands. Catch your enemies by surprise, or just impress them with your collection.', 100, [sword_dance, quick_draw, cross_slash, parry], 5, 8, 0, 12) # status weapon
black_belt = G.weapon('Black Belt', 'A weapon worn around the waist. Grants user impeccable hand-to-hand combat ability. Or, supposedly, it could be used to towel-snap your opponent.', 5, [charge, flying_kick, low_sweep, high_kick], 10, 10, 5) # regular damage
# Boss Weapons
black_suit_prebuff = G.weapon("Agent's Arsenal", 'An array of items and techniques known and used by the FBI.', 1000, [punch, shin_kick, pepper_spray, throw_chair])
black_suit_buffed = G.weapon('Herculean Brawn', "After injection of a mysterious liquid, the FBI agent has turned into a terrifying bruiser.", 5000, [bash, punch, shin_kick, throw_table])

# Entity-related #

# Collections

# Stat Lists

# NPCs
narrator = G.NPC('Narrator', None, None, None)
black_suit_narrator = G.NPC('The Man in the black suit', None, None, None)

# Battlers
