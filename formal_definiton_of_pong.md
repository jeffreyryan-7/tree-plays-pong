# Formal Definition of Pong


### Components and rules

Pong is a two player game played in a rectangular space with three objects: two identical paddles--represented by vertical bars--and a ball--represented by a square of pixels. The paddles are locked into the leftmost and rightmost ends of the rectangle and can move up and down at any time. 

At the start of a round, the ball is shot from the center of the field. The ball always travels with constant speed and direction. The ball only changes direction when it collides with a wall of the arena--the upper and lower bounds--or with one of the players paddles. If the ball passes one of the horizontal borders of the arena, the player on the opposite side of the field earns a point. The next round starts in the same way, with the ball at the center of the field.

For the purposes of this study, games will be one point to win. This assumes that the win rate of rounds is perfectly correlated with winning the best of some n rounds. For playing against the atari's original simulated opponent, this assumption is reasonable. It may not hold when playing against a human player, who learns and changes strategy each round, but this will be set as out of scope for this project. 


### Minimum model

After a round has started, pong can be modeled with the following structure:

$$X_t \ \& \ D_t = X_{t+1}$$

Where $X_t$ contains all of data pertinent to the state of the game and $D_t$ describes the choices made by the players at time $t$. In pong, this relationship is deterministic and can be perfectly modeled !!!is this true for paddle strikes?!!!. They are defined as follows:

$$
X_t = 
\begin{bmatrix}
x_{P1,t} \\
y_{P1,t} \\
x_{P2,t} \\
y_{P2,t} \\
x_{B,t} \\
y_{B,t} \\
v_{x,t} \\
v_{y,t} \\
\end{bmatrix}
= 
\begin{bmatrix}
\text{paddle 1 $x$ position} \\
\text{paddle 1 $y$ position} \\
\text{paddle 2 $x$ position} \\
\text{paddle 2 $y$ position} \\
\text{ball $x$ position} \\
\text{ball $y$ position} \\
\text{ball $x$ velocity} \\
\text{ball $y$ velocity} \\
\end{bmatrix}
$$

$$ 
D_t =
\begin{bmatrix}
u_{P1,t} \\
d_{P1,t} \\
u_{P2,t} \\
d_{P2,t} \\
\end{bmatrix}
=
\begin{bmatrix}
\text{is player 1 pressing up?} \\
\text{is player 1 pressing down?} \\
\text{is player 2 pressing up?} \\
\text{is player 2 pressing down?} \\
\end{bmatrix}
$$

$$s.t. \ (u_{Pi,t} + d_{Pi,t} \leq 1)  \ \forall \ t \ \& \ \forall i \epsilon \{1, 2\} \ \ \text{i.e. paddles move in one direction at a time or stay still}$$

To complete the model, a few constants are needed:
$$
x_{max}\text{: the rightmost part of the field} \\
x_{min}=0\text{: the leftmost of the field} \\
y_{max}\text{: the top of the field} \\
y_{min}=0\text{: the bottom of the field} \\
v_{p}\text{: the distance traveled by a paddle in one frame when a direction is pressed} \\
h\text{: the height of a paddle (it's collision box with the ball)} \\
l\text{: the length of the size of the ball (the ball is a square)}
$$

From these definitions, we can intuit how the game works and how all the mechanics unfold in play. 
