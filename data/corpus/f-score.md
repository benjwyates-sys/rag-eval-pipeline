# F-score

In statistical analysis of binary classification and information retrieval systems, the F-score or F-measure is a measure of predictive performance. It is calculated from the precision and recall of the test, where the precision is the number of true positive results divided by the number of all samples predicted to be positive, including those not identified correctly, and the recall is the number of true positive results divided by the number of all samples that should have been identified as positive. Precision is also known as positive predictive value, and recall is also known as sensitivity in diagnostic binary classification.
The F1 score is the harmonic mean of the precision and recall. It thus symmetrically represents both precision and recall in one metric. The more generic 
  
    
      
        
          F
          
            β
          
        
      
    
    {\displaystyle F_{\beta }}
  
 score applies additional weights, valuing one of precision or recall more than the other.
The highest possible value of an F-score is 1.0, indicating perfect precision and recall, and the lowest possible value is 0, if the precision or the recall is zero.


== Etymology ==
The name F-measure is believed to be named after a different F function in Van Rijsbergen's book, when introduced to the Fourth Message Understanding Conference (MUC-4, 1992).


== Definition ==
The traditional F-measure or balanced F-score (F1 score) is the harmonic mean of precision and recall:

  
    
      
        
          F
          
            1
          
        
        =
        
          
            2
            
              
                
                  r
                  e
                  c
                  a
                  l
                  l
                
                
                  −
                  1
                
              
              +
              
                
                  p
                  r
                  e
                  c
                  i
                  s
                  i
                  o
                  n
                
                
                  −
                  1
                
              
            
          
        
        =
        2
        
          
            
              
                p
                r
                e
                c
                i
                s
                i
                o
                n
              
              ⋅
              
                r
                e
                c
                a
                l
                l
              
            
            
              
                p
                r
                e
                c
                i
                s
                i
                o
                n
              
              +
              
                r
                e
                c
                a
                l
                l
              
            
          
        
        =
        
          
            
              2
              
                T
                P
              
            
            
              2
              
                T
                P
              
              +
              
                F
                P
              
              +
              
                F
                N
              
            
          
        
      
    
    {\displaystyle F_{1}={\frac {2}{\mathrm {recall} ^{-1}+\mathrm {precision} ^{-1}}}=2{\frac {\mathrm {precision} \cdot \mathrm {recall} }{\mathrm {precision} +\mathrm {recall} }}={\frac {2\mathrm {TP} }{2\mathrm {TP} +\mathrm {FP} +\mathrm {FN} }}}
  

With precision = TP / (TP + FP) and recall = TP / (TP + FN), it follows that the numerator of F1 is the sum of their numerators and the denominator of F1 is the sum of their denominators.
If FP=FN

  
    
      
        
          F
          
            1
          
        
        =
        
          
            
              2
              
                T
                P
              
            
            
              2
              
                T
                P
              
              +
              2
              
                F
                P
              
            
          
        
        =
        
          
            
              T
              P
            
            
              
                T
                P
              
              +
              
                F
                P
              
            
          
        
      
    
    {\displaystyle F_{1}={\frac {2\mathrm {TP} }{2\mathrm {TP} +2\mathrm {FP} }}={\frac {\mathrm {TP} }{\mathrm {TP} +\mathrm {FP} }}}
  

or

  
    
      
        
          F
          
            1
          
        
        =
        
          
            
              2
              
                T
                P
              
            
            
              2
              
                T
                P
              
              +
              2
              
                F
                N
              
            
          
        
        =
        
          
            
              T
              P
            
            
              
                T
                P
              
              +
              
                F
                N
              
            
          
        
      
    
    {\displaystyle F_{1}={\frac {2\mathrm {TP} }{2\mathrm {TP} +2\mathrm {FN} }}={\frac {\mathrm {TP} }{\mathrm {TP} +\mathrm {FN} }}}
  

So, F1 = precision = recall
If TP=FP=FN

  
    
      
        
          F
          
            1
          
        
        =
        
          
            
              2
              
                T
                P
              
            
            
       

---
Source: https://en.wikipedia.org/wiki/F-score (CC BY-SA 4.0)
