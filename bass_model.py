import random

class Agent:
    def __init__(self, p, q, m, population):
        self.p = p	# coefficient of innovation
        self.q = q	# coefficient of imitation
        self.m = m
        self.friends = random.sample(population, k=random.randint(1, len(population)-1))
        self.heard = False if random.random() < 0.5 else True
        
    def hear(self, t):
        if not self.heard:
            cumulative_bass = 0
            for friend in self.friends:
                if friend.heard:
                   cumulative_bass += friend.p + (friend.q * 1 / friend.m)
            bass = cumulative_bass / self.m
            prob = 1-(1-bass)**t
            self.heard = random.random() < prob	   # if the probability of having adopted the product is overwhelming, then self.heard = True
        return self.heard


def simulate(num_agents, p, q, m, t):
    population = [Agent(p, q, m, list(range(num_agents))) for i in range(num_agents)]
    for i, agent in enumerate(population):
        agent.friends = random.sample(population[:i]+population[i+1:], k=random.randint(1, len(population)-1)) # the list (array) is being repopulated by the same number of friends
    heard_count = 0
    for agent in population:
        if agent.hear(t):
            heard_count += 1
    return heard_count
    
    
if __name__ == "__main__":
    print(simulate(1000, 0.03, 0.38, 50, 5))
