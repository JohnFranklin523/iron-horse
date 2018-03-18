from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='v8',
                        base_numeric_id=410,
                        title='V8 2-C+C-2 [Electric]',
                        power=4000,
                        speed=85,
                        type_base_buy_cost_points=35,  # dibble buy cost for game balance
                        type_base_running_cost_points=-10,  # dibble running costs for game balance
                        intro_date=1949)

consist.add_unit(type=ElectricEngineUnit,
                 weight=160,
                 vehicle_length=8,
                 spriterow_num=0)

