import os
import random
import datetime
import subprocess
from datetime import timedelta

def create_file_if_not_exists(filename):
    """Create a file if it doesn't exist."""
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write('')

def update_file(filename, content):
    """Update a file with new content."""
    with open(filename, 'w') as f:
        f.write(content)

def make_commit(date, commit_message):
    """Make a commit with the specified date."""
    # Set environment variables for the commit date
    os.environ['GIT_AUTHOR_DATE'] = date
    os.environ['GIT_COMMITTER_DATE'] = date
    
    # Add all files and commit
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', commit_message])

def is_weekday(date):
    """Check if the date is a weekday (not Saturday or Sunday)."""
    return date.weekday() < 5  # Monday=0, Sunday=6

def main():
    # Initialize git repository if not already initialized
    if not os.path.exists('.git'):
        subprocess.run(['git', 'init'])
    
    # Create a dummy file for commits
    dummy_file = 'activity.txt'
    create_file_if_not_exists(dummy_file)
    
    # Calculate the date range (1 year ago until yesterday)
    end_date = datetime.datetime.now().date() - timedelta(days=1)
    start_date = end_date - timedelta(days=365)
    
    current_date = start_date
    
    # Process each day in the date range
    while current_date <= end_date:
        if is_weekday(current_date):
            # Random number of commits for the day (between 1 and 8)
            num_commits = random.randint(1, 8)
            
            for i in range(num_commits):
                # Create a timestamp with a random hour for the current date
                hour = random.randint(9, 17)  # Between 9 AM and 5 PM
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                
                timestamp = datetime.datetime(
                    current_date.year, 
                    current_date.month, 
                    current_date.day,
                    hour, minute, second
                )
                
                # Format the date for Git
                date_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                
                # Update the file with a unique content
                content = f"Update {current_date} - {i+1}/{num_commits}"
                update_file(dummy_file, content)
                
                # Make the commit
                commit_message = f"Update {i+1} for {current_date}"
                make_commit(date_str, commit_message)
                
                print(f"Created commit {i+1}/{num_commits} for {current_date}")
        
        # Move to the next day
        current_date += timedelta(days=1)
    
    print("Commit history generation completed!")

if __name__ == "__main__":
    main()
