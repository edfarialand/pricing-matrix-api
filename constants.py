"""API constants"""
from enum import Enum


GDOCS_URL = "https://docs.google.com/spreadsheets/d/"
CSV_ENDING = "/export?format=csv&gid="
ATLAS_ID = "1tJQ-WdQZc91cCw0ExvPe6-lOkRuHVRbIsj4D2nNwuTo"

HANGGROUP_URL = "https://us7.campaign-archive.com/feed?u=c436b270f72b9fd53ce62e913&id=c249be35a0"

class AtlasSheets(Enum):
    """Maps sheet names to google doc ID"""
    GENERAL_INFO_GRADING = 1453313541
    NEW_IN_BOX = 677728473
    IPHONE_USED = 1216102336
    PARTS = 724685250
    APPLE_WATCH = 1323917402
    MACBOOKS = 2071430745
    SAMSUNG = 536270645
    IPAD_USED = 1559497964

    @property
    def csv_url(self) -> str:
        """returns url to csv download of sheet"""
        return GDOCS_URL + ATLAS_ID + CSV_ENDING + str(self.value)
