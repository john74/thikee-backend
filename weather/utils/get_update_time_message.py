from django.utils import timezone


def get_update_time_message(setting):
    last_updated_time = setting.weather_data_last_updated
    if not last_updated_time:
        return

    current_time = timezone.now()
    time_passed_since_last_update = current_time - last_updated_time
    minutes_passed_since_last_update, seconds_passed_since_last_update = divmod(time_passed_since_last_update.total_seconds(), 60)

    update_interval = setting.weather_data_update_interval
    minutes_until_next_update = int(update_interval - minutes_passed_since_last_update)
    if minutes_until_next_update < 0:
        return

    seconds_until_next_update = int(60 - seconds_passed_since_last_update)
    time_message = (
        f"{minutes_until_next_update} minute{'s' if minutes_until_next_update != 1 else ''}"
    ) if minutes_until_next_update else (
        f"{seconds_until_next_update} second{'s' if seconds_until_next_update != 1 else ''}"
    )
    return time_message