import os 
from pathlib import Path
from dotenv import load_dotenv
# import yaml

load_dotenv()

class Config():
    """
    Class contains all the configuration of the project.
        1) data
        2) environment variables
        3) model configurations
    """

    PROJECT_ROOT = Path(__file__).resolve().parents[1] # Go up two folders to the project root folder

    def __init__(self):
        
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.raw_data_path = self.PROJECT_ROOT / "data/raw"


if __name__ == "__main__":
    
    cfg = Config()
    print(cfg.api_key)
    print(cfg.PROJECT_ROOT)
    print(cfg.raw_data_path)
    

