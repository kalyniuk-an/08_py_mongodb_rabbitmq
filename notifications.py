def send_email(notification):
    print(
        f"Email sent to user {notification['user_id']}: "
        f"{notification['message']}"
    )


def send_sms(notification):
    print(
        f"SMS sent to user {notification['user_id']}: "
        f"{notification['message']}"
    )