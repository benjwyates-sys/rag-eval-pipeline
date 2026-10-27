# Simultaneous localization and mapping

Simultaneous localization and mapping (SLAM) is a problem in photogrammetry where a computer constructs or updates a map of an unknown environment while simultaneously keeping track of an entity's location within it. While this initially appears to be a chicken or the egg problem, there are several algorithms known to solve it in, at least approximately, tractable time for certain environments. Popular approximate solution methods include the particle filter, extended Kalman filter, covariance intersection, and GraphSLAM. SLAM algorithms are based on concepts in computational geometry and computer vision, and are used in robot navigation, robotic mapping and odometry for virtual reality or augmented reality.
SLAM algorithms are tailored to the available resources and are not aimed at perfection but at operational compliance. Published approaches are employed in self-driving cars, unmanned aerial vehicles, autonomous underwater vehicles, planetary rovers, newer domestic robots and even inside the human body.


== Mathematical description of the problem ==
Given a series of controls 
  
    
      
        
          u
          
            t
          
        
      
    
    {\displaystyle u_{t}}
  
 and sensor observations 
  
    
      
        
          o
          
            t
          
        
      
    
    {\displaystyle o_{t}}
  
 over discrete time steps 
  
    
      
        t
      
    
    {\displaystyle t}
  
, the SLAM problem is to compute an estimate of the agent's state 
  
    
      
        
          x
          
            t
          
        
      
    
    {\displaystyle x_{t}}
  
 and a map of the environment 
  
    
      
        
          m
          
            t
          
        
      
    
    {\displaystyle m_{t}}
  
. All quantities are usually probabilistic, so the objective is to compute

  
    
      
        P
        (
        
          m
          
            t
            +
            1
          
        
        ,
        
          x
          
            t
            +
            1
          
        
        
          |
        
        
          o
          
            1
            :
            t
            +
            1
          
        
        ,
        
          u
          
            1
            :
            t
          
        
        )
      
    
    {\displaystyle P(m_{t+1},x_{t+1}|o_{1:t+1},u_{1:t})}
  

Applying Bayes' rule gives a framework for sequentially updating the location posteriors, given a map and a transition function 
  
    
      
        P
        (
        
          x
          
            t
          
        
        
          |
        
        
          x
          
            t
            −
            1
          
        
        )
      
    
    {\displaystyle P(x_{t}|x_{t-1})}
  
,

  
    
      
        P
        (
        
          x
          
            t
          
        
        
          |
        
        
          o
          
            1
            :
            t
          
        
        ,
        
          u
          
            1
            :
            t
          
        
        ,
        
          m
          
            t
          
        
        )
        =
        
          ∑
          
            
              m
              
                t
                −
                1
              
            
          
        
        P
        (
        
          o
          
            t
          
        
        
          |
        
        
          x
          
            t
          
        
        ,
        
          m
          
            t
          
        
        ,
        
          u
          
            1
            :
            t
          
        
        )
        
          ∑
          
            
              x
              
                t
                −
                1
              
            
          
        
        P
        (
        
          x
          
            t
          
        
        
          |
        
        
          x
          
            t
            −
            1
          
        
        )
        P
        (
        
          x
          
            t
            −
            1
          
        
        
          |
        
        
          m
          
            t
          
        
        ,
        
          o
          
            1
            :
            t
            −
            1
          
        
        ,
        
          u
          
            1
            :
            t
          
        
        )
        
          /
        
        Z
      
    
    {\displaystyle P(x_{t}|o_{1:t},u_{1:t},m_{t})=\sum _{m_{t-1}}P(o_{t}|x_{t},m_{t},u_{1:t})\sum _{x_{t-1}}P(x_{t}|x_{t-1})P(x_{t-1}|m_{t},o_{1:t-1},u_{1:t})/Z}
  

where 
  
    
      
        Z
      
    
    {\displaystyle Z}
  
 is the normalization constant, which ensures all the probabilities sum up to 1.
Similarly the map can be updated sequentially by

  
    
      
        P
        (
        
          m
          
            t
          
        
        
          |
        
        
          x
          
            t
          
        
        ,
        
          o
          
            1
            :
            t
          
        
        ,
        
          u
          
            1
            :
            t
          
        
        )
        =
        
          ∑
          
            
              x
              
                t
              
            
          
        
        
          ∑
          
            
              m
              
                t
              
            
          
        
        P
        (
        
          m
          
            t
          
        
        
          |
        
        
          x
          
            t
          
    

---
Source: https://en.wikipedia.org/wiki/Simultaneous_localization_and_mapping (CC BY-SA 4.0)
