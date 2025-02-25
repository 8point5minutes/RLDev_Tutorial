import tcod

from engine import Engine
from input_handlers import EventHandler
from entity import Entity
from game_map import GameMap
from procgen import generate_dungeon

def main() -> None:
    #screen parameters
    screen_width = 80
    screen_height = 50
    #map paramenters
    map_width = 80
    map_height = 45
    #room parameters
    room_max_size = 12
    room_min_size = 5
    max_rooms = 100
    #player info
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    #loading tileset
    tileset = tcod.tileset.load_tilesheet(
        "image.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 0, 0))
    entities = {npc, player}
    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        player=player
    )

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)
    
    #new terminal parameters
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Eminences of Kybernabad",
        vsync=True,
    ) as context:
        #creating console; F swaps x and y so it's [x, y]
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        #game loop!
        while True:
            #print it to the console
            engine.render(console=root_console, context=context)
            events = tcod.event.wait()
            engine.handle_events(events)

if __name__ == "__main__":
    main()