import os
import sys
import urllib.request as request
from zipfile import ZipFile
from pathlib import Path

from src.malaria.b_entity.config_entity import DataIngestionConfig
from src.malaria import logging, CustomException
from src.malaria.f_utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

# -----------------------------------------------------------------------------
    def download_file(self):

        try:
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logging.info(
                    f"{filename} download! with following info: \n{headers}")
            else:
                logging.info(
                    f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

        except Exception as e:
            logging.info(CustomException(e, sys))
            raise CustomException(e, sys)

# -----------------------------------------------------------------------------
    def extract_zip_file(self):

        try:

            unzip_dir = self.config.unzip_dir
            os.makedirs(unzip_dir, exist_ok=True)
            logging.info(f"{unzip_dir} Directory created")

            with ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)

            logging.info(f"All files from zip were extracted to {unzip_dir}")

        except Exception as e:
            logging.info(CustomException(e, sys))
            raise CustomException(e, sys)
# -----------------------------------------------------------------------------
