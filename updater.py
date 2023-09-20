import hashlib
import os
import shutil
import git
import requests
class SelfUpdating:

    def __init__(self, repo_url, branch="master"):
        self.repo_url = f'https://github.com/{repo_url}'
        self.repo_name = repo_url
        self.branch = branch
        self.current_version = self.get_current_version()
    
    def check_for_update(self):
        latest_tag = self.get_latest_tag_from_github(self.repo_name)
        
        if latest_tag != self.current_version:
            print(f"New version {latest_tag} available! Updating...")
            self.update()
        else:
            print(f"Already on latest version {self.current_version}")
            
    def update(self):
        temp_dir = "./temp/" 
        if not os.path.exists(temp_dir):
            git.Git(".").clone(self.repo_url, temp_dir)
        try:
            # Checkout latest commit
            repo = git.Repo(temp_dir)
            repo.git.checkout('master')
            repo.git.pull()
        except git.exc.GitCommandError as e:  
            # Handle pull error
            print(f"Git pull failed: {e}")
            return
        # Walk through temp dir
        changed_files = []
        for root, dirs, files in os.walk(temp_dir):
            if '.git' in dirs:
                dirs.remove('.git')
            for file in files:
                file_path = os.path.join(root, file)
                # Calculate hash of file 
                current_hash = hashlib.sha256(open(file_path, "rb").read()).hexdigest()
                # Construct destination path        
                destination_path = os.path.join(os.getcwd(), file_path.split(temp_dir, 1)[1])  
                if os.path.exists(destination_path):
                    # Calculate hash of existing file
                    existing_hash = hashlib.sha256(open(destination_path, "rb").read()).hexdigest()
                else:
                    existing_hash = ""
                # Only overwrite if hashes don't match
                if current_hash != existing_hash:
                    shutil.copyfile(file_path, destination_path)  
                    changed_files.append(file)
        # Delete temp dir
        try:
            shutil.rmtree(temp_dir)
        except OSError as e:
            print(f"Error removing temp dir: {e}")
            
        self.current_version = self.get_current_version()
        
    def get_current_version(self):
        # Return current version somehow
        return "0.6"

    def get_latest_tag_from_github(self,repo_url):
        api_url = f"https://api.github.com/repos/{repo_url}/releases/latest"
        response = requests.get(api_url)
        if response.ok:
          release = response.json()
          return release["name"]
        else:
          print(f"Error fetching latest release: {response}")
          return "None"