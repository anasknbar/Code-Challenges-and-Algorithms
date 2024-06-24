### challenge-1

Given:
- `preorder = [3, 9, 20, 15, 7]`
- `inorder = [9, 3, 15, 20, 7]`

Construct the binary tree:

```
     3
    / \
   9  20
     /  \
    15   7
```

### Steps to Construct the Tree

1. **Identify the Root**: 
   - The first element of `preorder` (`3`) is the root of the tree.

2. **Divide the Inorder List**:
   - Find the root (`3`) in the `inorder` list.
   - Elements left of the root in `inorder` (`9`) are in the left subtree.
   - Elements right of the root in `inorder` (`15, 20, 7`) are in the right subtree.

3. **Recursively Construct Subtrees**:
   - Apply steps 1 and 2 recursively to build the left and right subtrees.

### Graphical Representation

- **Step 1**: Identify the Root (`3`)

```
     3
```

- **Step 2**: Divide the Inorder List

```
     3
    / \
```

- **Step 3**: Recursively Build Subtrees

  - Left Subtree (`9`)
  
  ```
     3
    / \
   9
  ```

  - Right Subtree (`20, 15, 7`)

  ```
     3
    / \
   9  20
     /  \
    15   7
  ```



