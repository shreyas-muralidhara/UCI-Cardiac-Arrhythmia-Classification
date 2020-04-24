## Prediction and Classification of Cardiac Arrhythmia using Machine Learning
### Final project for CSC 522 - Automated Learning and Data Anlayis for Spring 2020 Term

Team members:  
* Shreyas Chikkballapur Muralidhara - schikkb
* Mangalnathan Vijayagopal - mvijaya2
* Nischal Kashyap - nkashya
* Pawandeep Mendiratta - psmendir


### Source Code: [Prediction and Classification of Cardiac Arrhythmia](https://colab.research.google.com/drive/1yfABjLEh7HithNjcZJxaTbH_XXj9RIOd)

#### ABSTARCT:
To detect and predict the type of arrhythmia based on Electro-cardiogram (ECG) tool using machine learning models andalgorithms. We will be training a model using a given datasetand then use test data to classify instances with unknownclass labels.

#### MOTIVATION AND INTRODUCTION:
Most cardiac disorders cause irregularities in heartbeat. Theseirregular patterns in rhythm of heartbeat is called Arrhyth-mia. Electrocardiogram (ECG) [1] is the most preferred toolused by clinical practitioners to capture heartbeat. ECG isrenowned to be cost-effective, easy to use and noninvasiveto the human body. However, Physicians may not interpretElectrocardiogram for large data sets effectively as it is timeconsuming and can also cause miss-classification of beats.They also cannot effectively identify the normalities andabnormalities in the heartbeat.Although single arrhythmia heartbeat may not have aserious impact on life, continuous arrhythmia beats can re-sult in fatal circumstances. Therefore, automatic detectionof arrhythmia beats from ECG signals is a significant taskin the field of cardiology. To eradicate the complexity andpossibility of human error in diagnosing, we leverage thecomputational power and indefatigability of machine learn-ing models.UCI Machine learning repository transformed the ECGsignals  into  QRS  complexes(column  10)  based  on  the  R-peak(column 19) of 17 different types of beats. Our approachincludes Weighted class models - Proportionate samplingfor all the 17 classes of beats because of a high standarddeviation in the number of samples produced per class. QRS complex extraction based on annotated files with makingR-peak as the centre and of constant size. Designing Machinelearning model including deep neural network and calibratehyperparameters to obtain the best results.The data set will be split accordingly (70/30 rule) into train-ing and testing data. We will be using 1D-CNN, MLP, SVMand KNN with k-fold cross validation models to achieve the objectives.

![blockdiag](https://media.github.ncsu.edu/user/14762/files/ea310780-860d-11ea-975a-a787bd71b9b1)

#### RATIONALE
* We implemented SVM because it is the most reliable modelfor the stratified arrhythmia data set for classifying and re-gression.
* We implemented KNN because this model requires no train-ing before making predictions. Therefore, new data can beseamlessly added to the model without impacting the accu-racy scores.
* Neural Networks are famous for high classification accuracy.This is because the deep layers of a neural network representshierarchical and non-linear combination of features and patterns detected from the input. Therefore, instead of hand cod-ing essential features, neural network autonomously choosesfeatures resulting in high classification accuracy. This justifies our choice of neural networks (MLP and 1D-CNN) forarrhythmia classification.
    * Multi Layer Perceptrons (MLP) are universal approximatorswhich can be used to create mathematical models using re-gression analysis. Since classification is a form of regressionwhen the class labels are categorical, MLPs make good classifier algorithms.
    * 1D-CNN is generally more preferred for image classification,but flattened images are equivalent to 1D-CNN with multipleattributes. Since the waveform is converted into attributesin the data set, 1D-CNN is also a good choice as a machinelearning model for this data set.


#### CONCLUSION
We were success-fully able to predict classifications for all the labels whichhad adequate information required to train the models andthen perform proportionate sampling of all the 16 classes ofheartbeats.In our current approach we have considered detecting andclassifying the class-imbalanced UCI Arrhythmia tabulardata based on the QRS wavelets based on the R-peak valueand achieved accuracy values ranging from 60% to 70% witha maximum accuracy of 73.53% by the Support Vector Machine with Linear Kernal, using the Weighted loss function.
