import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ps_wordcount.py <input_file> <output_directory>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()
    sc = spark.sparkContext

    lines = sc.textFile(sys.argv[1])
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x.lower(), 1)) \
                  .reduceByKey(lambda a, b: a + b)

    counts.saveAsTextFile(sys.argv[2])
    spark.stop()