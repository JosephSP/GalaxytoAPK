from kivy.uix.relativelayout import RelativeLayout



# Keyboard interaction
def keyboard_closed(self):
    self._keyboard.unbind(on_key_down = self.on_keyboard_down)
    self._keyboard.unbind(on_key_up = self.on_keyboard_up)
    self._keyboard = None

def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == "a":
            self.mov_direction = 1
        elif keycode[1] == "d":
            self.mov_direction = -1
        return True
    
def on_keyboard_up(self, keyboard, keycode):
    self.mov_direction = 0

# mobile interactions:

def on_touch_down(self, touch):
    if not self.state_game_over and self.state_game_has_started:
        if touch.x < self.width/2:
            self.mov_direction = 1
            # <-
            
        else:
            self.mov_direction = -1
            # ->
    return super(RelativeLayout, self).on_touch_down(touch)
        
def on_touch_up(self, touch):
    self.mov_direction = 0
    