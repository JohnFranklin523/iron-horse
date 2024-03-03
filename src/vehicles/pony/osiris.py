from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="osiris",
        base_numeric_id=30570,
        name="Osiris",
        role="express",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 900,
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        # note that livery names are metadata only and can repeat for different spriterows
        #additional_liveries=["SWOOSH", "INDUSTRIAL_YELLOW"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=42,
        vehicle_length=6,
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    # https://en.wikipedia.org/wiki/Euskotren_TD2000_series
    # https://en.wikipedia.org/wiki/JR_Freight_Class_DF200#DF200-7000
    consist.description = """"""
    consist.foamer_facts = """"""

    return consist
