from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.ml.feature import HashingTF, Tokenizer
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.feature import StopWordsRemover
from pyspark.ml.feature import *
from pyspark.ml.classification import *
from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.regression import LabeledPoint
from pyspark.ml.classification import NaiveBayes


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

def parseLine2(line):
    parts = line.split('#')
    label = float(parts[4])
    value  = parts[3]
    return ("halo",value)

# Put Data to DataFrame

data_mapped = sc.textFile('output-fix.txt').map(parseLine)
trainingData = data_mapped.toDF(['class', 'value'])

# Indexing the lable

labelIndexer = StringIndexer(inputCol = "class", outputCol = "label").fit(trainingData)

dataIndexed = labelIndexer.transform(trainingData)

dataIndexed.show()

# Splitting Words & Removing Stop Words

tokenizer = Tokenizer(inputCol="value", outputCol="words")
remover = StopWordsRemover(inputCol=tokenizer.getOutputCol(), outputCol="filtered")

tokenized = tokenizer.transform(dataIndexed)
removed = remover.transform(tokenized)

tokenized.show()
removed.show()

# Extracting Features

hashingTF = HashingTF(inputCol="filtered", outputCol="features", numFeatures=20)
hashed = hashingTF.transform(removed)

hashed.show()

splits = hashed.randomSplit([0.6, 0.4], 1234)
train = splits[0]
test = splits[1]

# create the trainer and set its parameters
nb = NaiveBayes(smoothing=1.0, modelType="multinomial")

# train the model
model = nb.fit(train)

# compute accuracy on the test set
result = model.transform(test)
predictionAndLabels = result.select("prediction", "label")
evaluator = MulticlassClassificationEvaluator(metricName="precision")
print("Accuracy: " + str(evaluator.evaluate(predictionAndLabels)))
