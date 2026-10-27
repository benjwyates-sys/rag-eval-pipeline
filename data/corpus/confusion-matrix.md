# Confusion matrix

A confusion matrix, also known as error matrix, is a specific table layout that allows visualization of the performance of a person or an algorithm on a specific task. In audiology these matrices measure how a person can hear specific words or sounds. In machine learning these matrices show the success of the learning system both in supervised learning and unsupervised learning, where they are usually called matching matrix. 
Each row of the matrix represents the instances in an actual class while each column represents the instances in a predicted class, or vice versa – both variants are found in the literature. The diagonal of the matrix therefore represents all instances that are correctly predicted. The name stems from the fact that it makes it easy to identify whether the system is confusing two classes (i.e., commonly mislabeling one class as another). The confusion matrix has its origins in human perceptual studies of auditory stimuli. It was adapted for machine learning studies and used by Frank Rosenblatt, among other early researchers, to compare human and machine classifications of visual (and later auditory) stimuli.
It is a special kind of contingency table, with two dimensions ("actual" and "predicted"), and identical sets of "classes" in both dimensions (each combination of dimension and class is a variable in the contingency table).


== Example ==
Given a sample of 12 individuals, 8 that have been diagnosed with cancer and 4 that are cancer-free, where individuals with cancer belong to class 1 (positive) and non-cancer individuals belong to class 0 (negative), we can display that data as follows:

Assume that we have a classifier that distinguishes between individuals with and without cancer in some way, we can take the 12 individuals and run them through the classifier. The classifier then makes 9 accurate predictions and misses 3: 2 individuals with cancer wrongly predicted as being cancer-free (sample 1 and 2), and 1 person without cancer that is wrongly predicted to have cancer (sample 9).

Notice, that if we compare the actual classification set to the predicted classification set, there are 4 different outcomes that could result in any particular column:

The actual classification is positive and the predicted classification is positive (1,1). This is called a true positive result because the positive sample was correctly identified by the classifier.
The actual classification is positive and the predicted classification is negative (1,0). This is called a false negative result because the positive sample is incorrectly identified by the classifier as being negative.
The actual classification is negative and the predicted classification is positive (0,1). This is called a false positive result because the negative sample is incorrectly identified by the classifier as being positive.
The actual classification is negative and the predicted classification is negative (0,0). This is called a true negative result because the negative sample gets correctly identified by the classifier.
We can then perform the comparison between actual and predicted classifications and add this information to the table, making correct results appear in green so they are more easily identifiable.

The template for any binary confusion matrix uses the four kinds of results discussed above (true positives, false negatives, false positives, and true negatives) along with the positive and negative classifications. The four outcomes can be formulated in a 2×2 confusion matrix, as follows:

The color convention of the three data tables above were picked to match this confusion matrix, in order to easily differentiate the data.
Now, we can simply total up each type of result, substitute into the template, and create a confusion matrix that will concisely summarize the results of testing the classifier:

In this confusion matrix, of the 8 samples with cancer, the system judged that 2 were cancer-free, and of the 4 samples without cancer, it predicted that 1 did have cancer. All correct predictions are located in the diagonal of the table (highlighted in green), so it is easy to visually inspect the table for prediction errors, as values outside the diagonal will represent them. By summing up the 2 rows of the confusion matrix, one can also deduce the total number of positive (P) and negative (N) samples in the original dataset, i.e. 
  
    
      
        P
        =
        T
        P
        +
        F
        N
      
    
    {\displaystyle P=TP+FN}
  
 and 
  
    
      
        N
        =
        F
        P
        +
        T
        N
      
    
    {\displaystyle N=FP+TN}
  
.


== Table of confusion ==
In predictive analytics, a table of confusion or Santhosh's table of confusion (sometimes also called a confusion matrix) is a table with two rows and two columns that reports the number of true positives, false negatives, false positives, and true negatives. This allows more detailed analysis than simply observing the proportion of correct classifications (accuracy). Accuracy will yield misleading results if the data set is unbalanced; that is, when the numbers of observations in different classes vary greatly. 
For example, if there were 95 cancer samples and only 5 non-cancer samples in the data, a particular classifier might classify all the observations as having cancer. The overall accuracy would be 95%, but in more detail the classifier would have a 100% recognition rate (sensitivity) for the cancer class but a 0% recognition rate for the non-cancer class.

---
Source: https://en.wikipedia.org/wiki/Confusion_matrix (CC BY-SA 4.0)
