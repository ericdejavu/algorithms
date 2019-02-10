class Boid {
	constructor() {
		this.postion = createVector(random(height), random(width));
		this.velocity = p5.Vector.random2D();
		this.accleration = createVector();
	}

	align(boids) {
		let perceptionRadius = 100;
		let steering = createVector();
		let total = 0;
		for (let other of boids) {
			let d = dist(this.postion.x, this.postion.y, other.postion.x, other.postion.y);
			if (other != this && d < perceptionRadius) {
				steering.add(other.velocity);
				total ++;
			}
		}
		if (total > 0) {
			steering.div(total);
			steering.sub(this.velocity);
		}
		return steering;
	}

	flock(boids) {
		let alignment = this.align(boids);
		this.acceleration = alignment;
	}

	edges() {
		if (this.postion.x > width) this.postion.x = 0;
		else if(this.postion.x < 0) this.postion.x = width;
		if (this.postion.y > width) this.postion.y = 0;
		else if(this.postion.y < 0) this.postion.y = height;
	}

	update() {
		this.postion.add(this.velocity);
		this.velocity.add(this.accleration);
		this.edges();
	}

	show() {
		strokeWeight(8);
		stroke(255);
		point(this.postion.x, this.postion.y);
	}
}
