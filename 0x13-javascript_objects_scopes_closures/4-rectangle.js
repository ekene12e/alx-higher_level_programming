#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (h > 0 && w > 0) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
    rotate() {
      let temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  }
module.exports = Rectangle;
