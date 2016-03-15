If you commit a file > 100M into your local repo you will be unable to push to GitHub.  This is because GitHub has a 100MB per file limit.  Therefore it will reject the push to Github but will remain in your local git commits. 

Even if you delete or move the > 100M file out of your local repo and commit you still will not be able to push to Github.  Why?  The > 100MB file is still in the local repo commit history and so to keep the history and earlier versions synched your local repository.  Why?  Because there is a version of the file stored as part of the file history of commits in your local repo just like every version of any file is saved in your local repo after commits.

To enable a push to Github you will have to clean out any record of the > 100MB file in the local repo commit history as well as removing the actual file from your local repo folders.  To do this use a tool such as BFG which is specifically designed to solve this problem and clean out the reference to > 100MB files from your local repo's commit history.

[BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)

JIm
