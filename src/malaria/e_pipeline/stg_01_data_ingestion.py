import sys
from src.malaria import logging, CustomException
from src.malaria.b_entity.config_entity import DataIngestionConfig
from src.malaria.c_config.configuration import ConfigurationManager
from src.malaria.d_components.data_ingestion import DataIngestion


STAGE_NAME = "Data--Ingestion--Stage"

# -----------------------------------------------------------------------------


class DataIngestionPipeline:
    def __init__(self):
        pass

# -----------------------------------------------------------------------------
    def main(self):
        # Creates the root directory first with initialization
        config_manager = ConfigurationManager()
        logging.info(f"===========> Configuration Manager instance created")

        # Creates the directories under root_dir,
        # and returns all paths of directories as an instance
        data_ingestion_config = config_manager.get_data_ingestion_config()
        logging.info(f"===========> Data Ingestion directories Configured")

        # initializes all paths from data_ingestion_config
        # 1. download files 2. unzip the files
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        logging.info(f"===========> Data Ingestion completed")
# -----------------------------------------------------------------------------


if __name__ == '__main__':
    try:
        logging.info(
            f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
        DT_Pipe = DataIngestionPipeline()
        DT_Pipe.main()
        logging.info(
            f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)
