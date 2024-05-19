# Probability Calculator solution for freeCodeCamp Scientific Computing with Python certification

import random
import copy

class Hat:
    def __init__(self, **kwargs):
        ball_list = []
        for key, value in kwargs.items():
            for _ in range(value):
                ball_list.append(key)

        self.contents = ball_list

    def draw(self, n):
        draw_list = []
        if n > len(self.contents):
            return self.contents
        else:
            for _ in range(n):
                random_index = random.randint(0, len(self.contents) - 1)
                draw_list.append(self.contents[random_index])
                self.contents.pop(random_index)
        return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    temporary_hat = Hat()
    hat_cont = hat.contents
    n = 0
    for _ in range(num_experiments):
        temporary_hat.contents = copy.deepcopy(hat_cont)
        drawing = temporary_hat.draw(num_balls_drawn) # return list
        results = []
        for key, value in expected_balls.items():
            if value <= drawing.count(key):
                results.append(True)
            else:
                results.append(False)
        if all(results):
            n += 1
    return n / num_experiments
