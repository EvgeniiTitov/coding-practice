- When it comes to trees there always seems to be a recursive and an 
iterative solution.

- Sometimes you need to be able to get access two nodes from
the opposite subtrees (root.left and root.right) like in the
symmetric_tree problem. In this case, you need to start propagating
left and right simulatenously. In other cases, this is not required 
such as in the invert_binary_tree problem. Notice how these two 
approaches differ for both recursive and iterative solutions. 

- 