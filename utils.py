import gymnasium as gym
import numpy as np

class Pong6InputWrapper(gym.Wrapper):
    def __init__(self, env):
        super().__init__(env)
        # 6 inputs: [P1_y, P2_y, Ball_x, Ball_y, V_x, V_y]
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(6,), dtype=np.float32)
        self.prev_ball_pos = None

    def observation(self, obs):
        # NORMALIZE: Divide by 255 to keep values between 0.0 and 1.0
        p1_y, p2_y = obs[51]/255.0, obs[50]/255.0
        b_x, b_y   = obs[49]/255.0, obs[54]/255.0

        if self.prev_ball_pos is None:
            v_x, v_y = 0.5, 0.5 # Neutral start
        else:
            # Velocity is also scaled
            v_x = (b_x - self.prev_ball_pos[0]) + 0.5
            v_y = (b_y - self.prev_ball_pos[1]) + 0.5
            if abs(v_x - 0.5) > 0.1 or abs(v_y - 0.5) > 0.1:
                v_x, v_y = 0.5, 0.5

        self.prev_ball_pos = (b_x, b_y)
        return np.array([p1_y, p2_y, b_x, b_y, v_x, v_y], dtype=np.float32)

    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)
        
        # REWARD SHAPING: Give +0.1 for hitting the ball
        # In Pong RAM, a specific flag at index 12 or 13 usually flips on contact
        # Or more simply: if the reward is 0 but the ball's V_x just flipped directions 
        # while near the paddle, it's a hit!
        if reward == 0 and self.prev_ball_pos is not None:
             # If ball was far right and now moving left (Simplified hit detection)
             if obs[49] > 180 and (obs[49] - self.prev_ball_pos[0]*255) < 0:
                 reward += 0.1 

        return self.observation(obs), reward, terminated, truncated, info

    def reset(self, **kwargs):
        self.prev_ball_pos = None
        obs, info = self.env.reset(**kwargs)
        return self.observation(obs), info