from pyspark.ml.feature import StringIndexer
df = spark.creatDataFrame([[0, 'a'], [1, 'b'], [2, 'c'], [3, 'a'], [4, 'a'], [5, 'c']], ['id', 'category'])
indexer = StringIndexer(inputCol='category', outputCol='categoryIndex')
model =indexer.fit(df)
indexed = model.transform(df)
indexed.show()