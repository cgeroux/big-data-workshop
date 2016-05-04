TARGET=wordcount

LOCALINPUTFILE=./sampleArchive.txt
INPUTDIR=/user/${USER}/examples/
INPUTFILE=sampleArchive.txt
OUTPUTDIR=${INPUTDIR}/wordcount/spark/python/output


#Settings for how to run the job:
#see https://spark.apache.org/docs/1.2.1/submitting-applications.html 
#for more details
NUM_CORES=1

#run using yarn schedualar
MASTER=yarn

#run using yarn schedualar in cluster mode
#MASTER=yarn-cluster

#run using yarn schedualar in cluster mode
#MASTER=yarn-client

#run on local machine with given number of cores
#MASTER=local[${NUM_CORES]

#run on spark standalone cluster
#MASTER=spark://master:7077

#cluster deploy mode
#DEPLOY_MODE=--deploy-mode cluster

#client deploy mode
#DEPLOY_MODE=

run: ${TARGET}.py cleanoutput uploadinputtohdfs
	spark-submit --master ${MASTER} --deploy-mode cluster --executor-cores ${NUM_CORES} ${TARGET}.py ${INPUTDIR}${INPUTFILE} ${OUTPUTDIR}

runbg: ${TARGET}.jar cleanoutput
	hadoop jar ${TARGET}.jar ${MAINCLASS} ${SEARCHSTRING} ${INPUTDIR}${INPUTFILE} ${OUTPUTDIR} &>std_out.txt&

uploadinputtohdfs: ${LOCALINPUTFILE}
	hdfs dfs -mkdir -p ${INPUTDIR}
	-hdfs dfs -put ${LOCALINPUTFILE} ${INPUTDIR}${INPUTFILE}

showoutput:
	hdfs dfs -cat ${OUTPUTDIR}/part-00000

cleanoutput:
	-hdfs dfs -rm -R ${OUTPUTDIR}

clean:
	@if [ -f ${TARGET}.class ];then rm ${TARGET}.class;echo rm ${TARGET}.class;fi;
	@if [ -f ${TARGET}.jar ];then rm ${TARGET}.jar;echo rm ${TARGET}.jar;fi;
	-rm *.class

help:
	@echo Targets:
	@echo   <no target>: builds the jar file
	@echo   run: runs the hadoop job in the forground
	@echo   runbg: runs the hadoop job in the background and redirects stdout and 
	@echo     std error to std_out.txt file
	@echo   clean: cleans up build files for a fresh rebuild
