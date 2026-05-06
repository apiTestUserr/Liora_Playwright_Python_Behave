from dotenv import load_dotenv
import os

# On a besoin de charger les valeurs des variables dans le fichier .env puis fiare un get_env pour recuperer les valeurs a  partir de leur clé


load_dotenv(dotenv_path=".env.qa")

# -> represente le type de retour de la methode

def get_env(key: str) -> str:
  
   value = os.getenv(key)
   if value is None:
      raise ValueError(f"Environment variable key '{key}' is empty or not set") 
   return value


def get_bool_env(key: str) -> bool:
   
   return os.getenv(key, "false").lower() == "true"
