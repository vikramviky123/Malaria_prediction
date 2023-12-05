import sys
from src.malaria import logging, CustomException

from src.malaria.c_config.configuration import ConfigurationManager
from src.malaria.d_components.base_model import BaseModel


# -----------------------------------------------------------------------------
STAGE_NAME = "Base--Model--Preparation"
# -----------------------------------------------------------------------------


class BaseModelPipeline:
    def __init__(self):
        pass

# -----------------------------------------------------------------------------
    def main(self):
        # Creates the root directory first with initialization
        config_manager = ConfigurationManager()
        logging.info(f"===========> Configuration Manager instance created")

        # Creates the directories under root_dir,
        # and returns all paths of directories as an instance
        base_model_config = config_manager.get_base_model_config()
        logging.info(f"===========> Base Model directories Configured")

        # initializes all paths from data_ingestion_config
        # 1. download files 2. unzip the files
        base_model = BaseModel(config=base_model_config)
        base_model.get_base_model()
        logging.info(f"===========> Base Model Created")
        base_model.update_base_model()
        logging.info(f"===========> Base Model Updated")
# -----------------------------------------------------------------------------


if __name__ == '__main__':
    try:
        logging.info(
            f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
        DT_Pipe = BaseModelPipeline()
        DT_Pipe.main()
        logging.info(
            f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)
