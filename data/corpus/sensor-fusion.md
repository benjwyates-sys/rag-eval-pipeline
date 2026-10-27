# Sensor fusion

Sensor fusion is a process of combining sensor data or data derived from disparate sources so that the resulting information has less uncertainty than would be possible if these sources were used individually. For instance, one could potentially obtain a more accurate location estimate of an indoor object by combining multiple data sources such as video cameras and WiFi localization signals. The term uncertainty reduction in this case can mean more accurate, more complete, or more dependable, or refer to the result of an emerging view, such as stereoscopic vision (calculation of depth information by combining two-dimensional images from two cameras at slightly different viewpoints).
The data sources for a fusion process are not specified to originate from identical sensors. One can distinguish direct fusion, indirect fusion and fusion of the outputs of the former two. Direct fusion is the fusion of sensor data from a set of heterogeneous or homogeneous sensors, soft sensors, and history values of sensor data, while indirect fusion uses information sources like a priori knowledge about the environment and human input.
Sensor fusion is also known as (multi-sensor) data fusion and is a subset of information fusion.


== Examples of sensors ==
Accelerometers
Electronic Support Measures (ESM)
Flash LIDAR
Global Positioning System (GPS)
Infrared / thermal imaging camera
Magnetic sensors
MEMS
Phased array
Radar
Radiotelescopes, such as the proposed Square Kilometre Array, the largest sensor ever to be built
Scanning LIDAR
Seismic sensors
Sonar and other acoustic
Sonobuoys
TV cameras
→Additional List of sensors


== Algorithms ==
Sensor fusion is a term that covers a number of methods and algorithms, including:

Kalman filter
Bayesian networks
Dempster–Shafer
Convolutional neural network
Gaussian processes


== Example calculations ==
Two example sensor fusion calculations are illustrated below.
Let 
  
    
      
        
          
            x
          
          
            1
          
        
      
    
    {\displaystyle {x}_{1}}
  
 and 
  
    
      
        
          
            x
          
          
            2
          
        
      
    
    {\displaystyle {x}_{2}}
  
 denote two estimates from two independent sensor measurements, with noise variances 
  
    
      
        
          
            σ
            
              1
            
            
              2
            
          
        
      
    
    {\displaystyle \scriptstyle \sigma _{1}^{2}}
  
 and 
  
    
      
        
          
            σ
            
              2
            
            
              2
            
          
        
      
    
    {\displaystyle \scriptstyle \sigma _{2}^{2}}
  

, respectively. One way of obtaining a combined estimate 
  
    
      
        
          
            x
          
          
            3
          
        
      
    
    {\displaystyle {x}_{3}}
  
 is to apply inverse-variance weighting, which is also employed within the Fraser-Potter fixed-interval smoother, namely

  
    
      
        
          
            x
          
          
            3
          
        
        =
        
          σ
          
            3
          
          
            2
          
        
        (
        
          σ
          
            1
          
          
            −
            2
          
        
        
          
            x
          
          
            1
          
        
        +
        
          σ
          
            2
          
          
            −
            2
          
        
        
          
            x
          
          
            2
          
        
        )
      
    
    {\displaystyle {x}_{3}=\sigma _{3}^{2}(\sigma _{1}^{-2}{x}_{1}+\sigma _{2}^{-2}{x}_{2})}
  
 ,
where 
  
    
      
        
          
            σ
            
              3
            
            
              2
            
          
          =
          (
          
            
              σ
              
                1
              
              
                −
                2
              
            
            +
            
              
                σ
                
                  2
                
                
                  −
                  2
                
              
              
                )
                
                  −
                  1
                
              
            
          
        
      
    
    {\displaystyle \scriptstyle \sigma _{3}^{2}=(\scriptstyle \sigma _{1}^{-2}+\scriptstyle \sigma _{2}^{-2})^{-1}}
  
 is the variance of the combined estimate. It can be seen that the fused result is simply a linear combination of the two measurements weighted by their respective information. 
It is worth noting that if 
  
    
      
        
          x
        
      
    
    {\displaystyle {x}}
  
 is a random variable. The estimates 
  
    
      
        
          
            x
          
          
            1
          
        
      
    
    {\displaystyle {x}_{1}}
  
 and 
  
    
      
        
          
            x
          
          
            2
          
        
      
    
    {\displaystyle {x}_{2}}
  
 will be correlated through common process noise, which will cause the estimate 
  
    
      
        
          
            x
          
          
            3
          
        
      
    
    {\displaystyle {x}_{3}}
  
 to lose conservativeness.
Another (equivalent) method to fuse two measurements is to use the optimal Kalman filter. Suppose that the data is generated by a first-order system and let 
  
    
      
        
          
            
              P
            
          
          
            k
          
        
      
    
    {\displaystyle {\textbf {P}}_{k}}
  
 denote the solution of the filter's Riccati equation.

---
Source: https://en.wikipedia.org/wiki/Sensor_fusion (CC BY-SA 4.0)
