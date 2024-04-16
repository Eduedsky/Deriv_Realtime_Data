import subprocess
import time
import glob
import os
import logging
import shutil

# Constants
LOG_DIRECTORY = "/home/deriv"
GIT_REPO_PATH = "/home/github"
LOG_REPO_PATH = os.path.join(GIT_REPO_PATH, "logs")  # Subdirectory for logs within the Git repository
SCRIPT_LOG_FILE = "/home/github/git_push_log.log"

# Setup logging
logging.basicConfig(filename=SCRIPT_LOG_FILE, level=logging.INFO, filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

def copy_logs_to_repo(log_files):
    """ Copy log files to the repository directory. """
    os.makedirs(LOG_REPO_PATH, exist_ok=True)  # Ensure the directory exists
    for file in log_files:
        shutil.copy(file, LOG_REPO_PATH)
    return [os.path.join(LOG_REPO_PATH, os.path.basename(file)) for file in log_files]

def git_add_commit_push():
    print("Running git_add_commit_push")
    # Navigate to the Git repository directory
    os.chdir(GIT_REPO_PATH)
    print(f"Changed directory to {GIT_REPO_PATH}")

    # Find all matching log files
    log_files = glob.glob(os.path.join(LOG_DIRECTORY, 'realtime_data*.log'))  # Removes the underscore
    print(f"Found log files: {log_files}")
    if log_files:
        copied_files = copy_logs_to_repo(log_files)
        print(f"Copied log files: {copied_files}")
        # Add files to staging
        subprocess.check_call(['git', 'add'] + copied_files)
        print("Added files to staging.")
        # Commit changes
        subprocess.check_call(['git', 'commit', '-m', 'Automated log update'])
        print("Committed the changes.")
        # Push changes to GitHub
        subprocess.check_call(['git', 'push', 'origin', 'main'])
        print("Pushed the changes to GitHub.")
        logging.info("Updated the repository with new log files.")
    else:
        print("No new log files to update.")
        logging.info("No new log files to update.")

def main():
    while True:
        git_add_commit_push()
        print("Sleeping for 60 seconds...")
        time.sleep(60)  # Sleep for 1 minute

if __name__ == "__main__":
    main()
