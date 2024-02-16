import os
import urllib.request as request
import zipfile
from src.mlops import logger
from src.mlops.utils.common import get_size
from src.mlops.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename = os.path.basename(self.config.source_URL)
            target_file = os.path.join(self.config.unzip_dir, filename)
            
            logger.info(f"Downloading file: {filename} from {self.config.source_URL} to {target_file}")
            request.urlretrieve(
                url=self.config.source_URL,
                filename=target_file
            )
            logger.info(f"File: {filename} has been downloaded")
            
            self.extract_zip_file(target_file)
            
            os.remove(target_file)            
            logger.info(f"File: {filename} has been removed")

        else:
            logger.info(f"File: {self.config.local_data_file} already exists")
        
            
    def extract_zip_file(self, target_file):
        logger.info(f"Extracting {target_file}")
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(target_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extraction completed")