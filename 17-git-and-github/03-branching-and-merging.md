# Branching and Merging

## Learning Objectives
By the end of this lesson you can:
- Explain why branches let you work on changes safely, in isolation
- Create and switch branches with `git branch` and `git switch`/`git checkout`
- Combine a branch's changes back into another branch with `git merge`
- Recognize (and know how to resolve) a simple merge conflict

## Concept Explanation

A **branch** is an independent line of development — a way to try
something (a new feature, an experiment, a risky change) without touching
your main, working codebase until you're confident it's ready.

Every Git repository starts with one branch, conventionally called `main`.
When you want to work on something new, you create a new branch from
`main`, make your commits there, and once you're happy, **merge** it back
into `main` — combining the two histories.

```
main:      A---B---C-------F
                    \       /
feature:             D---E
```
Here, commits `D` and `E` happened on a separate `feature` branch. `F` is
the merge commit that brings those changes back into `main`.

## Syntax

```
git branch                       # list branches, show current one
git branch <name>                # create a new branch (doesn't switch to it)
git switch <name>                # switch to an existing branch
git switch -c <name>              # create AND switch to a new branch in one step
git checkout <name>                # older equivalent of `git switch`

git merge <branch-name>            # merge another branch into your CURRENT branch
```

## Examples

**Example 1 — Creating and switching to a new branch**
```
$ git branch
* main
$ git switch -c add-login-feature
Switched to a new branch 'add-login-feature'
$ git branch
* add-login-feature
  main
```

**Example 2 — Making commits on a branch**
```
$ echo "def login(): pass" > login.py
$ git add login.py
$ git commit -m "Add login function stub"
[add-login-feature 3f4a5b6] Add login function stub
 1 file changed, 1 insertion(+)
 create mode 100644 login.py
```

**Example 3 — Merging the branch back into `main`**
```
$ git switch main
Switched to branch 'main'
$ git merge add-login-feature
Updating a1b2c3d..3f4a5b6
Fast-forward
 login.py | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 login.py
```
This particular merge was a "fast-forward" — `main` hadn't changed since
the branch split off, so Git simply moved `main`'s pointer forward.

**Example 4 — A merge conflict (when both branches changed the same lines)**
```
$ git merge add-login-feature
Auto-merging login.py
CONFLICT (content): Merge conflict in login.py
Automatic merge failed; fix conflicts and then commit the result.
```
Git marks the conflicting section directly inside the file:
```python
<<<<<<< HEAD
def login():
    print("Logging in (main version)")
=======
def login():
    print("Logging in (feature version)")
>>>>>>> add-login-feature
```
You manually edit the file to keep the correct version (or a combination),
remove the `<<<<<<<`/`=======`/`>>>>>>>` markers, then:
```
$ git add login.py
$ git commit -m "Resolve merge conflict in login.py"
```

## Common Mistakes

- **Making all your changes directly on `main`** — this defeats the
  purpose of branches. Get comfortable creating a branch for anything
  beyond a trivial fix.
- **Panicking at a merge conflict.** It just means Git needs your help
  deciding between two changes to the same lines — it isn't broken; open
  the file, choose/combine the correct version, remove the conflict
  markers, then `add` and `commit`.
- **Forgetting which branch you're on** before making changes — run
  `git branch` (or `git status`, which also shows the current branch) if
  you're ever unsure.
- **Not deleting old, merged branches** — once merged, a branch can be
  deleted (`git branch -d <name>`) to keep things tidy; the commits remain
  in history either way.

## Practice

1. Create a new branch, switch to it, and confirm with `git branch` that
   you're now on it.
2. Make a commit on that branch, then switch back to `main` and confirm
   (e.g. by listing files) that the change isn't there yet.
3. Merge your branch into `main` and confirm the change now appears.
4. Deliberately create a merge conflict (edit the same line of the same
   file differently on two branches) and practice resolving it.

## Challenge

Create two branches from `main`, each modifying a *different* part of the
same file, and merge both back into `main` one after another — the first
merge should be conflict-free, and (depending on what you changed) the
second might or might not conflict. Explain in a comment why.

## Mini Project

No dedicated mini project — practicing the Challenge above thoroughly is
this lesson's hands-on application.

## Summary

Branches let you develop changes in isolation from your main codebase;
`git switch -c <name>` creates and moves to a new one, and `git merge
<name>` (run from the branch you want to update) combines another
branch's history into it. A merge conflict simply means Git needs you to
manually decide how to combine two competing changes to the same lines.

## Next Step

Continue to [`04-github-workflow.md`](04-github-workflow.md).
