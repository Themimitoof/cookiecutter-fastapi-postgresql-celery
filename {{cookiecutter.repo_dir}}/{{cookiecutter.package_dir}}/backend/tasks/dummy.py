import logging
import time

from {{cookiecutter.package_dir}}.backend import app

log = logging.getLogger(__name__)


@app.task
def dummy_created(dummy):
    log.info(f"New dummy created via the API! {dummy}")

    time.sleep(20)  # Do fake magic for "fun"

    log.info("Dummy processed.")
