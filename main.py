import sys
from src.malaria import logging, CustomException
from src.malaria.e_pipeline.stg_01_data_ingestion import DataIngestionPipeline
from src.malaria.e_pipeline.stg_02_base_model import BaseModelPipeline
from src.malaria.e_pipeline.stg_03_training import TrainingPipeline
from src.malaria.e_pipeline.stg_04_evaluation import EvaluationPipeline
# # -----------------------------------------------------------------------------
# STAGE_NAME = "Data--Ingestion--Stage"

# try:
#     logging.info(
#         f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
#     DT_Pipe = DataIngestionPipeline()
#     DT_Pipe.main()
#     logging.info(
#         f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logging.info(CustomException(e, sys))
#     raise CustomException(e, sys)

# -----------------------------------------------------------------------------
# STAGE_NAME = "Base--Model--Preparation"

# try:
#     logging.info(
#         f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
#     DT_Pipe = BaseModelPipeline()
#     DT_Pipe.main()
#     logging.info(
#         f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logging.info(CustomException(e, sys))
#     raise CustomException(e, sys)


# -----------------------------------------------------------------------------
# STAGE_NAME = "Training--the--Data"

# try:
#     logging.info(
#         f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
#     DT_Pipe = TrainingPipeline()
#     DT_Pipe.main()
#     logging.info(
#         f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logging.info(CustomException(e, sys))
#     raise CustomException(e, sys)
# # # -----------------------------------------------------------------------------
STAGE_NAME = "Evaluation--of--Model"

try:
    logging.info(
        f"\n\nx==========x\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
    eval_pipline = EvaluationPipeline()
    eval_pipline.main()
    logging.info(
        f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.info(CustomException(e, sys))
    raise CustomException(e, sys)
