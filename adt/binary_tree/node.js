function Node(val){
  this.value = val;
  this.left = null;
  this.right = null;

}
// The JavaScript prototype property allows you to add new properties to object constructors:
// The JavaScript prototype property also allows you to add new methods to objects constructors:
Node.prototype.visit = function(){
  if (this.left != null){
    this.left.visit();
  }
    console.log(this.value)
  if (this.right != null){
      this.right.visit();
  }
}

Node.prototype.AddNode = function(n){
  if (n.value < this.value){
    if (this.left == null){
      this.left = n;
  }else{
    this.left.AddNode(n);
    }

  }else if (n.value > this.value){
    if (this.right == null){
      this.right = n;
    }else{
      this.right.AddNode(n);
    }
  }
}
