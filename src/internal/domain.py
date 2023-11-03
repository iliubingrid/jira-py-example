from datetime import datetime

from pytz import UTC

SPRINT_A_START_TIME = datetime(2023, 2, 22, 16, 30).replace(tzinfo=UTC)

SPRINTS = ["C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"]
UNUSED_SPRINTS = ["0", "A", "B", "C", "S", "T", "U", "V", "W", "X", "Y", "Z"]
