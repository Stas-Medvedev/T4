# TODO:
#       Write unit tests
#       Start running the code to debug:
#           - Player vs Player [DONE]
#           - Player vs Easy CPU
#           - Player vs Medium CPU
#           - Player vs Hard CPU

from game_manager import GameManager

def main() -> None:
   gm = GameManager()
   gm.run() 

if __name__ == '__main__':
   main()