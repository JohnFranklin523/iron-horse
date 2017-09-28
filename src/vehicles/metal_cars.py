import global_constants
from train import MetalConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = MetalConsist(title = '[Metal Car]',
                           roster = 'pony',
                           base_numeric_id = 890,
                           wagon_generation = 1,
                           vehicle_life = 50,
                           suppress_animated_pixel_warnings = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 30,
                            vehicle_length = 5,
                            spriterow_num = 0))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    consist = MetalConsist(title = '[Metal Car]',
                           roster = 'pony',
                           base_numeric_id = 900,
                           wagon_generation = 2,
                           vehicle_life = 50,
                           suppress_animated_pixel_warnings = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 60,
                            vehicle_length = 8,
                            spriterow_num = 0))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)


    consist = MetalConsist(title = '[Metal Car]',
                           roster = 'pony',
                           base_numeric_id = 910,
                           wagon_generation = 3,
                           vehicle_life = 50,
                           suppress_animated_pixel_warnings = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 90,
                            vehicle_length = 8,
                            spriterow_num = 0))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date)
