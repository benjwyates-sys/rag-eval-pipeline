# Precision and recall

In classification, precision and recall are performance metrics that apply to data retrieved from a collection, corpus or sample space.
Precision (also called positive predictive value) is the fraction of relevant instances among the retrieved instances. Written as a formula:

  
    
      
        
          Precision
        
        =
        
          
            Relevant retrieved instances
            
              
                All 
              
              
                
                  retrieved
                
              
              
                 instances
              
            
          
        
      
    
    {\displaystyle {\text{Precision}}={\frac {\text{Relevant retrieved instances}}{{\text{All }}{\textbf {retrieved}}{\text{ instances}}}}}
  

Recall (also known as sensitivity) is the fraction of relevant instances that were retrieved. Written as a formula:

  
    
      
        
          Recall
        
        =
        
          
            Relevant retrieved instances
            
              
                All 
              
              
                
                  relevant
                
              
              
                 instances
              
            
          
        
      
    
    {\displaystyle {\text{Recall}}={\frac {\text{Relevant retrieved instances}}{{\text{All }}{\textbf {relevant}}{\text{ instances}}}}}
  

Both precision and recall are therefore based on relevance. 
Consider a computer program for recognizing dogs (the relevant element) in a digital photograph. Upon processing a picture which contains ten cats and twelve dogs, the program identifies eight dogs. Of the eight elements identified as dogs, only five actually are dogs (true positives), while the other three are cats (false positives). Seven dogs were missed (false negatives), and seven cats were correctly excluded (true negatives). The program's precision is then 5/8 (true positives / selected elements) while its recall is 5/12 (true positives / relevant elements).
Adopting a hypothesis-testing approach, where in this case, the null hypothesis is that a given item is irrelevant (not a dog), absence of type I and type II errors (perfect specificity and sensitivity) corresponds respectively to perfect precision (no false positives) and perfect recall (no false negatives).  
More generally, recall is simply the complement of the type II error rate (i.e., one minus the type II error rate). Precision is related to the type I error rate, but in a slightly more complicated way, as it also depends upon the prior distribution of seeing a relevant vs. an irrelevant item.
The above cat and dog example contained 8 − 5 = 3 type I errors (false positives) out of 10 total cats (true negatives), for a type I error rate of 3/10, and 12 − 5 = 7 type II errors (false negatives), for a type II error rate of 7/12.  Precision can be seen as a measure of quality, and recall as a measure of quantity. 
Higher precision means that an algorithm returns more relevant results than irrelevant ones, and high recall means that an algorithm returns most of the relevant results (whether or not irrelevant ones are also returned).


== Introduction ==

In a classification task, the precision for a class is the number of true positives (i.e. the number of items correctly labelled as belonging to the positive class) divided by the total number of elements labelled as belonging to the positive class (i.e. the sum of true positives and false positives, which are items incorrectly labelled as belonging to the class). Recall in this context is defined as the number of true positives divided by the total number of elements that actually belong to the positive class (i.e. the sum of true positives and false negatives, which are items which were not labelled as belonging to the positive class but should have been).
Precision and recall are not particularly useful metrics when used in isolation. For instance, it is possible to have perfect recall by simply retrieving every single item. Likewise, it is possible to achieve perfect precision by selecting only a very small number of extremely likely items.
In a classification task, a precision score of 1.0 for a class C means that every item labelled as belonging to class C does indeed belong to class C (but says nothing about the number of items from class C that were not labelled correctly) whereas a recall of 1.0 means that every item from class C was labelled as belonging to class C (but says nothing about how many items from other classes were incorrectly also labelled as belonging to class C).
Often, there is an inverse relationship between precision and recall, where it is possible to increase one at the cost of reducing the other, but context may dictate if one is more valued in a given situation:
A smoke detector is generally designed to commit many Type I errors (to alert in many situations when there is no danger), because the cost of a Type II error (failing to sound an alarm during a major fire) is prohibitively high.  As such, smoke detectors are designed with recall in mind (to catch all real danger), even while giving little weight to the losses in precision (and making many false alarms).  In the other direction, Blackstone's ratio, "It is better that ten guilty persons escape than that one innocent suffer," emphasizes the costs of a Type I error (convicting an innocent person). As such, the criminal justice system is geared toward precision (not convicting innocents), even at the cost of losses in recall (letting more guilty people go free). 
A brain surgeon removing a cancerous tumor from a patient's brain illustrates the tradeoffs as well: The surgeon needs to remove all of the tumor cells since any remaining cancer cells will regenerate the tumor. Conversely, the surgeon must not remove healthy brain cells since that would leave the patient with impaired brain function.

---
Source: https://en.wikipedia.org/wiki/Precision_and_recall (CC BY-SA 4.0)
