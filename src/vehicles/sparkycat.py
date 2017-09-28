import global_constants
from train import EngineConsist, ElectroDieselLoco

consist = EngineConsist(id = 'sparkycat',
              base_numeric_id = 160,
              title = 'SparkyCat [ElectroDiesel]',
              power = 1700,
              speed = 110,
              type_base_buy_cost_points = 60, # dibble buy cost for game balance
              vehicle_life = 40,
              intro_date = 2020,
              power_by_railtype = {'RAIL': 1850, 'ELRL': 3700})

consist.add_unit(ElectroDieselLoco(consist = consist,
                        weight = 120,
                        vehicle_length = 8,
                        spriterow_num = 0))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
