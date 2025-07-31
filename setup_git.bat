@echo off
echo Initializing Git repository...
git init

echo Adding files to Git...
git add .

echo Creating initial commit...
git commit -m "Initial commit: AI Soul Cycle core implementation"

echo Adding remote repository...
git remote add origin https://github.com/priyanshu-kumar952/ai-soul-cycle-doctrine.git

echo Setting main branch...
git branch -M main

echo Pushing to remote repository...
git push -u origin main

echo Git setup complete!
pause
