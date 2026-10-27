# Automotive safety integrity level

Automotive safety integrity level (ASIL) is a risk classification scheme defined by the ISO 26262 - Functional Safety for Road Vehicles standard. This is an adaptation of the safety integrity level (SIL) used in IEC 61508 for the automotive industry. This classification helps defining the safety requirements necessary to be in line with the ISO 26262 standard. The ASIL is established by performing a risk analysis of a potential hazard by looking at the severity, exposure and controllability of the vehicle operating scenario. The safety goal for that hazard in turn carries the ASIL requirements.
There are four ASILs identified by the standard: ASIL A, ASIL B, ASIL C, ASIL D. ASIL D dictates the highest integrity requirements on the product and ASIL A the lowest. Hazards that are identified as QM (see below) do not dictate any safety requirements.


== Hazard analysis and risk assessment ==
Because of the reference to SIL and because the ASIL incorporate 4 levels of hazard with a 5th non-hazardous level, it is common in descriptions of ASIL to compare its levels to the SIL levels and DO-178C design assurance levels, respectively.
The determination of ASIL is the result of hazard analysis and risk assessment. 
In the context of ISO 26262, a hazard is assessed based on the relative impact of hazardous effects related to a system, as adjusted for relative likelihoods of the hazard manifesting those effects.  That is, each hazard is assessed in terms of severity of possible injuries within the context of how much of the time a vehicle is exposed to the possibility of the hazard happening (refer ISO26262 definition of exposure) as well as the relative likelihood that a typical driver can act to prevent the injury (refer ISO26262 definitions of severity and controllability).
In short, ASIL refers both to risk and to risk-dependent requirements (standard minimal risk treatment for a given risk).  Whereas risk may be generally expressed as 

  
    
      
        
          Risk
        
        =
        (
        
          expected loss in case of the accident
        
        )
        ×
        (
        
          probability of the accident occurring
        
        )
      
    
    {\displaystyle {\text{Risk}}=({\text{expected loss in case of the accident}})\times ({\text{probability of the accident occurring}})}
  

or

  
    
      
        
          Risk
        
        =
        
          Severity
        
        ×
        (
        
          Exposure
        
        ×
        
          Likelihood
        
        )
      
    
    {\displaystyle {\text{Risk}}={\text{Severity}}\times ({\text{Exposure}}\times {\text{Likelihood}})}
  

ASIL may be similarly expressed as

  
    
      
        
          ASIL
        
        =
        
          Severity
        
        ×
        (
        
          Exposure
        
        ×
        
          Controllability
        
        )
      
    
    {\displaystyle {\text{ASIL}}={\text{Severity}}\times ({\text{Exposure}}\times {\text{Controllability}})}
  

illustrating the role of exposure and controllability in establishing relative probability, which is combined with severity to form an expression of risk.


== Levels ==
The ASIL range from ASIL D, representing the highest degree of automotive hazard and highest degree of rigor applied in the assurance the resultant safety requirements, to QM, representing application with no automotive hazards and, therefore, no safety requirements to manage under the ISO 26262 safety processes. The intervening levels are simply a range of intermediate degrees of hazard and degrees of assurance required.


=== ASIL D ===
ASIL D, an abbreviation of automotive safety integrity level D, refers to the highest classification of initial hazard (injury risk) defined within ISO 26262 and to that standard's most stringent level of safety measures to apply for avoiding an unreasonable residual risk.   In particular, ASIL D represents likely potential for severely life-threatening or fatal injury in the event of a malfunction and requires the highest level of assurance that the dependent safety goals are sufficient and have been achieved. An example of dangerous hazard that warrants the ASIL D level is loss of braking on all wheels.
ASIL D is noteworthy, not only because of the elevated risk it represents and the exceptional rigor required in development, but also because automotive electrical, electronic, and software suppliers make claims that their products have been certified or otherwise accredited to ASIL D, ease development to ASIL D, or are otherwise suitable to or supportive of development of items to ASIL D.  Any product able to comply with ASIL D requirements would also comply with any lower level.
ISO 26262 "highly recommends" the use of semi-formal modeling languages for ASIL D designs (Stateflow and SysML provide examples of such languages). Executable validation using either prototyping or simulation is mandatory.


=== ASIL C ===
Loss of braking for only the rear wheels is less dangerous, so this hazard is associated with ASIL C. Another example of a less critical function that warrants the ASIL C rating is cruise control.
The use of semi-formal modeling languages is highly recommended for ASIL C designs. Executable validation using either prototyping or simulation is mandatory.


=== ASIL B ===
ASIL B examples are headlights and brake lights.
Modeling of the ASIL B design can rely on an informal languages. This and other differences requirements make the cost difference between C and B to be the largest step across all the ASILs.


=== ASIL A ===
ASIL A is the lowest rating of the functional safety. A typical example are tail lights (non-braking).

---
Source: https://en.wikipedia.org/wiki/Automotive_safety_integrity_level (CC BY-SA 4.0)
