import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'bertha',
              base_numeric_id = 70,
              title = '0-10-0 Big Bertha [Steam]',
              power = 1800,
              tractive_effort_coefficient = 0.33,
              speed = 45,
              type_base_buy_cost_points = 10, # dibble buy cost for game balance
              vehicle_life = 40,
              intro_date = 1900)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 95,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 40,
                        vehicle_length = 4,
                        spriterow_num = 1))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
