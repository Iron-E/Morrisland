from sys import path
path.append('./Gilbo-API/')
path.append('./Gilbo-API/deps/')
import Gilbo as G


#
# Objects #
#

# NPCs #
narrator = G.NPC('Narrator', None, None, None)
black_suit_narrator = G.NPC('The Man in the black suit', None, None, None)

# Battlers #

# Attacks #
pass

# Weapons #
# chop_sticks = G.weapon()
# katana = G.weapon()
# black_belt = G.weapon()
# black_suit_prebuff = G.weapon()
# black_suit_buffed = G.weapon()

# Armor #
pass

# Buffs/Heals #
black_suit_buff = G.stat_item('Mysterious Orange Liquid', 'A mysterious orange liquid that was used by the Man in the Black Suit.', 1000, 10, 0, 25, 5, -10)
msg = G.stat_item('MSG', 'Super Salt. Seriously bad for you, but a seriously wild ride.', 5, 2, 0, 10, 0, 10)
# Add function to summon General Tso's chicken if consumed
tso_chicken = G.stat_item("General Tso's Chicken", "Nothing incites a fighting spirit like the effigy of General Tso's Chicken. Why did the General only have one?", 20, 3, 30)

noodles = G.heal_item('Noodles', "A cup of Alton Brown's world-famous noodles.", 10, 8)
msg_noodles = G.heal_item('MSG Noodles', "Alton Brown's noodles, now with 150% more MSG. It seems to good to be true, so you'll probably pay for it later...", 2, 20)
lo_mein = G.heal_item('Lo Mein', "Alton Brown's signature Lo Mein. You'd slurp the noodles if he weren't watching.", 7, 10)

# Boss-related objects #
pass
