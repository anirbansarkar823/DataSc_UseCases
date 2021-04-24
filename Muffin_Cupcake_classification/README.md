This small use case of classifying objects as either Muffins or Cupcake was originally done by Alice Zhao. This use case shows the implementation os SVM.

In SVM, we split the data using a hyperplane such that the distance (margin is more) of the nearest data points to the line is maximum [maximising the margin].

The line that divides is called hyperplane
The nearest points are called support vectors.
Lagrange Multipliers are used to solve this optimization problem.

Original GitHub Link: https://github.com/adashofdata
Original Youtube Video Link: https://youtu.be/N1vOgolbjSc

She prepared (normalized) the data from (ammount based) 2 cups, 1/2 cups etc. to (percent based) 47%, 24%
 for easy implementation of SVM model.
While converting to percentages, she ensured that each row sums to 100%.

She followed the below 6 steps to achieve the prediction and has beautifully explained each in her video:
1. Importing Libraries
2. Importing the Data
3. Preparing the Data
4. Fitting the Model (SVM)
5. Visualizing Results
6. Predicting New Cases (deployment)


## Observation: Muffins have more flour, while Cupcakes have more butter and sugar.



# C value (while creating the model; = 1.0 is default) decides bias and variance. High C value gives high variance (thus overfitting). Low C value gives low variance (thus underfitting).


#Multiple Classes:
for more than 2 class classifications
svm.SVC(kernel='linear', decision_function_shape='ovr') #ovr-One vs Rest; ovo-One vs One


# kernel Trick: 
adding another dimension for classification, when seperation is not possible in current dimention.

svm.SVC(kernel='rbf', C=1, gamma=2**-5) #rbf - radial kernel;

we need to specify, gamma and C along with kernel. High gamme gives more complexity(over fitting) and vice versa.


#pros and cons of SVM
pros:
- Good at dealing with high dimensional data (data with more features)
- works well on small dataset

cons:
- picking the right kernel is difficult and can be computationally intensive.


Future works:
We can pick other classification models using based on below ML algorithms
-Logistic Regression
-k Nearest Neighbors
-Decision trees
-Naive bayes
-Neural Networks