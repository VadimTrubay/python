from dotenv import dotenv_values


"""Settings"""
config = dotenv_values(".env")
ADMIN_TOKEN = config['ADMIN_TOKEN']