from Animations import run
import sys

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='pygame')
import pygame

pygame.init()
clock=   pygame.time.Clock()
font =   pygame.font.Font(pygame.font.get_default_font(), 25)
fps = 30 # frames per sec
window = pygame.display.set_mode((800, 800))
screen = pygame.display.get_surface()

if __name__ == '__main__':
    """
        Argument from command line: `python main.py <input_file_path> <algorithm> <time_delay>(optional)`
        search_algorithm must be one of ['bfs', 'dfs', 'ucs', 'greedy', 'astar']
    """
    if (len(sys.argv)<3) or (len(sys.argv)>5):
        raise Exception("Wrong input!!!")
    input = str(sys.argv[1])
    al = str(sys.argv[2])
    if (len(sys.argv)==4):
        time_delay = int(sys.argv[4])
    else: time_delay=500
    run(input, al, time_delay)
    
