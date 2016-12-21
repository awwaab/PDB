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

import pandas as pd


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
data = data_mapped.toDF(['class', 'value'])

# Split words in value

tokenizer = Tokenizer(inputCol="value", outputCol="words")
tokenized = tokenizer.transform(data)

# Extracting Feature

df = pd.DataFrame(tokenized)

print df

for words_label in tokenized.select("words", "class").get():
    	print (words_label)
