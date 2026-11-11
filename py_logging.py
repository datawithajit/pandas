import logging

logging.basicConfig(
    filename="py_code.logs",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"

)

logging.info("Pipeline started")
logging.info("Extracting data")
logging.info("Data extracted successfully")
logging.info("Loading data into database")
logging.info("Pipeline completed")

print("Logging config successfully.")