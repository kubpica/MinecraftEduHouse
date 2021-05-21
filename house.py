agent.teleport()
agent.move("forward")
agent.give("stone brick", 64, 1)
agent.give("wood", 64, 2)
agent.move("up")
x = 8
for count in range(x):
    for count2 in range(4):
        for count3 in range(x):
            agent.place(1, "down")
            agent.move("forward")
        agent.turn("left")
    agent.move("up")
agent.move("back")
agent.move("right")
x = x + 2
while x > 0:
    for count in range(4):
        for count2 in range(x):
            agent.place(2, "down")
            agent.move("forward")
        agent.turn("left")
    x = x - 2
    agent.move("up")
    agent.move("forward")
    agent.move("left")
if x == 0:
    agent.place(2, "down")
        