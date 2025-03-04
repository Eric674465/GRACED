import datetime

def display_current_datetime():
    """Displays the current date and time in a readable format."""

    current_datetime = datetime.datetime.now()  # Get the current date and time

    # Format the date and time
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current date and time: {formatted_datetime}")


if __name__ == "__main__":  # This ensures the function is only called when the script is run directly.
    display_current_datetime()
