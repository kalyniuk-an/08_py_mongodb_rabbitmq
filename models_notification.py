from dataclasses import dataclass


@dataclass
class Notification:
    user_id: str
    message: str
    notification_type: str
