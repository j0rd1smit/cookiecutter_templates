import datetime

from src.utils.os_utils import relative_to


class RootPaths:
    DATA_EXTERNAL = relative_to(__file__, "../data/external")
    DATA_INTERIM = relative_to(__file__, "../data/interim")
    DATA_PROCESSED = relative_to(__file__, "../data/processesed")
    DATA_RAW = relative_to(__file__, "../data/raw")
    MODELS = relative_to(__file__, "../data/models")
    REPORTS = relative_to(__file__, "../data/reports")


class DataExternalPaths:
    pass


class DataInterimPaths:
    pass


class DataProcessedPaths:
    pass


class DataRawPaths:
    pass


class ModelPaths:
    @staticmethod
    def make_timestamped_dir(name: str = ""):
        now = datetime.datetime.now()
        timestamp_str = now.strftime("%Y_%m_%d_%H_%M_%S")
        
        path = RootPaths.MODELS / (name + timestamp_str)
        path.mkdir(parents=True, exist_ok=True)
        
        return path


class ReportPaths:
    pass