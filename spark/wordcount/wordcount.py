from __future__ import print_function

import sys
from operator import add

from pyspark import SparkContext

def splitWords(x):
  return x.split(' ')
def mapWords(x):
  return (x,1)
if __name__ == "__main__":
  
  #check that we have expected number of arguments
  if len(sys.argv) != 3:
    print("Got the following arguments:"+str(sys.argv))
    print("Usage: wordcount <input-file> <output-dir>", file=sys.stderr)
    exit(-1)
  
  #get the spark context
  sc = SparkContext(appName="PythonWordCount")
  
  #get input and output files
  inputFile=sys.argv[1]
  outputFile=sys.argv[2]
  
  #read in input
  lines = sc.textFile(inputFile)
  
  counts = lines.flatMap(splitWords).map(mapWords).reduceByKey(add)
  counts.saveAsTextFile(sys.argv[2])#works
  
  #convert to a list
  #output = counts.collect()
  
  #loop over the list and print out to std out
  #for (word, count) in output:
  #    print("%s: %i" % (word, count))
  #
  sc.stop()
