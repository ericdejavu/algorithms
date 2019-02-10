class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
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

class QuadTree {
  constructor(boundary, n) {
    this.boundary = boundary;
    this.capacity = n;
    this.points = [];
    this.divide = false;
  }

  subdivide() {
    let x = this.boundary.x;
    let y = this.boundary.y;
    let w = this.boundary.w;
    let h = this.boundary.h;
    let ne_boundary = new Rectangle(x + w / 2, y - h / 2, w / 2, h / 2);
    this.ne = new QuadTree(ne_boundary, this.capacity);
    let nw_boundary = new Rectangle(x - w / 2, y - h / 2, w / 2, h / 2);
    this.nw = new QuadTree(nw_boundary, this.capacity);
    let se_boundary = new Rectangle(x + w / 2, y + h / 2, w / 2, h / 2);
    this.se = new QuadTree(se_boundary, this.capacity);
    let sw_boundary = new Rectangle(x - w / 2, y + h / 2, w / 2, h / 2);
    this.sw = new QuadTree(sw_boundary, this.capacity);
    this.divide = true;
  }

  insert(point) {
    if (!this.boundary.contains(point)) {
      return false;
    }
    if (this.points.length < this.capacity) {
      this.points.push(point);
      return true;
    } else {
      if (!this.divide) {
        this.subdivide();
      }

      if (this.ne.insert(point)) return true;
      else if (this.nw.insert(point)) return true;
      else if (this.se.insert(point)) return true;
      else if (this.sw.insert(point)) return true;
    }
  }

  query(range, found) {
    if (!found) {
      found = [];
    }
    if (!this.boundary.intersects(range)) {
      return;
    } else {
      for (let p of this.points) {
        count ++;
        if (range.contains(p)) {
          found.push(p);
        }
      }
      if (this.divide) {
        this.ne.query(range, found);
        this.nw.query(range, found);
        this.se.query(range, found);
        this.sw.query(range, found);
      }
    }
    return found;
  }

  show() {
    stroke(255);
    strokeWeight(1);
    noFill();
    rectMode(CENTER);
    rect(this.boundary.x, this.boundary.y, this.boundary.w*2, this.boundary.h*2);
    if (this.divide) {
      this.ne.show();
      this.nw.show();
      this.se.show();
      this.sw.show();
    }
    stroke(120);
    strokeWeight(4);
    for (let p of this.points) {
      point(p.x,p.y);
    }
  }
}
