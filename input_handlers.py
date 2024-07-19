from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction

#subclass of EventDispatch
class EventHandler(tcod.event.EventDispatch[Action]):
    #quite when we click X in the corner
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    #keypress setup
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        #use the keyboard for schmovement
        if key == tcod.event.KeySym.UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.KeySym.DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.KeySym.LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.KeySym.RIGHT:
            action = MovementAction(dx=1, dy=0)
        
        #press esc to quit
        elif key == tcod.event.KeySym.ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action