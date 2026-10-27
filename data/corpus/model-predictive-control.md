# Model predictive control

Model predictive control (MPC) is an advanced method of process control that is used to control a process while satisfying a set of constraints.  Model predictive controllers rely on dynamic models of the process, most often linear empirical models obtained by system identification. The main advantage of MPC is the fact that it allows the current timeslot to be optimized, while keeping future timeslots in account. This is achieved by optimizing a finite time-horizon, but only implementing the current timeslot and then optimizing again, repeatedly, thus differing from a linear–quadratic regulator (LQR). Also MPC has the ability to anticipate future events and can take control actions accordingly. PID controllers do not have this predictive ability. MPC is nearly universally implemented as a digital control, although there is research into achieving faster response times with specially designed analog circuitry.
It has been in use in the process industries in chemical plants and oil refineries since the 1980s. In recent years it has also been used in power system balancing models and in power electronics.
Generalized predictive control (GPC) and dynamic matrix control (DMC) are classical examples of MPC.


== Overview ==

The models used in MPC are generally intended to represent the behavior of complex and simple dynamical systems. The additional complexity of the MPC control algorithm is not generally needed to provide adequate control of simple systems, which are often controlled well by generic PID controllers. Common dynamic characteristics that are difficult for PID controllers include large time delays and high-order dynamics.
MPC models predict the change in the dependent variables of the modeled system that will be caused by changes in the independent variables. In a chemical process, independent variables that can be adjusted by the controller are often either the setpoints of regulatory PID controllers (pressure, flow, temperature, etc.) or the final control element (valves, dampers, etc.). Independent variables that cannot be adjusted by the controller are used as disturbances. Dependent variables in these processes are other measurements that represent either control objectives or process constraints.
MPC uses the current plant measurements, the current dynamic state of the process, the MPC models, and the process variable targets and limits to calculate future changes in the dependent variables. These changes are calculated to hold the dependent variables close to target while honoring constraints on both independent and dependent variables. The MPC typically sends out only the first change in each independent variable to be implemented, and repeats the calculation when the next change is required.
While many real processes are not linear, they can often be considered to be approximately linear over a small operating range. Linear MPC approaches are used in the majority of applications with the feedback mechanism of the MPC compensating for prediction errors due to structural mismatch between the model and the process.  In model predictive controllers that consist only of linear models, the superposition principle of linear algebra enables the effect of changes in multiple independent variables to be added together to predict the response of the dependent variables.  This simplifies the control problem to a series of direct matrix algebra calculations that are fast and robust.
When linear models are not sufficiently accurate to represent the real process nonlinearities, several approaches can be used. In some cases, the process variables can be transformed before and/or after the linear MPC model to reduce the nonlinearity. The process can be controlled with nonlinear MPC that uses a nonlinear model directly in the control application.  The nonlinear model may be in the form of an empirical data fit (e.g. artificial neural networks) or a high-fidelity dynamic model based on fundamental mass and energy balances. The nonlinear model may be linearized to derive a Kalman filter or specify a model for linear MPC.


=== Theory behind MPC ===
 MPC is based on iterative, finite-horizon optimization of a plant model.  At time 
  
    
      
        t
      
    
    {\displaystyle t}
  
 the current plant state is sampled and a cost minimizing control strategy is computed (via a numerical minimization algorithm) for a relatively short time horizon in the future: 
  
    
      
        [
        t
        ,
        t
        +
        T
        ]
      
    
    {\displaystyle [t,t+T]}
  
.  Specifically, an online or on-the-fly calculation is used to explore state trajectories that emanate from the current state and find (via the solution of Euler–Lagrange equations) a cost-minimizing control strategy until time 
  
    
      
        t
        +
        T
      
    
    {\displaystyle t+T}
  
. Only the first step of the control strategy is implemented, then the plant state is sampled again and the calculations are repeated starting from the new current state, yielding a new control and new predicted state path. The prediction horizon keeps being shifted forward and for this reason MPC is also called receding horizon control.  Although this approach is not optimal, in practice it has given very good results.

---
Source: https://en.wikipedia.org/wiki/Model_predictive_control (CC BY-SA 4.0)
