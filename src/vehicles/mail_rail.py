from train import MailEngineConsist, DieselEngineUnit

consist = MailEngineConsist(id='mail_rail',
                                 base_numeric_id=3000,
                                 title='Mail Rail [Diesel]',
                                 power=870,
                                 # matched to fast (in this gen) freight speeds
                                 speed=110,
                                 type_base_running_cost_points=-32,  # dibble running costs for game balance
                                 intro_date=2015)  # explicit intro date by design

consist.add_unit(type=DieselEngineUnit,
                 weight=37,
                 vehicle_length=8,
                 capacity=40,
                 spriterow_num=3)

consist.add_model_variant(spritesheet_suffix=0)
