import sys

from src.malaria import logging, CustomException
from src.malaria.c_config.configuration import ConfigurationManager
from src.malaria.d_components.training import Training
from src.malaria.d_components.callbacks import Callback

# -----------------------------------------------------------------------------
STAGE_NAME = "Training--the--Data"
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


class TrainingPipeline:
    def __init__(self):
        pass
# -----------------------------------------------------------------------------

    def main(self):
        # Creating configuration manager instance
        config = ConfigurationManager()
        # Configuring callback directories/ creating paths for callback directories
        prepare_callbacks_config = config.get_callback_config()
        # Configuring & Creating directories, Callbacks object
        prepare_callbacks = Callback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        # ---------------------------------------------
        # Configuring training directories/ creating paths for training directories
        training_config = config.get_training_config()
        # Loading the training configuration into Training
        training = Training(config=training_config)

        # ---------------------------------------------
        # training the data
        training.get_base_model()
        training.train_valid_generator()
        training.train(callback_list=callback_list)


# -----------------------------------------------------------------------------


if __name__ == '__main__':
    try:
        logging.info(
            f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
        training_pipeline = TrainingPipeline()
        training_pipeline.main()
        logging.info(
            f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)
