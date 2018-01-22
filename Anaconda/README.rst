Tip
====

You may wish to edit your .bashrc to prepend the Anaconda3 install location to PATH: ::

	export PATH=/home/jack/anaconda3/bin:$PATH

constructor::

	$ conda install constructor


Fill in the following stuff in `Spark 2 Client Advanced Configuration Snippet (Safety Valve) for spark2-conf/spark-env.sh` in cloudera manager `Spark2` `Configuration`::

	if [ -z "${PYSPARK_PYTHON}" ]; then
	export PYSPARK_PYTHON=/var/lib/hadoop-hdfs/anaconda3/envs/JackEnv/bin/python
	fi

From this doc_.

.. _doc: https://www.cloudera.com/documentation/enterprise/5-11-x/topics/spark_python.html#spark_python__section_ark_lkn_25

Conda::

	bin/conda create -n JackEnv --clone root
	envs/JackEnv/bin/pip install /tmp/spark/py2neo-pack/py2neo-3.1.2.tar.gz
