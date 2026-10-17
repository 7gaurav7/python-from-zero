# GitHub and Remote Workflow

## Learning Objectives
By the end of this lesson you can:
- Explain what a "remote" repository is
- Push local commits to GitHub and pull others' changes down
- Clone an existing GitHub repository to your computer
- Describe the basic pull-request collaboration workflow

## Concept Explanation

Everything in the previous two lessons happened entirely on your own
computer. A **remote** is a copy of your repository hosted somewhere else
— almost always GitHub in practice — that you and others can sync with.

The two core commands:
- `git push` — send your local commits *up* to the remote.
- `git pull` — bring the remote's commits *down* to your computer.

This is exactly how you likely got this very course:
`git clone <this-repo's-URL>` downloads a full copy of a remote repository,
including its entire history, onto your computer.

## Syntax

```
git clone <url>                              # download a full copy of a remote repo
git remote add origin <url>                    # connect a local repo to a remote (once)
git push origin main                          # push your local `main` branch to the remote
git push -u origin main                        # push AND remember this pairing for next time
git pull origin main                          # pull the remote's changes into your local branch

git remote -v                                  # list configured remotes
```

**The basic GitHub collaboration workflow ("pull request"):**
1. Push a feature branch to GitHub (`git push -u origin my-branch`).
2. On GitHub's website, open a **pull request** — a request to merge your
   branch into `main`, which teammates can review and comment on.
3. Once approved, the pull request is merged (often directly through
   GitHub's website), updating `main` on the remote.
4. Everyone else runs `git pull` to bring that update down to their own
   computer.

## Examples

**Example 1 — Cloning an existing repository**
```
$ git clone https://github.com/some-user/python-from-zero.git
Cloning into 'python-from-zero'...
remote: Enumerating objects: 124, done.
...
$ cd python-from-zero
$ git log --oneline -3
a1b2c3d Update README
9f8e7d6 Add final projects
1234567 Initial commit
```

**Example 2 — Connecting an existing local repo to a new GitHub repo**
```
$ git remote add origin https://github.com/your-username/my-project.git
$ git push -u origin main
Enumerating objects: 3, done.
...
To https://github.com/your-username/my-project.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

**Example 3 — The everyday push/pull cycle**
```
$ git add .
$ git commit -m "Add score tracking to quiz game"
$ git push
Enumerating objects: 5, done.
...
To https://github.com/your-username/my-project.git
   b2c3d4e..c3d4e5f  main -> main
```
And on another computer (or a teammate's):
```
$ git pull
Updating b2c3d4e..c3d4e5f
Fast-forward
 quiz_game.py | 4 ++++
 1 file changed, 4 insertions(+)
```

**Example 4 — Checking your remotes**
```
$ git remote -v
origin  https://github.com/your-username/my-project.git (fetch)
origin  https://github.com/your-username/my-project.git (push)
```

## Common Mistakes

- **Forgetting to `git pull` before starting new work**, especially on a
  shared project — this leads to unnecessary merge conflicts when your
  local history has fallen behind the remote's.
- **Pushing directly to `main` on a shared/team project** instead of using
  a feature branch and a pull request — fine solo, but disruptive on a
  team.
- **Confusing `git clone` (download a whole new repo) with `git pull`**
  (update a repo you already have locally) — you only clone once per
  project.
- **Committing sensitive data** (passwords, API keys) and pushing it to a
  public GitHub repository — treat anything pushed to a public remote as
  permanently public, even if you delete it in a later commit (see
  `18-real-world-python`'s environment variables lesson for the right way
  to handle secrets).

## Practice

1. Create a new, empty repository on GitHub's website, then connect a
   local practice repo to it using `git remote add origin <url>` and push
   your first commit.
2. Make a small change locally, commit it, and push again.
3. On GitHub's website, edit a file directly (GitHub lets you do this in
   the browser) to simulate a teammate's change, then `git pull` it down
   locally.
4. Clone a public repository you don't own (read-only) just to practice
   `git clone`.

## Challenge

Practice the full feature-branch workflow: create a branch, commit a
change, push the branch to GitHub (`git push -u origin your-branch-name`),
then open a pull request on GitHub's website comparing it to `main`
(even if you're merging your own pull request solo).

## Mini Project

Push one of your completed `19-projects` folders (from
`17-git-and-github`'s earlier mini project, where you ran `git init`
inside it) to a brand-new GitHub repository, so it's visible on your own
GitHub profile.

## Summary

A remote (typically GitHub) is a hosted copy of your repository you sync
with using `git push` (send commits up) and `git pull` (bring commits
down); `git clone` downloads an entire existing remote repository for the
first time. The pull-request workflow — branch, push, review, merge — is
how most real-world teams collaborate on shared code.

## Next Step

Continue to [`05-readme-basics.md`](05-readme-basics.md).
