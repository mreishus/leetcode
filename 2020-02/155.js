#!/usr/bin/env node

/**
 * initialize your data structure here.
 */
var MinStack = function() {
  this.items = [];
};

/**
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
  let newMin = x;
  if (this.items.length > 0) {
    let currentMin = this.getMin();
    if (currentMin < newMin) {
      newMin = currentMin;
    }
  }
  let newItem = [x, newMin];
  this.items.push(newItem);
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
  this.items.pop();
  return null;
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
  if (this.items.length == 0) {
    return null;
  }
  let lastItem = this.items[this.items.length - 1];
  let [x, min] = lastItem;
  return x;
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
  if (this.items.length == 0) {
    return null;
  }
  let lastItem = this.items[this.items.length - 1];
  let [x, min] = lastItem;
  return min;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */

var obj = new MinStack();
obj.push(-2);
obj.push(0);
obj.push(-3);
console.log("Expect -3");
console.log(obj.getMin());
obj.pop();
console.log(obj.getMin());
