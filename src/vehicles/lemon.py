import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'lemon',
              base_numeric_id = 1170,
              title = '2-10-0 Lemon [Steam]',
              str_type_info = 'COASTER',
              replacement_id = '-none',
              power = 2100,
              tractive_effort_coefficient = 0.29,
              speed = 65,
              buy_cost = 114,
              fixed_run_cost_factor = 3.5,
              fuel_run_cost_factor = 1.0,
              vehicle_life = 40,
              intro_date = 1935,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 97,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 52,
                        vehicle_length = 4,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
