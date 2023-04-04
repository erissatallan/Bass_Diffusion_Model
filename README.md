# Bass Diffusion Model
The Bass diffusion model consists of a differential equation that describes the adoption of a new product in a population by considering how adopters and potential adopters of a product interact.

The agent class has the following attributes:
p: the coefficient of innovation, which reflects the tendency of an individual to adopt the product independently of influence from her peers. This might be due to the advertising efforts or simply naturally
q: the coefficient of imitation, which reflects the tendency of an individual to adopt the product owing to imitation of her friends or hearing about the product from them
m: the number of friends that an agent has

Line `cumulative_bass += friend.p + (friend.q * 1 / friend.m)` calculates the cumulative bass coefficient for a given individual. The Bass coefficient is a mathematical parameter used in the model to capture the effect of social influence on the adoption of a new product or idea. `friend.q * 1 / friend.m` reflects the idea that individuals are less likely to be influenced by a large number of acquaintances than by a smaller, more intimate group
of friends. By adding up the Bass coefficients of all friends of the current individual, the cumulative_bass variable keeps track of the overall influence of social connections on the current individual's decision to adopt the new product. The resulting value is then used in the formula to calculate the probability of the current agent hearing about the product.

The line `prob = 1-(1-bass)**t` calculates the probability that the current agent will hear about the product at a given time $t$.
The `bass` variable represents the overall influence of social connections on the current individuals's decision to adopt the new product, calculated as the cumulative Bass coefficient for the agent's friends. If it equals 1, then everyone has been influenced enough to adopt the product.
`(1 - bass)` represents the proportion of the population that has not yet adopted the new product.
`(1 - bass) ** t` represents the probability that an individual in the population has not yet adopted the new product after t time steps. It is reasonable to use because it exponentially decays the number of non-adopters with time, as observed in the real world.
`1 - (1 - bass) ** t` represents the probability that an individual in the population has adopted the new product after t time steps.
Therefore, `prob` represents the probability that the current individual will hear about the product at a given time t. This resulting probability is used to determine whether the agent adopts the product or not.


The simulate function has parameters:
t: the time in days at which to measure the number of people who have heard of the product
num_agents: the number of agents in the simulation
