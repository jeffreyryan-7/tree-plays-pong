# tree-plays-pong

## TLDR

Neural networks are very good at playing pong. Can a shallow decision tree achieve similar levels of performance by extracting strategies form the neural net? 

### Abstract 

Despite the tremendous power of deep learning models, there is continued anxiety about their use because we don't understand what they are thinking. This project tests whether a simple neural network's performance can be nearly matched by a decision tree. To test this idea, I take an existing neural network which has been trained to win at the Atari game pong. I then developed an approach to extract a small list of decisions which achieve similarly high performance with a shallow decision tree, which I will call the stump. I also investigated the tradeoffs and weaknesses of using the stump compared to the original neural network. 

