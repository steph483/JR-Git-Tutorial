# GitHub Tutorial
Stephanie Enriquez Isais
COMP 390 Junior Seminar

## Introduction
<!--- Introduce Git Hub and the most used commands like 
- git status
- benefits of git 
- maybe talk about about git commit graph --->
Welcome to this tutorial on how to use GitHub through the command line. We will be cloning a repository (repo), creating a branch, stashing, committing, pushing and merging branches together. GitHub is a version control system that allows you to collaborate with others on projects. Git Bash is an application that allows you to use GitHub through the command line. This tutorial assumes you have [downloaded Git Bash](https://git-scm.com/) and have connected it to your [GitHub account](https://github.com/).  


## Tutorial
Imagine that you are having some friends over and would like to play a game of Mad Libs. You find a project someone else has made on GitHub but want to customize it to fit the experiences you have shared with your friends.


---

*Note: Throughout this tutorial, one of the most used commands used in the command line on Git Bash is `$ git status`. This allows you to see where your files are being stored. Try this out by typing `$ git status` in the command line. It should output*
```fatal: not a git repository (or any of the parent directories): .git```

*This is because we still have not added any repos to the folder.*

---

#### Cloning a Repository
To begin the cloning process, first make a folder on your computer in which you would like to keep the MadLibs file. Open GitBash on this folder. 

To clone the repo into the folder, you will first need to get URL of the repo you want to clone. To do this, go to the [repo's page](https://github.com/steph483/MadLibs.git) on GitHub. Then select the green *Code* button and copy the HTTPS link.


<img src="/Images/GH-Code-SS.PNG" width="300">

In the Git Bash terminal, use the command `$ git clone <Repo URL>` to finish the cloning process. You should get the following message. 

<img src="/Images/GH-clone_done-SS.PNG" width="500">

You can also verify that the repo was correctly cloned by making sure that it appears in the folder. In Git Bash, move into the repo you just cloned by using the command `$ cd MadLibs/`. 


#### Creating a new Branch
<!--- This is so they can add a new "feature", for my example
I think it'll just be a  new option for the madlibs --->
Now that you have a the MadLibs project on your computer, it's time to make it your own. Branches in GitHub are very useful when it comes to making a new feature. In a use case in which you are working with others on the same project, creating a new branch can help isolate your work and merge it back when it is ready. It also helps to test feature before incorporating them into the main branch. In the case of this project, a new branch could be made to add a new subject to the options of MadLibs that fits better with your friends.

The first step to creating a new branch is using the command `$ git branch <new branch name>`. In this case, lets call that new branch *4friends*. Although you created a new branch, you are still on the *main* branch, to move to the new branch use the command `$ git checkout <new branch name>`. The command should output the following:

<img src="/Images/GH-new_branch-SS.PNG" width="500">

You can also tell what branch you are on by looking at the end of the location path. The blue branch name in parentheses tells you what branch you are currently on.

---

Note: The process of creating a new branch and switching to it can simplified into one command `$ git checkout -b <new branch name>`. The *-b* in this case is creating a new branch to switch to. 

Note: When creating more than one branch it can be hard to remember all the branches tou have, use the command `$ git branch` to see all the branches currently in that repository. 

<img src="/Images/GH-branches-SS.PNG" width="100">

This also shows you what branch you are currently on with the use of the asterisk *. 

---

##### Making Changes to the file
<!--- This is so that they can safely store their work while
they are checking out to another branch (going back to the main branch and want to stash away their past)--->

Now let's say that you have started to work on your new branch, *4friends*. Since this is in a new branch you can make any changes you would like without the worry of affecting the original files. For the purpose of the tutorial lets say you would like to change the sad category into something about about the pets of your friends. 

Change the all the *sad* words to *pet* on the Mad_Libs.py file. This is so that we can reuse the sad function but change the output it prints. Also, in the print statement of the variable called `user_animal`, change it to say `user_animal = input("Choose one of our friend's pet: ")`. Finally, in the new `pet()` function, use the *user_animal, user_location, user_verb* variables to make a sentence that talks about your freind's pet. Make sure you keep the print output in the same format `print("<text> {} <text>".format())`. Save these changes on your Mad_Libs.py file. 


#### Stashing your work
Just like when working on any project, there are times you need to take a break and work on something else. For the purpose of this tutorial, lets say you decide to work on the main brain for a bit. In the case you want to save your changes without committing, you can stash them away. 

The first step to stashing is to go back to the command line and enter the command `$ git stash`. If you look at the file, it will have changed it back to what it was before your edits, this is because the changes you've made have been stashed so you can safely move onto other branches. 

If you use the `$ git status` command, it'll output: 

<img src="/Images/GH-stashing-SS.PNG" width="300">

This is because all of the changes you've made have been stashed away.

#### Making Commits
Lets got back to the main branch using the `$ git checkout main` command. 

Back on the main branch you can open up the Mad_Libs.py again and add a *if* statement that gives the user the option to play the MadLibs again. Below is a piece of sample code that can be added to the end of the main function on the Mad_Libs.py to give the user that option. Test it to see how it works.

```
 play_again = input("Thanks for playing. Want to play again? (y/n) ")
    if play_again == 'y':
        main()
    else:
        print("bye")
```
Since you are sure about the edits that you've made, you can commit that file on the main branch to the your local repository.


##### Staging your work
The first step to committing work is to stage your files. This is done so that you can move the files you have edited from the working directory to the staging area. The purpose of the staging area is to have all the files relevant to a certain feature or topic be in the same commit. To do this, use the add command along with the name of the file, `$ git add <file name>`. If you were to have more that one file to stage, use `$ git add .` to add of them at the same time.

Check that you file has been added by using the `$ git status` command. It should output the following:

<img src="/Images/GH-gitadd-SS.PNG" width="400">

This lets you see all the files (in green) that are ready to be committed.

---
Note: To remove a file from the staged area, use the `$ git restore --staged <file>` command. 

---


##### Committing your work
<!--- ADD SOMETHING ABOUT REVERTING BACK TO PREVIOUS COMMIT --->
Now that your file has been staged, it is time to make a commit. By committing something you are taking it from the staging area to the local repository on your computer. This can be done as many times as you'd like but it is important to be meaningful about the work you are committing so it is easier and more useful to look back at previous commits.

To commit your staged files, simply write `$ git commit -m "<Message>"`. The purpose of adding the *-m* is to add a message tied to the commit that helps you remember what the commit was about when you look back at all the commits in the future. The output of this should be the following:

<img src="/Images/GH-commit message-SS.PNG" width="400">

The output confirms that your commit has been added, where it was added, the 7 character ID it has and how many changes were made. 

---
Note: Commits can be really useful when deciding to go back on a previous feature. This is where the version control aspect of Git Hub comes into play since you can go back to any commit needed. To see all the commits you have, use the command `$ git log`.

<img src="/Images/GH-log message-SS.PNG" width="400">

This will show you the full commit ID, the author, date, and commit message.

If you want to go back and look at the commit, simply type `git checkout <7 character ID>`. 

If you want to continue working from a specific past commit, you can do so by creating a new branch and switching back using the command `git checkout -b <Branch Name> <7 character ID>`. This takes you to the old commit and starts a new branch from there. 

---

#### Applying your stashes
Lets go back to the stashes made on the *4friends* branch and restore them. This should be done when you want to see the stashes made and are ready to commit to the changes stashed away. Use the `$ git checkout` to go back to the *4friends* branch. 

To see a all of the stashes, use the command `$ git stash list`. In the future you might have more than one to choose from but for this tutorial, there is only one to restore. 

There are two ways to restore the changes, one is to the use the `$ git stash apply <stash ID>`. This will reapply the changes made to the file but it will not remove the stash from the list of stashes. To reapply the changes and remove the top stash from list of stashes, use the command `$ git stash pop`. This will apply the changes from only the first stash listed and remove that stash. It should output the following:

<img src="/Images/GH-stash restore-SS.PNG" width="500">

After reapplying the one stash, make sure the changes were made by looking back at your Mad_Libs.py file. 

Since we are happy with the changes made, we can commit these changes using the same steps previously listed. 

---
Note: Although this was a simple example of stashing, you can image how useful it could be where there are multiple versions of changes you are considering. It is also a less formal way of saving these changes compared to committing.

---

#### Merging 
Now that you are happy with both the *main* and *4friends* branches and have committed all your changes to your local repository, it is time to merge them together. The purpose of merging things together is to incorporate all the new changes from both versions of the file into one. Merging is also a non-destructive combination that creates a new commit from both the files instead of rewriting over one. 

To begin the merge lets make sure we are on the *main* branch and then use the command `$ git merge 4friends`. This merges the *4friends* branch into the *main* branch. You should get the following message: 

<img src="/Images/GH-git merge-SS.PNG" width="400">

You could also merge the *main* branch into the *4friends* branch but for our case we want to keep the changes on the main branch. 

If you look at the Mad_Libs.py file now, it should have all of the new changes implemented. 

---
Note: There are cases in which you are merging files that can cause some sort of merge conflict since Git cannot decide which change to keep. In those cases, you would have to manually edit the file with all versions that caused the conflict and choose which one you would like to keep. 

For example: You could receive a merge conflict for conflicting lines, 
```
CONFLICT: Merge conflict in <file name>
Automatic merge conflict failed; fix conflicts and then commit the result.
```
To fix this, you would opened the file and see that it pointed out the conflicts in a format similar to the following:
```
<<<<< HEAD
    *version 1 of code*
===== 
    *version 2 of code*
>>>>> *Branch Name*
```

In this case, you would choose which version to keep and delete everything else, including the <<< Head, === and >>>. 

[Here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts) is a link with more specifics on how to fix this.

---

Congratulations! You have officially learned the basics of Github. 

## Future Work
The following techniques are not relevant to our use case of cloning a repo from Git Hub but they are essential in learning to use github, especially when it comes to creating and uploading your own work.

#### Making your own repository
When you decide to upload your own projects on GitHub, the first thing you will need to do is create a new folder in which you will put all the files relevant to your project. Once you have done that, open Git Bash in that folder. 


We start by initializing our local directory (folder) as a repository with a main branch by using the command `$ git init -b main`. You can make sure your local repository was created by using the `$ git status` command. It should output the following. 

<!--- FIX ME ADD NEW SCREENSHOT --->
<img src="/Images/GH-newrepo-SS.PNG" width="500">

This screenshot shows untracked files because there are files relevant to the repository that still haven't been staged. 

From here on out, you can follow the same steps for adding, committing, branches, stashing and merging as if you has cloned the repository from Git Hub as the steps above have shown.

#### Pushing your work to your GitHub
Although committing is a useful way of storing different versions of your work, it is also important to keep versions of that somewhere else, like GitHub, in case something happens to your computer. By pushing your commits into a remote repository on GitHub, you are able to store your files in a safe cloud based source code management system that you can access and clone at any time.

In addition to that, there are also times in which you need to collaborate with other on projects. By having a system like GitHub that stores, creates branches and can merge files together, you are able to easily share and combine your work with others through the use of a common repository.

All of this can be done through the use of pushing your work into the remote repository on GitHub. 

To do that you will need to make sure your local tree is clean and working well with all the commits in it, this can be found by using the `$ git status` command.

Once you have verified that, you can use the command `$ git remote add origin <remote repo URL>` to add your local to the remote one. Then, use `git push -u origin master` to push it all the way through to the remote repository on github. After pushing your file, you might get asked to login to Github. Check your files have been correctly pushed by seeing if they are on the Git Hub remote repo you wanted.


## Conclusion
<!--- Briefly summarize and introduce other options like rebasing --->
The purpose of this tutorial was to help you become more comfortable with using GitHub through the command line. We learned how to clone a repo, create your own repo, create a new branch, stash changes, commit files, merge and even how to upload it all to GitHub. Although this tutorial mainly focused on the basics of GitHub, it gives you a great foundation to grown on.

In addition, if you ever forget one of the commands, use `$ git help` in the command line to receive a list of commands and how they can be used.


## References
- https://docs.github.com/en
- https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud 
- https://git-scm.com/book/en/v2 

