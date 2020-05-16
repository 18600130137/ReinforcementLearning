import   numpy  as  np
import   gym
env=gym.make('CartPole-v0')


env.reset()
random_episodes=0
MAX_EPISODES=100
reward_all_sum=0
reward_sum=0
while  random_episodes<MAX_EPISODES:
    env.render()
    observation,reward,done,_=env.step(np.random.randint(0,2))
    reward_sum+=reward
    if done:
        random_episodes+=1
        print('Reward for  this episode was:',reward_sum)
        reward_all_sum+=reward_sum
        reward_sum=0
        env.reset()
print('Reward all sum  is:',reward_all_sum,'  Reward  avgrage is:',reward_all_sum/MAX_EPISODES)
#time.sleep(10)
env.close()
#Reward all sum  is: 2136.0   Reward  avgrage is: 21.36