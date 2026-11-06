## E1 — Clone remotes and authentication

**Git remotes:**
```text
fork    git@github.com:LordAdonis07/lantern.git (fetch)
fork    git@github.com:LordAdonis07/lantern.git (push)
origin  git@github.com:kareemahmoud/lantern.git (fetch)
origin  git@github.com:kareemahmoud/lantern.git (push)
```

**SSH authentication:**
```text
Hi LordAdonis07! You've successfully authenticated, but GitHub does not provide shell access.
```

## E3 — Git object identity

Two consecutive first-parent commits on main:

**Older commit:**
```text
Commit: 97b027d443822363ae0535ee79491701266274cb
Tree: c9e57c325fc72b99c17fd8dd2a86e2d72ca298a7
```

**Newer commit:**
```text
Commit: 6c065226a70ee357056fc8680be459a533404d99
Tree: 36b106795b234401e3218847b24001e0895a0c91
```

**Changed file — lantern.py**
```text
Older: 8bc0aea0c6a9b934d0a6074052c697a30376df7a
Newer: b0a9db3451d88e0f43f669477fc5c28348a48761
```

**Unchanged file — tasks.py**
```text
Older: 10d35af0fe70a5d98f6e44f5511f8e2f4738aa15
Newer: 10d35af0fe70a5d98f6e44f5511f8e2f4738aa15
```

## E4 — History graph after R3 merges

```text
*   452f77a merge: combine JSON sorting and pretty formatting
|\  
| * 915ade4 feat(storage): format JSON with indentation
* | 75dd359 fix(storage): sort JSON keys
|/  
*   1391532 Merge branch 'main' of github.com:kareemahmoud/lantern
|\  
| * b6e7882 chore(config): add local environment settings
| *   d3f7004 merge: combine done flag with strip fix
| |\  
| | * 6f4ed1b feat(tasks): add done flag to new tasks
| * | d2e66af fix(tasks): strip whitespace from task title
| |/  
| * 13dbdbd docs(notes): add first project notes
| * 557ea85 refactor(notes): rename draft.txt to notes.txt
| * 8d6c6a1 chore(notes): add draft placeholder file
```

## E5(b) — Reflog evidence

```text
85cd5ef main@{6}: reset: moving to origin/main
cca24fe (docs/usage-heading) main@{5}: merge docs/usage-heading: Fast-forward
cca24fe (docs/usage-heading) main@{7}: commit: docs: add development notes heading
85cd5ef main@{8}: commit: chore: ignore generated and temporary files
```

## E6 — Stash evidence

```text
stash@{0}: On feature/list-sort: WIP: add list sort argument
```