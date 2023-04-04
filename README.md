# Bass Diffusion Model
The Bass diffusion model consists of a differential equation that describes the adoption of a new product in a population by considering how adopters and potential adopters of a product interact.

The agent class has the following attributes:
p: the coefficient of innovation, which reflects the tendency of an individual to adopt the product independently of influence from her peers. This might be due to the advertising efforts or simply naturally
q: the coefficient of imitation, which reflects the tendency of an individual to adopt the product owing to imitation of her friends or hearing about the product from them
m: the number of friends that an agent has


The simulate function has parameters:
t: the time in days at which to measure the number of people who have heard of the product
num_agents: the number of agents in the simulation
