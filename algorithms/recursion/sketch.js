// https://www.youtube.com/watch?v=jPsZwrV9ld0
// what is recursion
// how does it work
// why use it?
// how do you setup an exit condition?
// why not just use a loop?
// how is the data from recursion saved?
// what are some costs of recursion?
// can you mathematically or artistically represent recursion?

function setup(){
  createCanvas(600, 600);

}

function draw(){
  background(0);
  stroke(255);
  noFill();
  drawCircle(300,200,300)
}

function drawCircle(x,y,d){
  ellipse(x, y, d);
  if (d > 2){
    drawCircle(x + d * 0.5, y, d * 0.5);
    drawCircle(x - d * 0.5, y, d * 0.5);
    drawCircle(x, y + d * 0.5, d * 0.5);

  }
}
