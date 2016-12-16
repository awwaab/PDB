from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.ml.feature import HashingTF, Tokenizer
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.feature import StopWordsRemover


# Spark Configuration

conf = SparkConf().setAppName('Classify Trump Hillary')
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)


# Splitting Line

def parseLine(line):
    parts = line.split('#')
    label = float(parts[4])
    value  = parts[3]
    return (label, value)


# Put Data to DataFrame

data_mapped = sc.textFile('output-fix.txt').map(parseLine)
data = data_mapped.toDF(['label', 'value'])


# Extracting Features

tokenizer = Tokenizer(inputCol="value", outputCol="words")
wordsData = tokenizer.transform(data)
hashingTF = HashingTF(inputCol="words", outputCol="features", numFeatures=20)
featurizedData = hashingTF.transform(wordsData)


# Showing Data 

featurizedData.show()
data.show()


# Defining Model PIPELINE

labelIndexer = StringIndexer(inputCol="label", outputCol="indexedLabel").fit(featurizedData)
featureIndexer = VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=4).fit(featurizedData)
(trainingData, testData) = featurizedData.randomSplit([0.7, 0.3])
dt = DecisionTreeClassifier(labelCol="indexedLabel", featuresCol="indexedFeatures")


# Chain indexers and tree in a Pipeline

pipeline = Pipeline(stages=[labelIndexer, featureIndexer, dt])


# Train model.  This also runs the indexers.

model = pipeline.fit(trainingData)


# Make predictions.

predictions = model.transform(testData)


# Select example rows to display.

predictions.select("prediction", "indexedLabel", "features").show(5)


# Select (prediction, true label) and compute test error

evaluator = MulticlassClassificationEvaluator(labelCol="indexedLabel", predictionCol="prediction", metricName="precision")
accuracy = evaluator.evaluate(predictions)
print("Test Accuracy = %g " % (accuracy))

treeModel = model.stages[2]
# summary only
print(treeModel)
