const points = [];
const point_capacity = 5000;
let qtree;
let count = 0;

class Rectangle {
  constructor(x,y,w,h) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
  }

  contains(point) {
    return (point.x >= this.x -this.w &&
      point.x <= this.x + this.w &&
      point.y >= this.y - this.h &&
      point.y <= this.y + this.h);
  }

  intersects(range) {
    return !(range.x - range.w > this.x + this.w ||
      range.x + range.w < this.x - this.w ||
      range.y - range.h > this.y + this.h ||
      range.y + range.h < this.y - this.h);
  }

}

function setup() {
  createCanvas(1024,800);
  for (let i=0;i<point_capacity;i++) {
    // points.push(new Point(randomGaussian(width / 2, width / 8), randomGaussian(height / 2, height / 8)));
    points.push(new Point(random(width), random(height)));
  }
  qtree = new QuadTree(new Rectangle(0,0,width,height), 5);
  for (let point of points) {
    qtree.insert(point);
  }
}

function draw() {
  count = 0;
  background(50);
  qtree.show();

  let range = new Rectangle(mouseX,mouseY,250,160);
  stroke(10,250,0);
  rect(range.x,range.y,range.w * 2,range.h * 2);
  let found = qtree.query(range);

  console.log(found);
  console.log(count);

  stroke(10,250,0);
  strokeWeight(10);
  for (let p of found) {
    point(p.x,p.y);
  }
}
