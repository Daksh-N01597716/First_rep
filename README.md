Create a GitHub Account:
Visit GitHub.
Click on “Sign Up”.
Fill in the sign-up form with your details.
Verify your email address when prompted.

Create a New Repository on GitHub:
Once logged in, click on the “+” icon in the upper-right corner and select “New repository”.
Name your repository and provide a brief description.
Choose to make the repository either public or private.
Initialize the repository with a README if you wish.
Click “Create repository”.

Install Git on Linux:
Open a terminal.
Update your package lists:
sudo apt-get update

Install Git:
sudo apt-get install git

Configure Git:
Set your global username:
git config --global user.name "Your Name"

Set your global email:
git config --global user.email "your_email@example.com"

Generate an SSH Key Pair (Optional but Recommended):
Generate a new SSH key pair:
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
Press Enter to accept the default file location.
Enter a secure passphrase when prompted.

Add the SSH Key to the SSH-Agent:
Start the ssh-agent in the background:
eval "$(ssh-agent -s)"
Add your SSH private key to the ssh-agent:
ssh-add ~/.ssh/id_rsa

Add the SSH Key to Your GitHub Account:
Copy the SSH public key to your clipboard:
cat ~/.ssh/id_rsa.pub | xclip -selection clipboard
Go to GitHub, click on your profile picture, then click “Settings”.
In the user settings sidebar, click “SSH and GPG keys”.
Click “New SSH key”, paste your key into the field, and click “Add SSH key”.

In the terminal, navigate to where you want your project:
cd path/to/your/project

Clone the repository:
Use the SSH URL to clone your repository:
git clone https://github.com/yourusername/yourrepository.git

Create a Python Virtual Environment:
Navigate into your project directory:
cd yourrepository

Create a virtual environment:
python3 -m venv venv

Activate the virtual environment:
source venv/bin/activate

Add a Python File:
Create a new Python file for your project:
touch main.py

Edit the file using a text editor, like nano or vim.
Write Your Python Code:
For example, a simple Python script:
Python

# main.py
print("Hello, GitHub!")
AI-generated code. Review and use carefully. More info on FAQ.
Stage and Commit Your Python File:
Add the file to staging:
git add main.py

Commit the file to your local repository:
git commit -m "Add initial Python script"


Push Your Changes to GitHub:
Push the commit to your remote repository:
git push origin main

Complete Project Requirements:
Continue to develop your project, committing changes frequently.
Once all requirements are met, push the final changes to GitHub.
Deactivate Virtual Environment (When Done):
To exit your virtual environment:
deactivate

To view the full Git log after all the changes, you can use the git log command in your terminal. This command shows the commit history for the current branch you’re on, listing the commits in reverse chronological order. 
Here’s how you can do it:
git log
This will display the full commit logs with details such as the commit hash, author, date, and commit message.

For a more condensed view, you can use:
git log --oneline
This will show each commit as a single line, which is useful for getting a quick overview of the history.

If you want to see the changes introduced in each commit, you can use:
git log -p
This will display the diff of each commit.

And if you’re interested in a graphical representation of the commit history, you can use:
git log --graph --all --decorate
This command will show you a text-based graphical representation of the commit history, including branches and tags.

Remember to navigate to your repository directory in the terminal before running these commands.
