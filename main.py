import logging
import time
import random

def setup_logging():

    #log_format = '%(asctime)s - %(process)d:%(thread)d:%(threadName)s - %(name)s - %(levelname)s - %(message)s'
    log_format = '%(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO,
                        format=log_format,
                        handlers=[logging.StreamHandler()])

def main():

    setup_logging()
    logger = logging.getLogger("worker")



    MAX_PROC_RUNTIME_IN_SECONDS = 30 # 5 minutes

    logger.info("App starting up. max_proc_runtime_in_seconds=%d", MAX_PROC_RUNTIME_IN_SECONDS)

    MIN_SLEEP_TIME_IN_SECONDS = 5
    MAX_SLEEP_TIME_IN_SECONDS = 10

    proc_runtime_in_secs = 0

    while (proc_runtime_in_secs < MAX_PROC_RUNTIME_IN_SECONDS):

        logger.info("Proc running for %d seconds", proc_runtime_in_secs)

        start = time.monotonic()

        logger.info("Doing some work")
        sleep_for = random.randint(MIN_SLEEP_TIME_IN_SECONDS, MAX_SLEEP_TIME_IN_SECONDS)
        logger.info("Sleeping for %d", sleep_for)
        time.sleep(sleep_for)

        end = time.monotonic()

        proc_runtime_in_secs += end - start

    logger.info("Exceeded max runtime (%d). Exiting", MAX_PROC_RUNTIME_IN_SECONDS)
    

if __name__ == "__main__":
    main()
