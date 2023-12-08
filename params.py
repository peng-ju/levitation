import argparse

def args_parser():
    parser = argparse.ArgumentParser(description='Levitation_Monte_Carlo_Simulation')
    parser.add_argument('--name', '-n',
                        default="default",
                        type=str,
                        help='experiment name, used for saving results')
    

    args = parser.parse_args()

    return args