from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='defiant',
                            base_numeric_id=5070,
                            name='Defiant',
                            role='heavy_freight',
                            role_child_branch_num=-1,
                            power=3650,
                            # dibble for game balance, assume super-slip control
                            tractive_effort_coefficient=0.355,
                            random_reverse=True,
                            gen=6,
                            intro_date_offset=-4,  # let's be a little bit earlier for this one
                            fixed_run_cost_points=280, # run cost nerf as light weight throws the cost too cheap
                            default_livery_extra_docs_examples=[('COLOUR_MAUVE', 'COLOUR_CREAM')],
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=100, # notably low weight
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """"""
    consist.foamer_facts = """"""

    return consist