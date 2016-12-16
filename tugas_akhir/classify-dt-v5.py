from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.ml.feature import HashingTF, Tokenizer
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.feature import StopWordsRemover
from pyspark.ml.feature import *
from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.regression import LabeledPoint


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
trainingData = data_mapped.toDF(['label', 'value'])

# indexing the lable
labelIndexer = StringIndexer(inputCol = "label", outputCol = "indexedLabel").fit(trainingData)

dataIndexed = labelIndexer.transform(trainingData)

dataIndexed.show()


# reverse the index

converter = IndexToString(inputCol="indexedLabel", outputCol="originalCategory")
converted = converter.transform(dataIndexed)

converted.show()


# something

tokenizer = Tokenizer(inputCol="value", outputCol="words")
remover = StopWordsRemover(inputCol=tokenizer.getOutputCol(), outputCol="filtered")

tokenized = tokenizer.transform(converted)
removed = remover.transform(tokenized)

tokenized.show()
removed.show()


# Extracting Features

hashingTF = HashingTF(inputCol=remover.getOutputCol(), outputCol="features", numFeatures=20)
hashed = hashingTF.transform(removed)

hashed.show()


# Making Labeled Point

def labeling (line):
	return LabeledPoint(line[2], line[6])


# DT Model

dt = DecisionTreeClassifier(labelCol="indexedLabel", featuresCol="features")


# Train The Model

model = dt.fit(hashed)


####################################
###############MODEL SUDAH DILATIH
############## MENGELOLA DATA DARI USER SEKARANG
##################################################

# Put Data From Web to Dataframe
web_data_mapped = sc.textFile('input-web.txt').map(parseLine2)
testData = web_data_mapped.toDF(['nilai','value'])

# something


tokenizer = Tokenizer(inputCol="value", outputCol="words")
remover = StopWordsRemover(inputCol=tokenizer.getOutputCol(), outputCol="filtered")

tokenized = tokenizer.transform(testData)
removed = remover.transform(tokenized)

tokenized.show()
removed.show()


# Extracting Features

hashingTF = HashingTF(inputCol=remover.getOutputCol(), outputCol="features", numFeatures=20)
hashed = hashingTF.transform(removed)

predicts = model.transform(hashed)
predicts.show(5)
