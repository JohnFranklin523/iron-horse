from train import HopperCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    # no gen 1 hoppers in Pony eh
    # also just type A for gen 1

    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=2310,
                               gen=2,
                               subtype='A',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=1070,
                               gen=3,
                               subtype='A',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=2330,
                               gen=3,
                               subtype='B',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=2320,
                               gen=4,
                               subtype='A',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_gapped_16px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=1380,
                               gen=4,
                               subtype='B',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=1080,
                               gen=5,
                               subtype='A',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_sparse_16px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=1090,
                               gen=5,
                               subtype='B',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=2780,
                               gen=5,
                               subtype='C',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=3010,
                               gen=6,
                               subtype='B',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = HopperCarConsist(roster='pony',
                               base_numeric_id=3020,
                               gen=6,
                               subtype='C',
                               sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')
