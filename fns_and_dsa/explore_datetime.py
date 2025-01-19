from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days):
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date after {days} days: {formatted_future_date}")
    return future_date

def main():
    # Display the current date and time
    current_date = display_current_datetime()
    
    # Calculate a future date
    try:
        days = int(input("Enter the number of days to add: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")

if __name__ == "__main__":
    main()