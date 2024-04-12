"""API constants"""
from enum import Enum


GDOCS_URL = "https://docs.google.com/spreadsheets/d/"
CSV_ENDING = "/export?format=csv&gid="
ATLAS_ID = "1pu4Adxq4MGB6Qour0k__4gBdgnggWRoSVYnJUKgxzEw"

class AtlasSheets(Enum):
    """Maps sheet names to google doc ID"""
    GENERAL_INFO_GRADING = 1453313541
    NEW_IN_BOX = 677728473
    IPHONE_USED = 0
    PARTS = 724685250
    APPLE_WATCH = 1323917402
    MACBOOKS = 2071430745
    SAMSUNG = 536270645
    IPAD_USED = 1559497964

    @property
    def csv_url(self) -> str:
        """returns url to csv download of sheet"""
        return GDOCS_URL + ATLAS_ID + CSV_ENDING + str(self.value)
