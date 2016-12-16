from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.ml.feature import HashingTF, Tokenizer
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.feature import StopWordsRemover
from pyspark.ml.feature import *


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


# Removing Stop Words

tokenizer = Tokenizer(inputCol="value", outputCol="words")
remover = StopWordsRemover(inputCol=tokenizer.getOutputCol(), outputCol="filtered")


# Extracting Features

hashingTF = HashingTF(inputCol=remover.getOutputCol(), outputCol="features", numFeatures=20)

labelIndexer = StringIndexer(inputCol = "label", outputCol = "indexedLabel").fit(data)
# Defining Model PIPELINE

(trainingData, testData) = data.randomSplit([0.7, 0.3])
dt = DecisionTreeClassifier(labelCol="indexedLabel", featuresCol="features")


# Chain indexers and tree in a Pipeline

pipeline = Pipeline(stages=[tokenizer, remover, hashingTF, labelIndexer, dt])


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

treeModel = model.stages[4]

# summary only
print(treeModel)

sc.parallelize(Seq(treeModel), 1).saveAsObjectFile("dt.model")

