import global_constants
from train import LivestockConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'pony',
                               base_numeric_id = 1010,
                               wagon_generation = 1,
                                                intro_date = 1860,
                               vehicle_life = 40,
                               use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 12,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'pony',
                               base_numeric_id = 1020,
                               wagon_generation = 2,
                                                intro_date = 1950,
                               vehicle_life = 40,
                               use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 35,
                            weight = 25,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'pony',
                               base_numeric_id = 1030,
                               wagon_generation = 1,
                                                intro_date = 1860,
                               vehicle_life = 40,
                               track_type = 'NG',
                               use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 12,
                            weight = 5,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    #--------------- llama ----------------------------------------------------------------------
    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'llama',
                               base_numeric_id = 1040,
                               wagon_generation = 1,
                                                intro_date = 1860,
                               vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            weight = 12,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'llama',
                               base_numeric_id = 1430,
                               wagon_generation = 2,
                                                intro_date = 1925,
                               vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 45,
                            weight = 20,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'llama',
                               base_numeric_id = 1050,
                               wagon_generation = 1,
                                                intro_date = 1860,
                               vehicle_life = 40,
                               track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 5,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'llama',
                               base_numeric_id = 1520,
                               wagon_generation = 2,
                                                intro_date = 1920,
                               vehicle_life = 40,
                               track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 35,
                            weight = 5,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    #--------------- antelope ----------------------------------------------------------------------
    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'antelope',
                               base_numeric_id = 1720,
                               wagon_generation = 1,
                                                intro_date = 1950,
                               vehicle_life = 40,
                               use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 45,
                            weight = 30,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = LivestockConsist(title = '[Livestock Car]',
                               roster = 'antelope',
                               base_numeric_id = 2150,
                               wagon_generation = 1,
                                                intro_date = 1860,
                               vehicle_life = 40,
                               track_type = 'NG',
                               use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            weight = 12,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)

