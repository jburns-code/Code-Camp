import copy
import random

class Hat:

    def __init__(self, **kwargs):
        self.hats = dict(kwargs)
        self.contents = []

        for item in self.hats:
            count = 0
            while count < self.hats[item]:
                self.contents.append(item)
                count += 1


    def draw(self,num_to_draw):
        """
        Removes a numbet of random items from self.contents, based on the argument passed in
        """
        balls_removed = []
        if num_to_draw > len(self.contents):
            return self.contents
        else:
            for n in range(num_to_draw):
                balls_removed.append(self.contents.pop(random.randrange(len(self.contents))))
        return balls_removed
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Returns the probability of expected_balls to match the items in Hat, 
    based on an amount of experiments conducted.
    """
    success_counter = 0
    for n in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        drawn_balls = temp_hat.draw(num_balls_drawn)
        success_bool = True
        for key,value in expected_balls.items():
            if drawn_balls.count(key) < value:
                success_bool = False
                break
            else: 
                success_bool = True

        if success_bool:
            success_counter += 1
            
    return (success_counter / num_experiments)