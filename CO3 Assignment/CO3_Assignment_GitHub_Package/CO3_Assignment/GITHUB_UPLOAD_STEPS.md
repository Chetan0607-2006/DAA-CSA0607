# GitHub upload steps
1. Sign in to https://github.com and select **+ > New repository**.
2. Name the repository `CO3_Assignment`, choose visibility, and click **Create repository**. Do not initialize with a README if using the command-line method.
3. Extract the ZIP, then open a terminal inside the `CO3_Assignment` folder.
4. Run `git init`, `git add .`, `git commit -m "Initial CO3 assignment submission"`, `git branch -M main`.
5. Run `git remote add origin https://github.com/YOUR_USERNAME/CO3_Assignment.git` (replace YOUR_USERNAME).
6. Run `git push -u origin main` and sign in when prompted.
7. Refresh GitHub and verify all Q1–Q7 folders, report files, screenshots and README are visible.

Alternative (browser): open new repository > **Add file > Upload files**, drag the extracted `CO3_Assignment` folder's CONTENTS into the upload area (not the ZIP), and click **Commit changes**. GitHub does not preserve empty directories, so placeholder README files are provided.

For later edits: `git add .`, `git commit -m "Complete report and screenshots"`, `git push`.
