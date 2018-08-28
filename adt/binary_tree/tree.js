// https://www.youtube.com/watch?v=ZNH0MuQ51m4
// http://cslibrary.stanford.edu/110/BinaryTrees.html
// what is a data structure?
// what is the basic idea of a binary tree's structure
// What is a node
// What is the root of a trees
// what is a child
// how are binary trees sorted
// how do you build a tree
// create pseduo code for printing out a sorted binary tree

function Tree(){
  this.root = null;
}

Tree.prototype.traverse = function(){
  this.root.visit();
}

Tree.prototype.addValue = function(val){
  var n = new Node(val);
  if (this.root == null){
    this.root = n;
  } else {
    this.root.AddNode(n);
  }
}
