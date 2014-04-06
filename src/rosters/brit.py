from roster import Roster

from vehicles import cargo_sprinter
from vehicles import chaplin
from vehicles import chinook
from vehicles import collier
from vehicles import cyclops
from vehicles import donegal
from vehicles import double_juice
from vehicles import electra
from vehicles import gridiron
from vehicles import high_flyer
from vehicles import hudswell
from vehicles import lemon
from vehicles import little_bear
from vehicles import northcock
from vehicles import planet
from vehicles import ramsbottom
from vehicles import raven
from vehicles import screamer
from vehicles import slammer
from vehicles import standard
from vehicles import stewart
from vehicles import suburban
from vehicles import tin_rocket
from vehicles import vulcan
from vehicles import walker

roster = Roster(id = 'brit',
                buy_menu_sort_order = [
                                       'chaplin',
                                       'standard','ramsbottom',
                                       'collier',
                                       'high_flyer',
                                       'raven',
                                       'suburban',
                                       'northcock',
                                       'lemon',
                                       'electra',
                                       'chinook',
                                       'vulcan',
                                       'little_bear',
                                       'gridiron',
                                       'screamer',
                                       'cargo_sprinter',
                                       'double_juice',
                                       'cyclops',
                                       'slammer',
                                       'tin_rocket',
                                       # brit extras
                                       'metro_mu_brit_extras_gen_1',
                                       'metro_mu_brit_extras_gen_2',
                                       'metro_mu_brit_extras_gen_3',
                                       'metro_loco_brit_extras_gen_1',
                                       'metro_car_brit_gen_1', # special case, non-standard naming, and this is explicitly placed after metro locos, unlike most cars which are automatically placed in buy menu
                                       # brit ng
                                       'stewart',
                                       'hudswell',
                                       'donegal',
                                       'planet',
                                       'walker'])
