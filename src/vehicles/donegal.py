import global_constants
from train import EngineConsist, DieselRailcar

consist = EngineConsist(id = 'donegal',
              base_numeric_id = 1580,
              title = 'Donnegal [Diesel]',
              replacement_id = '-none',
              track_type = 'NG',
              power = 250,
              speed = 50,
              type_base_buy_cost_points = -5, # dibble buy cost for game balance
              intro_date = 1954,
              vehicle_life = 40,
              graphics_status = '',
              use_legacy_spritesheet = True)

consist.add_unit(DieselRailcar(consist = consist,
                        weight = 30,
                        vehicle_length = 8,
                        capacity_pax = 25,
                        capacity_mail = 12,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
