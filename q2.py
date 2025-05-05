import numpy as np
from pathlib import Path

EXPECTED_FILE_NAMES = ['walls', 'terrain']
CSV_SUFFIX = '.csv'
CSV_DIR = 'csvs'

EMPTY, DRYWALL, WOOD, STONE = [0, 1, 2, 3]
MUD, DIRT, STONE, BEDROCK = [0, 1, 2, 3]

LEAK_ORIGIN = (6, 5)

def unstable_walls(walls: np.ndarray, terrain: np.ndarray, threshold: int = MUD) -> int:

    #------------------------------------------ YOUR CODE GOES HERE ------------------------------------------
    # Question 2a
    wall_mask = (walls != EMPTY) 
    soft_wall = (terrain <= threshold)
    reinforce_walls = np.count_nonzero(wall_mask & soft_wall)
    return reinforce_walls
    #---------------------------------------------------------------------------------------------------------

def leak_territory(walls: np.ndarray, leak_origin: tuple[int] = LEAK_ORIGIN) -> int:

    #------------------------------------------ YOUR CODE GOES HERE ------------------------------------------
    # Question 2b
    wall_mask = (walls != EMPTY) # boolean array for empty walls

    flooded = np.zeros_like(wall_mask, bool)
    flooded[LEAK_ORIGIN] = True

    while True:
        up      = np.roll(flooded, 1, axis=0)
        down    = np.roll(flooded, -1, axis=0)
        right   = np.roll(flooded, 1, axis=1)
        left    = np.roll(flooded, -1, axis=1)
        neighbors = (up | down | right | left) # possible neighbors

        new_spill = neighbors & (~wall_mask) & (~flooded) # spill in places where there is no wall
        if not new_spill.any():
            break
        flooded |= new_spill

    surface_area = flooded.sum()
    return surface_area

    #---------------------------------------------------------------------------------------------------------

def validate_env(csv_dir: Path):
    
    if (not csv_dir.exists()):
        raise('csv dir does not exist')
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

    # Q2a result printed here
    print('unstable_walls:', unstable_walls(np.copy(WALLS), np.copy(TERRAIN), threshold=DIRT))

    # Q2b result printed here
    print('leak_territory:', leak_territory(np.copy(WALLS), leak_origin=LEAK_ORIGIN))

if __name__ == '__main__':
    main()
