class GameState:
    def __init__(self, state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume
        self.handle_events = state.handle_events
        self.update = state.update
        self.draw = state.draw



class TestGameState:

    def __init__(self, name):
        self.name = name

    def enter(self):
        print("State [%s] Entered" % self.name)

    def exit(self):
        print("State [%s] Exited" % self.name)

    def pause(self):
        print("State [%s] Paused" % self.name)

    def resume(self):
        print("State [%s] Resumed" % self.name)

    def handle_events(self):
        print("State [%s] handle_events" % self.name)

    def update(self):
        print("State [%s] update" % self.name)

    def draw(self):
        print("State [%s] draw" % self.name)



running = None
stack = None


def change_state(state):
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].exit()
        # remove the current state
        stack.pop()
    stack.append(state)
    state.enter()



def push_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(state)
    state.enter()



def pop_state():
    global stack
    if (len(stack) > 0):
        stack[-1].exit()
        stack.pop()
    if (len(stack) > 0):
        stack[-1].resume()


def quit():
    global running
    running = False


def run(First_screen):
    global running, stack
    running = True
    stack = [First_screen]
    First_screen.enter()

    while (running):
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
    while (len(stack) > 0):
        stack[-1].exit()
        stack.pop()


def test_game_framework():
    First_screen = TestGameState("FirstState")
    run(First_screen)

if __name__ == '__main__':
    test_game_framework()