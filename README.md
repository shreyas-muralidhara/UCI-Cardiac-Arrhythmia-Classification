## Prediction and Classification of Cardiac Arrhythmia using Machine Learning
### Final project for CSC 522 - Automated Learning and Data Anlayis for Spring 2020 Term

Team members:  
* Shreyas Chikkballapur Muralidhara - schikkb
* Mangalnathan Vijayagopal - mvijaya2
* Nischal Kashyap - nkashya
* Pawandeep Mendiratta - psmendir


### Source Code: [Prediction and Classification of Cardiac Arrhythmia](https://colab.research.google.com/drive/1yfABjLEh7HithNjcZJxaTbH_XXj9RIOd)

#### ABSTRACT:
To detect and predict the type of arrhythmia based on Electro-cardiogram (ECG) tool using machine learning models andalgorithms. We will be training a model using a given datasetand then use test data to classify instances with unknownclass labels.

#### MOTIVATION AND INTRODUCTION:
Most cardiac disorders cause irregularities in heartbeat. These irregular patterns in rhythm of heartbeat is called Arrhythmia. Electrocardiogram (ECG) [1] is the most preferred toolused by clinical practitioners to capture heartbeat. ECG isrenowned to be cost-effective, easy to use and noninvasiveto the human body. However, Physicians may not interpret Electrocardiogram for large data sets effectively as it is time consuming and can also cause miss-classification of beats. They also cannot effectively identify the normalities and abnormalities in the heartbeat. Although single arrhythmia heartbeat may not have aserious impact on life, continuous arrhythmia beats can re-sult in fatal circumstances. Therefore, automatic detectionof arrhythmia beats from ECG signals is a significant taskin the field of cardiology. To eradicate the complexity and possibility of human error in diagnosing, we leverage the computational power and indefatigability of machine learn-ing models.UCI Machine learning repository transformed the ECGsignals  into  QRS  complexes(column  10)  based  on  the  R-peak(column 19) of 17 different types of beats. Our approach includes Weighted class models - Proportionate sampling for all the 17 classes of beats because of a high standard deviation in the number of samples produced per class. QRS complex extraction based on annotated files with makingR-peak as the centre and of constant size. Designing Machine learning model including deep neural network and calibrate hyperparameters to obtain the best results.The data set will be split accordingly (70/30 rule) into train-ing and testing data. We will be using 1D-CNN, MLP, SVM and KNN with k-fold cross validation models to achieve the objectives.

![blockdiag](https://media.github.ncsu.edu/user/14762/files/ea310780-860d-11ea-975a-a787bd71b9b1)

#### RATIONALE
* We implemented SVM because it is the most reliable model for the stratified arrhythmia data set for classifying and re-gression.
* We implemented KNN because this model requires no train-ing before making predictions. Therefore, new data can be seamlessly added to the model without impacting the accu-racy scores.
* Neural Networks are famous for high classification accuracy.This is because the deep layers of a neural network represents hierarchical and non-linear combination of features and patterns detected from the input. Therefore, instead of hand cod-ing essential features, neural network autonomously chooses features resulting in high classification accuracy. This justifies our choice of neural networks (MLP and 1D-CNN) for arrhythmia classification.
    * Multi Layer Perceptrons (MLP) are universal approximators which can be used to create mathematical models using re-gression analysis. Since classification is a form of regression when the class labels are categorical, MLPs make good classifier algorithms.
    * 1D-CNN is generally more preferred for image classification,but flattened images are equivalent to 1D-CNN with multiple attributes. Since the waveform is converted into attributes in the data set, 1D-CNN is also a good choice as a machine learning model for this data set.


#### CONCLUSION
We were success-fully able to predict classifications for all the labels which had adequate information required to train the models and then perform proportionate sampling of all the 16 classes of heartbeats.In our current approach we have considered detecting and classifying the class-imbalanced UCI Arrhythmia tabular data based on the QRS wavelets based on the R-peak value and achieved accuracy values ranging from 60% to 70% with a maximum accuracy of 73.53% by the Support Vector Machine with Linear Kernel, using the Weighted loss function.
