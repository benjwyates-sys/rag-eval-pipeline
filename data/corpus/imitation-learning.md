# Imitation learning

Imitation learning is a paradigm in reinforcement learning, where an agent learns to perform a task by supervised learning from expert demonstrations . It is also called learning from demonstration and apprenticeship learning.
It has been applied to underactuated robotics, self-driving cars, quadcopter navigation, helicopter aerobatics, and locomotion.


== Approaches ==
Expert demonstrations are recordings of an expert performing the desired task, often collected as state-action pairs 
  
    
      
        (
        
          o
          
            t
          
          
            ∗
          
        
        ,
        
          a
          
            t
          
          
            ∗
          
        
        )
      
    
    {\displaystyle (o_{t}^{*},a_{t}^{*})}
  
.


=== Behavior Cloning ===
Behavior Cloning (BC) is the most basic form of imitation learning. Essentially, it uses supervised learning to train a policy 
  
    
      
        
          π
          
            θ
          
        
      
    
    {\displaystyle \pi _{\theta }}
  
 such that, given an observation 
  
    
      
        
          o
          
            t
          
        
      
    
    {\displaystyle o_{t}}
  
, it would output an action distribution 
  
    
      
        
          π
          
            θ
          
        
        (
        ⋅
        
          |
        
        
          o
          
            t
          
        
        )
      
    
    {\displaystyle \pi _{\theta }(\cdot |o_{t})}
  
 that is approximately the same as the action distribution of the experts.
BC is susceptible to distribution shift. Specifically, if the trained policy differs from the expert policy, it might find itself straying from expert trajectory into observations that would have never occurred in expert trajectories.
This was already noted by ALVINN, where they trained a neural network to drive a van using human demonstrations. They noticed that because a human driver never strays far from the path, the network would never be trained on what action to take if it ever finds itself straying far from the path.


=== DAgger ===
DAgger (Dataset Aggregation) improves on behavior cloning by iteratively training on a dataset of expert demonstrations. In each iteration, the algorithm first collects data by rolling out the learned policy 
  
    
      
        
          π
          
            θ
          
        
      
    
    {\displaystyle \pi _{\theta }}
  
. Then, it queries the expert for the optimal action 
  
    
      
        
          a
          
            t
          
          
            ∗
          
        
      
    
    {\displaystyle a_{t}^{*}}
  
 on each observation 
  
    
      
        
          o
          
            t
          
        
      
    
    {\displaystyle o_{t}}
  
 encountered during the rollout. Finally, it aggregates the new data into the dataset
  
    
      
        D
        ←
        D
        ∪
        {
        (
        
          o
          
            1
          
        
        ,
        
          a
          
            1
          
          
            ∗
          
        
        )
        ,
        (
        
          o
          
            2
          
        
        ,
        
          a
          
            2
          
          
            ∗
          
        
        )
        ,
        .
        .
        .
        ,
        (
        
          o
          
            T
          
        
        ,
        
          a
          
            T
          
          
            ∗
          
        
        )
        }
      
    
    {\displaystyle D\leftarrow D\cup \{(o_{1},a_{1}^{*}),(o_{2},a_{2}^{*}),...,(o_{T},a_{T}^{*})\}}
  
and trains a new policy on the aggregated dataset.


=== Decision transformer ===

The Decision Transformer approach models reinforcement learning as a sequence modelling problem. Similar to Behavior Cloning, it trains a sequence model, such as a Transformer, that models rollout sequences 
  
    
      
        (
        
          R
          
            1
          
        
        ,
        
          o
          
            1
          
        
        ,
        
          a
          
            1
          
        
        )
        ,
        (
        
          R
          
            2
          
        
        ,
        
          o
          
            2
          
        
        ,
        
          a
          
            2
          
        
        )
        ,
        …
        ,
        (
        
          R
          
            t
          
        
        ,
        
          o
          
            t
          
        
        ,
        
          a
          
            t
          
        
        )
        ,
      
    
    {\displaystyle (R_{1},o_{1},a_{1}),(R_{2},o_{2},a_{2}),\dots ,(R_{t},o_{t},a_{t}),}
  
where 
  
    
      
        
          R
          
            t
          
        
        =
        
          r
          
            t
          
        
        +
        
          r
          
            t
            +
            1
          
        
        +
        ⋯
        +
        
          r
          
            T
          
        
      
    
    {\displaystyle R_{t}=r_{t}+r_{t+1}+\dots +r_{T}}
  
 is the sum of future reward in the rollout.

---
Source: https://en.wikipedia.org/wiki/Imitation_learning (CC BY-SA 4.0)
