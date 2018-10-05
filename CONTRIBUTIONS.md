# How to Contribute to [Hacktober-at-GVP](https://github.com/gvp-ai-club/Hacktober-at-GVP)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

# First Contributions

It's hard. It's always hard the first time you do something. Especially when you are collaborating, making mistakes isn't a comfortable thing. We wanted to simplify the way new open-source contributors learn & contribute for the first time.

Reading articles & watching tutorials can help, but what's better than actually doing the stuff in a practice environment? This project aims at providing guidance & simplifying the way beginners make their first contribution. If you are looking to make your first contribution, follow the steps below.

#### *If you're not comfortable with command line, [here are tutorials using GUI tools.]( #tutorials-using-other-tools )*

If you don't have git on your machine, [install it]( https://help.github.com/articles/set-up-git/).

## Fork this repository

Fork this repo by clicking on the fork button on the top of this page.
This will create a copy of this repository in your account.

## Clone the repository

Now clone the forked repo to your machine. Go to your GitHub account, open the forked repo, click on the clone button and then click the *copy to clipboard* icon.

Open a terminal and run the following git command:

```
git clone https://github.com/{username}/Hacktober-at-GVP.git
```
where `{username}` is your GitHub username. Here you're copying the contents of the first-contributions repository in GitHub to your computer.

For example: 

```
git clone https://github.com/WierdMosquito123/Hacktober-at-GVP.git
```

## Create a branch

Change to the repository directory on your computer (if you are not already there):

```
cd Hacktober-at-GVP
```
Now create a branch using the `git checkout` command:
```
git checkout -b <new-branch-name>
```

For example:
```
git checkout -b add-WierdMosquito123
```
(The name of the branch does not need to have the word *add* in it, but it's a reasonable thing to include because the purpose of this branch is to add your name to a list.)

## Make necessary changes and commit those changes

Now open `Contributors.md` file in a text editor, add your name to it. Don't add it at the beginning or end of the file. Put it anywhere in between. Now, save the file. 


If you go to the project directory and execute the command `git status`, you'll see there are changes. 


Add those changes to the branch you just created using the `git add` command:

```
git add Contributors.md
```

Now commit those changes using the `git commit` command:
```
git commit -m "Add <your-name> to Contributors list"
```
replacing `<your-name>` with your name.

## Push changes to GitHub

Push your changes using the command `git push`:
```
git push origin <your-branch-name>
```
replacing `<your-branch-name>` with the name of the branch you created earlier.

## Submit your changes for review

If you go to your repository on GitHub, you'll see a  `Compare & pull request` button.  Click on that button.

Now submit the pull request.

Soon We will be merging all your changes into the master branch of this project. You will get a notification email once the changes have been merged.

## Where to go from here?

Congrats! You just completed the standard _fork -> clone -> edit -> PR_ workflow that you'll encounter often as a contributor!

## Self-Promotion

If you liked this project, star it on [GitHub](https://github.com/GVP-AI-Club/Hacktober-at-GVP).
Follow [GVP-AI-Club](https://gvp-ai-club.github.io/) on
[GitHub](https://github.com/GVP-AI-Club).
