var grids = [];
var grids_colors = []
var _rows = 4;
var _cols = 4;

var _width = 50;

var ordered = []

var isRunning = true


function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}

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


function fill_red(x, y) {
  let range = grids[y][x];
  ordered.push([range, 'r', x, y]);
}

function fill_green(x, y) {
  let range = grids[y][x];
  ordered.push([range, 'g', x, y]);
}


function dfs(x, y) {
  
  if (y+1 < _rows) {
    fill_red(x, y)
    dfs(x, y+1)
  }

  if (x+1 < _cols) {
    fill_red(x, y)
    dfs(x+1, y)
  }

  fill_green(x, y)
}

function setup() {
  createCanvas(1024,800);
  // frameRate(1);

  console.log(_rows, _cols)

  for (let i=0;i<_rows;i++) {
    var rows = [];
    var colors = [];
    for (let j=0;j<_cols;j++) {
      rows.push(new Rectangle(i*_width,j*_width,_width,_width));
      colors.push([0,0,0,0])
    }
    grids_colors.push(colors)
    grids.push(rows);
  }
  dfs(0, 0)
  ordered.reverse()
  console.log(ordered)
}

function draw() {
  count = 0;
  background(50);

  stroke(10,250,0);

  let currentx = 0;
  let currenty = 0;
  let currentc = 'r';

  if (ordered.length > 0) {
    let data = ordered.pop()
    currentx = data[2]
    currenty = data[3]
    if (data[1] === 'r') {
      currentc = 'r'
      var c = grids_colors[currenty][currentx];
      c[3] += 10
      c[0] = 200
    } else if (data[1] === 'g') {
      currentc = 'g'
      var c = grids_colors[currenty][currentx];
      c[3] += 10
      c[1] = 200
    }
  }
  for (var i=0;i<_rows;i++) {
    for (var j=0;j<_cols;j++) {
      let range = grids[i][j];
      if (currentx === j && currenty === i) {
        if (currentc === 'r') {
          fill(200, 0, 255)
        } else {
          fill(0, 200, 255)
        }
      } else {
        fill(grids_colors[i][j])
      }
      rect(range.x, range.y, range.w, range.h);
    }
  }

}
