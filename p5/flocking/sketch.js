const flocks = [];

function setup() {
  createCanvas(1024,800);
  for (let i=0;i<100;i++) {
    flocks.push(new Boid());
  }
}

function draw() {
  background(50);
  for (let i=0;i<flocks.length;i++) {
    flocks[i].update();
    flocks[i].show()
  }
}
