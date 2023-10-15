from pyspark.sql import SparkSessionimport get_all_variables as gavimport loggingimport logging.configlogging.config.fileConfig(fname='../utils/logging_to_log.conf')logger = logging.getLogger('create_objects')def get_spark_object(envn,appName):    try:        logger.info(f'get spark_object() is start....The "{envn}" is used.')        if envn == 'TEST':            master = 'local'        else:            master = 'yarn'        spark = SparkSession \                    .builder \                        .master(master) \                            .appName(appName) \                                .getOrCreate()    except Exception as exp:        logger.error('Error in the method- get_spark_object(). Please check the Stack Trash ,' + str(exp))    else:        logger.info("Spark Object is Creating!!!")    return spark