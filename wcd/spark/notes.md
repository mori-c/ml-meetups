

![Learning path](https://image.slidesharecdn.com/bigdatausecaseshadoopinfosession2-190605175139/95/big-data-for-data-scientists-info-session-10-1024.jpg?cb=1559757230)
10
---
![learning path](https://image.slidesharecdn.com/bigdatausecaseshadoopinfosession2-190605175139/95/big-data-for-data-scientists-info-session-11-1024.jpg?cb=1559757230)
11
---
![data science essential skills](https://image.slidesharecdn.com/bigdatausecaseshadoopinfosession2-190605175139/95/big-data-for-data-scientists-info-session-14-1024.jpg?cb=1559757230)
14
---

![data science job requirements](https://image.slidesharecdn.com/bigdatausecaseshadoopinfosession2-190605175139/95/big-data-for-data-scientists-info-session-15-1024.jpg?cb=1559757230)
15
---

![data science myth](https://image.slidesharecdn.com/bigdatausecaseshadoopinfosession2-190605175139/95/big-data-for-data-scientists-info-session-16-1024.jpg?cb=1559757230)
16
---

## Portfolio
![demo projects](https://image.slidesharecdn.com/bigdatausecaseshadoopinfosession2-190605175139/95/big-data-for-data-scientists-info-session-76-1024.jpg?cb=1559757230)
- kaggle challenges
- portfolio
- weclouddata wecareer 6 months


![ds types](https://image.slidesharecdn.com/bigdatausecaseshadoopinfosession2-190605175139/95/big-data-for-data-scientists-info-session-17-1024.jpg?cb=1559757230)
17
---

![databases](https://image.slidesharecdn.com/bigdatausecaseshadoopinfosession2-190605175139/95/big-data-for-data-scientists-info-session-30-1024.jpg?cb=1559757230)
30
---


Distributed Systems
- data storage issues, eg IoT data
- EMR (elastic : cluster data)
- split data into 4 quadrants, where 1 quad gets copied thrice for ***fault tolerancy***


## Map (function or class) Reduce : Hadoop
![HDFS](https://image.slidesharecdn.com/bigdatausecaseshadoopinfosession2-190605175139/95/big-data-for-data-scientists-info-session-47-1024.jpg?cb=1559757230)
47
![HDFS replications](https://image.slidesharecdn.com/bigdatausecaseshadoopinfosession2-190605175139/95/big-data-for-data-scientists-info-session-48-1024.jpg?cb=1559757230)
48
![name node](https://image.slidesharecdn.com/bigdatausecaseshadoopinfosession2-190605175139/95/big-data-for-data-scientists-info-session-49-1024.jpg?cb=1559757230)
49
![mapreduce word count](https://image.slidesharecdn.com/bigdatausecaseshadoopinfosession2-190605175139/95/big-data-for-data-scientists-info-session-50-1024.jpg?cb=1559757230)
50
![mapreduce java and hive](https://image.slidesharecdn.com/bigdatausecaseshadoopinfosession2-190605175139/95/big-data-for-data-scientists-info-session-51-1024.jpg?cb=1559757230)
51

![mapreduce hadoop open source and infrasturcture ready](https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.slidesharecdn.com%2F2-hadoop-mapreduce-fundamentals-130518223334-phpapp02%2F95%2Fslide-31-1024.jpg&f=1)
![mapreduce overall word count process](https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.slidesharecdn.com%2Fmodule3-bigdataandhadoop-160425063358%2F95%2Fhadoop-mapreduce-framework-29-638.jpg%3Fcb%3D1461743943&f=1)

- if group A by customer ID, key value pairs
  - hash particioner
- else HDFR to shuffle data 
- another example, TDFR for text 
- node == server
  - word, occurances, map, combine, shuffle/sort, reduce (aggregated each)
  - shuffle and sort

big data 


![spark unified data platform](https://image.slidesharecdn.com/bigdatausecaseshadoopinfosession2-190605175139/95/big-data-for-data-scientists-info-session-61-1024.jpg?cb=1559757230)
61
- Hive (SQL & Hadoop)
- mapreduce is slow because it replicates data
-  spark core (scala) replaces mapreduce
-  spark code (core & dataframes) is easier to write than mapreduce
-  SQL, ML, graph computation
-  **as a developer, you'll need to learn how to work with a lot of APIs securely**

![mapreduce vs spark](https://image.slidesharecdn.com/bigdatausecaseshadoopinfosession2-190605175139/95/big-data-for-data-scientists-info-session-59-1024.jpg?cb=1559757230)
59
- Bottleneck: HDFS > MapReduce > HDFS
- Hadoop doesn't lose data


## Data lineage 
- **logistic regression & linear support vector**
![data lineage](https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.slidesharecdn.com%2Funtitled-141215093512-conversion-gate02%2F95%2Funified-big-data-processing-with-apache-spark-23-638.jpg%3Fcb%3D1418636227&f=1)
``` 
 DATA
   sc.textFile(hfs://)         # STAGE 01
     > rdd_0.filter()            # one csv file / rdd
      > rdd_1.map() 
        > rdd_2.reductByKey()  # STAGE 2 IN TRANSFORMATION
  ```
- one data transformed as a series of data numbered 
- replicating is costly in memory
![lineage in spark](https://image.slidesharecdn.com/large-scalelogisticregressionandlinearsupportvectormachinesusingspark-161108042002/95/large-scale-logistic-regression-and-linear-support-vector-machines-using-spark-29-638.jpg?cb=1478578896)
- sc = spark context
- textFile() = read text file in hadoop
- RDD = res dataset = in memory HDFS
- filter() = filter data based on x (operator)
- map() = column filtering select statement for fewer and less data (operator)
- reduceByKey()

![hadoop word count with mapreduce vs spark code](https://image.slidesharecdn.com/spark-overview-june2014-140711131800-phpapp01/95/apache-spark-hadoop-18-638.jpg?cb=1425492160)

PySpark
| code | explaination |
| ---- | ------------ |
| line = sc.textFile(hfs://)      |    read and identify data          |
| errors = lines.filter(lambda s: s.strartswith("ERROR))  |    read, parse, split (e.g.  timestamp), log to check for errors     |
| 
messages = erros.map(lambda s: split('\t'[2]))
split data
messages.cache()
cache
messages.filter
apply data by counting of saved memory data
- saving data, counting ```.count()```



![]()
- joint account ID must match for example of 3 months of history
- **logical plan** is where you write your code
A: ``` filter > join > tx | accounts ```
B: ``` join > filter ( > scan tx) | account ```
C: ``` join > optim scan | optim scan > redshift |```
- join is expensive
- use functions and operations in the dataframe for best optimization
- spark & kubernetes

DS Pipeline Deploy as Batch Scoring / Predictive APIs
ML engineer
- version control
- APIs
- write really good code
- banks, retailers

## Scikit-Learn 
numerical value = multiprocessing GPU core used
- n_jobs = 1  -->  Logistic regression Classifier
- n_jobs = 4 --> Random Forest
- n_jobs = -1 -->

## Embarrassingly Parrellel Jobs
- 1 node : 1 model training for batch scoring
- scikit-learn in spark for scoring
- distrubuted computing with schoastic gradient descent
- place all features in VectureAssembler

## SageMaker Deployment
- prep data before ETL with spark, e.g. labels, EMR clustering for ETL
- save to aws s3 to produce scoring on reduced data
- train model sagemaker (containerizer wrapper) or locally on computer
  - or deploy your secret sauce model in aws sagemaker and not in spark
- run notebook to see models
- deploy model from container to ECR instance with docker prediction API endpoint
- call transform API to do batch scoring
- 
![]()
![]()
![]()
![]()
![]()
![]()


Workshop:

[PySpark Dataframe](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/5167671179219994/1872946994452444/342380500410564/latest.html)
