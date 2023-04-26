import numpy as np
from pathlib import Path

EXPECTED_FILE_NAMES = ['walls', 'terrain']
CSV_SUFFIX = '.csv'
CSV_DIR = 'csvs'

MUD, DIRT, STONE, BEDROCK = [0, 1, 2, 3]

def unstable_walls(walls: np.ndarray, terrain: np.ndarray, threshold: int = MUD) -> int:

    #------------------------------------------ YOUR CODE GOES HERE ------------------------------------------

    return -1
    #---------------------------------------------------------------------------------------------------------

def validate_env(csv_dir: Path):
    
    if (not csv_dir.exists()):
        raise('eps or jpg dir does not exist')
    for expected_file in EXPECTED_FILE_NAMES:
        expected_file_path = csv_dir / (expected_file + CSV_SUFFIX)
        if (not expected_file_path.exists()):
            raise(f'{expected_file_path} does not exist')

def main():

    parent_dir = Path(__file__).parent.resolve()
    csv_dir = parent_dir / CSV_DIR
    validate_env(csv_dir)

    WALLS = np.loadtxt(CSV_DIR / Path('walls.csv'), delimiter=',').astype(np.int8)
    TERRAIN = np.loadtxt(CSV_DIR / Path('terrain.csv'), delimiter=',').astype(np.int8)

    print(unstable_walls(WALLS, TERRAIN, threshold=DIRT))

if __name__ == '__main__':
    main()