# Git Light

A tool to generate a GitHub contribution history with a natural commit pattern.

## Features

- Creates a realistic commit history that appears as daily activity on GitHub
- Generates 1-8 random commits on weekdays
- Occasionally adds 1-3 commits on some weekends (40% of weekend days)
- Skips commits on other weekend days (60% of weekend days)
- Customizable date range for commit history

## Usage

### Basic Usage

Run the `generate_history.bat` file by double-clicking it or from the command line:

```
generate_history.bat
```

This will create a year's worth of commit history by default (from 1 year ago until yesterday).

### Custom Date Range

You can specify a custom date range using the `--start-date` and `--end-date` parameters:

```
generate_history.bat --start-date 2023-01-01 --end-date 2023-12-31
```

You can also specify just one of the parameters:

```
generate_history.bat --start-date 2023-01-01
generate_history.bat --end-date 2023-12-31
```

Dates should be in the format `YYYY-MM-DD`.

## Pushing to GitHub

After generating the commit history, you can push the repository to GitHub with:

```
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main --force
```

Note: You may need to use `--force` when pushing to override GitHub's history.

## GitHub Badges

You can add badges to your GitHub repository to display various information. Here are some common badges you can add to your README.md:

### Basic Repository Badges

```markdown
![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/YOUR_REPO_NAME)
![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/YOUR_REPO_NAME)
![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/YOUR_REPO_NAME)
![GitHub pull requests](https://img.shields.io/github/issues-pr/YOUR_USERNAME/YOUR_REPO_NAME)
![GitHub license](https://img.shields.io/github/license/YOUR_USERNAME/YOUR_REPO_NAME)
```

### Activity Badges

```markdown
![GitHub last commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/YOUR_REPO_NAME)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/YOUR_USERNAME/YOUR_REPO_NAME)
![GitHub contributors](https://img.shields.io/github/contributors/YOUR_USERNAME/YOUR_REPO_NAME)
```

### Size and Download Badges

```markdown
![GitHub repo size](https://img.shields.io/github/repo-size/YOUR_USERNAME/YOUR_REPO_NAME)
![GitHub code size](https://img.shields.io/github/languages/code-size/YOUR_USERNAME/YOUR_REPO_NAME)
![GitHub language count](https://img.shields.io/github/languages/count/YOUR_USERNAME/YOUR_REPO_NAME)
![GitHub top language](https://img.shields.io/github/languages/top/YOUR_USERNAME/YOUR_REPO_NAME)
```

### Custom Badges

You can also create custom badges using shields.io:

```markdown
![Custom Badge](https://img.shields.io/badge/LABEL-MESSAGE-COLOR)
```

For example:
```markdown
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Made with](https://img.shields.io/badge/made%20with-Python-green)
```

### How to Use

1. Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repository name.
2. Copy the desired badge markdown code and paste it at the top of your README.md file.
3. For custom badges, replace `LABEL`, `MESSAGE`, and `COLOR` with your desired text and color.

For more badge options, visit [Shields.io](https://shields.io/).

## GitHub Achievements

GitHub Achievements are profile badges that GitHub awards to users based on their activities and contributions. Here's how to optimize your profile to earn these achievements:

### Available GitHub Achievements

1. **🏆 Starstruck**: Awarded when a repository you created gets 16 stars
2. **🔱 Quickdraw**: Awarded for closing an issue or PR within 5 minutes of opening
3. **⭐ Galaxy Brain**: Awarded for answering discussions
4. **📝 Pull Shark**: Awarded for having pull requests merged
5. **🌱 Pair Extraordinaire**: Awarded for co-authoring commits on merged pull requests
6. **🛠️ Public Sponsor**: Awarded for sponsoring open source work via GitHub Sponsors
7. **🔥 Arctic Code Vault Contributor**: Awarded for contributing code to repositories in the 2020 GitHub Archive Program
8. **🧠 YOLO**: Awarded for merging a pull request without code review
9. **👾 Mars 2020 Contributor**: Awarded for contributing to repositories used in the Mars 2020 Helicopter Mission

### How to Optimize for Achievements

1. **For Starstruck**:
   - Use this tool to create a realistic commit history
   - Create valuable repositories that others will want to star
   - Share your repositories on social media and developer communities

2. **For Pull Shark**:
   - Contribute to open source projects regularly
   - Submit quality pull requests that are likely to be merged

3. **For Pair Extraordinaire**:
   - Use co-authoring in your commits with the format:
     ```
     Co-authored-by: NAME <EMAIL>
     ```
   - Collaborate with others on projects

4. **For Quickdraw**:
   - Be active in your repositories
   - Respond quickly to new issues

5. **For Galaxy Brain**:
   - Participate in GitHub Discussions
   - Answer questions in repositories that have Discussions enabled

### Using Git Light to Help Earn Achievements

This tool can help you build a consistent commit history, which is essential for showcasing your coding activity. A well-maintained GitHub profile with regular contributions can:

1. Make your profile more attractive to potential employers or collaborators
2. Increase the visibility of your repositories, helping you earn the Starstruck achievement
3. Demonstrate your commitment to coding and open source

Remember that GitHub Achievements are meant to recognize genuine contributions. While this tool helps create a realistic commit history, the best way to earn achievements is through authentic participation in the GitHub community.
