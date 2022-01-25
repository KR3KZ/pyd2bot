from enum import Enum


class IdentificationFailureReason(Enum):
    BAD_VERSION = 1
    WRONG_CREDENTIALS = 2
    BANNED = 3
    KICKED = 4
    IN_MAINTENANCE = 5
    TOO_MANY_ON_IP = 6
    TIME_OUT = 7
    BAD_IPRANGE = 8
    CREDENTIALS_RESET = 9
    EMAIL_UNVALIDATED = 10
    OTP_TIMEOUT = 11
    LOCKED = 12
    SERVICE_UNAVAILABLE = 53
    EXTERNAL_ACCOUNT_LINK_REFUSED = 61
    EXTERNAL_ACCOUNT_ALREADY_LINKED = 62
    UNKNOWN_AUTH_ERROR = 99
    SPARE = 100

    def __str__(self):
        matched = {
            1: "BAD_VERSION",
            2: "WRONG_CREDENTIALS",
            3: "BANNED", 
            4: "KICKED",
            5: "IN_MAINTENANCE",
            6: "TOO_MANY_ON_IP",
            7: "TIME_OUT",
            8: "BAD_IPRANGE",
            9: "CREDENTIALS_RESET",
            10: "EMAIL_UNVALIDATED",
            11: "OTP_TIMEOUT",
            12: "LOCKED",
            53: "SERVICE_UNAVAILABLE",
            61: "EXTERNAL_ACCOUNT_LINK_REFUSED",
            62: "EXTERNAL_ACCOUNT_ALREADY_LINKED",
            99: "UNKNOWN_AUTH_ERROR",
            100: "SPARE"
        }
        return matched[self.value]