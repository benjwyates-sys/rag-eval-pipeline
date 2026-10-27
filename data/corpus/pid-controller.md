# PID controller

A proportional–integral–derivative (PID) controller, or three-term controller, is a feedback-based control loop mechanism commonly used to manage machines and processes that require continuous control and automatic adjustment. It is typically used in industrial control systems and various other applications where constant control through modulation is necessary without human intervention. The PID controller automatically compares the desired target value (setpoint or SP) with the actual value of the system (process variable or PV). The difference between these two values is called the error value, denoted as 
  
    
      
        e
        (
        t
        )
      
    
    {\displaystyle e(t)}
  
.
It then applies corrective actions automatically to bring the PV to the same value as the SP using three methods: The proportional (P) component responds to the current error value by producing an output that is directly proportional to the magnitude of the error. This provides immediate correction based on how far the system is from the desired setpoint. The integral (I) component, in turn, considers the cumulative sum of past errors to address any residual steady-state errors that persist over time, eliminating lingering discrepancies. Lastly, the derivative (D) component predicts future error trend by assessing the rate of change of the error, which helps to mitigate overshoot and enhance system stability, particularly when the system undergoes rapid changes. The PID output signal can directly control actuators through voltage, current, or other modulation methods, depending on the application. The PID controller reduces the likelihood of human error and improves automation.
A common example is a vehicle's cruise control system. For instance, when a vehicle encounters a hill, its speed will decrease if the engine power output is kept constant. The PID controller adjusts the engine's power output to restore the vehicle to its desired speed, doing so efficiently with minimal delay and overshoot.
The theoretical foundation of PID controllers dates back to the early 1920s with the development of automatic steering systems for ships. This concept was later adopted for automatic process control in manufacturing, first appearing in pneumatic actuators and evolving into electronic controllers. PID controllers are widely used in numerous applications requiring accurate, stable, and optimized automatic control, such as temperature regulation, motor speed control, and industrial process management.


== Fundamental operation ==

The most distinguishing feature of the PID controller is the ability to use the three control terms of proportional, integral and derivative influence on the controller output to apply accurate and optimal control. The block diagram on the right shows the principles of how these terms are generated and applied. It shows a PID controller, which continuously calculates an error value 
  
    
      
        e
        (
        t
        )
      
    
    {\displaystyle e(t)}
  
 as the difference between a desired setpoint 
  
    
      
        
          SP
        
        =
        r
        (
        t
        )
      
    
    {\displaystyle {\text{SP}}=r(t)}
  
 and a measured process variable 
  
    
      
        
          PV
        
        =
        y
        (
        t
        )
      
    
    {\displaystyle {\text{PV}}=y(t)}
  
: 
  
    
      
        e
        (
        t
        )
        =
        r
        (
        t
        )
        −
        y
        (
        t
        )
      
    
    {\displaystyle e(t)=r(t)-y(t)}
  
, and applies a correction based on proportional, integral, and derivative terms. The controller attempts to minimize the error over time by adjustment of a control variable 
  
    
      
        u
        (
        t
        )
      
    
    {\displaystyle u(t)}
  
, such as the opening of a control valve, to a new value determined by a weighted sum of the control terms.
The PID controller directly generates a continuous control signal based on error, without discrete modulation.
In this model:

Term P is proportional to the current value of the SP−PV error 
  
    
      
        e
        (
        t
        )
      
    
    {\displaystyle e(t)}
  
. For example, if the error is large, the control output will be proportionately large by using the gain factor "Kp". Using proportional control alone will result in an error between the set point and the process value because the controller requires an error to generate the proportional output response. In steady-state process conditions, an equilibrium is reached, with a steady SP−PV "offset".
Term I integrates past values of the SP−PV error. For example, if there is a residual error after the application of proportional control, the integral term seeks to eliminate the residual error by adding a control effect due to the historic cumulative value of the error. When the error is eliminated, the integral term will cease to grow. This will result in the proportional effect diminishing as the error decreases, but this is compensated for by the growing integral effect.
Term D is a best estimate of the future trend of the SP−PV error, based on its current rate of change. It is sometimes called "anticipatory control", as it is effectively seeking to reduce the effect of the SP−PV error by exerting a control influence generated by the rate of error change. The more rapid the change, the greater the controlling or damping effect.
Tuning – The balance of these effects is achieved by loop tuning to produce the optimal control function. The tuning constants are shown below as "K" and must be derived for each control application, as they depend on the response characteristics of the physical system, external to the controller.

---
Source: https://en.wikipedia.org/wiki/PID_controller (CC BY-SA 4.0)
