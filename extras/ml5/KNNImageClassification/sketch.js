// documentation on ml5 library
// https://ml5js.github.io/docs/knnImage.html

let video;
let knn;
let buttonA;

function setup(){
  video = createCapture(video).parent('videoContainer');
  // create knn image classifer
  // KNNImageClassifier(callback, ?numClasses, ?knnKValue, ?video)
  knn = new ml5.KNNImageClassifier(2, 1, modelLoaded, video.elt);
  // create callback functions for buttons
  CreateButtons();
}

function CreateButtons(){
  // connect to p5 html
  buttonA = select('#buttonA');
  // append function to button A
  buttonA.mousePressed(() => {
    train(1);
  });

  buttonB = select('#buttonB');
  buttonB.mousePressed(() => {
    train(2);
  });

  predictButton = select('#buttonPredict');
  predictButton.mousePressed(predict);

    save = select('#save');
  save.mousePressed(function() {
    knn.save('test');
  });

 load = select('#load');
 load.mousePressed(function() {
    knn.load('KNN-preload.json', updateExampleCounts);
  });


}

// Train the Classifier on a frame from the video.
function train(category) {
  let msg;
  if (category == 1) {
    msg = 'A';
  } else if (category == 2) {
    msg = 'B';
  }
  select('#training').html(msg);
  knn.addImageFromVideo(category);
  updateExampleCounts();
}

function predict(){
  console.log('predict');
  knn.predictFromVideo(gotResults);
}

function gotResults(results){
  console.log('got results');

}

function train(category){
    console.log('trained', category)
    knn.addImageFromVideo(category)
}

//define knnimage callback function
function modelLoaded(){
  console.log('model loaded :) ')
}