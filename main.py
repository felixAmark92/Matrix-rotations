# Example file showing a circle moving on screen
import pygame
import math
# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
dt = 0
angle: float = 0

def matmul(a:list[list[int]], b:list[list[int]]):

    colsA = len(a[0])
    rowsA = len(a)
    colsB = len(b[0])
    rowsB = len(b)

    if colsA  != rowsB:
        print("matrix multiplication not viable!")
        return None

    result = []

    for i in range(rowsA):
        row = []
        for j in range(colsB):
            sum = 0
            for k in range(colsA):
                sum += a[i][k] * b[k][j]
            row.append(sum)
        result.append(row)

    return result

# points = [
#     [[-100], [-100], [100]],
#     [[-100], [100], [100]],
#     [[100], [100], [100]],
#     [[100], [-100], [100]],
#     [[-100], [-100], [-100]],
#     [[-100], [100], [-100]],
#     [[100], [100], [-100]],
#     [[100], [-100], [-100]]]


points = [
    [[-0], [-200], [0]],
    [[-100], [0], [100]],
    [[100], [0], [100]],
    [[100], [0], [-100]],
    [[-100], [0], [-100]],
    [[0], [200], [0]]]






while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#4287f5")
   
    rotationZ = [
    [math.cos(angle),-math.sin(angle), 0],
    [math.sin(angle), math.cos(angle), 0],
    [0, 0, 1]
    ]

    rotationX = [
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ]

    rotationY = [
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]
    ]

    temp_points = []

 
    for point in points:


        rotated = matmul(rotationX, point)
        rotated = matmul(rotationY, rotated)
        rotated = matmul(rotationZ, rotated)

        dist = 1200

        z = 1000 / (dist - rotated[2][0])


        projection = [
            [z, 0, 0],
            [0, z, 0]

        ]

        projected2d = matmul(projection, rotated)
        temp_points.append((projected2d[0][0] + 300, projected2d[1][0] + 300))
        # pygame.draw.circle(screen, "white", (projected2d[0][0] + 300, projected2d[1][0] + 300), 5)
    
    # for i in range(4):
    #     pygame.draw.line(screen, "white", temp_points[i], temp_points[(i + 1) % 4] )
    #     pygame.draw.line(screen, "white", temp_points[i + 4], (temp_points[((i + 1) % 4) + 4]))
    #     pygame.draw.line(screen, "white", temp_points[i], temp_points[i + 4])

    for i in range(4):
        pygame.draw.line(screen, "white", temp_points[0], temp_points[i + 1] )
        pygame.draw.line(screen, "white", temp_points[5], temp_points[i + 1] )
        pygame.draw.line(screen, "white", temp_points[i + 1], (temp_points[i + 2]))

    pygame.draw.line(screen, "white", temp_points[1], temp_points[4])


    angle += 1 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()