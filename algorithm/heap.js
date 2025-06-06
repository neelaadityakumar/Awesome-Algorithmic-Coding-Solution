class PriorityQueue {
  constructor(compare = (a, b) => a - b) {
    this.compare = compare; // if a > b means b is higher priority (lower number has higher priority)
    this.heap = [];
  }

  size() {
    return this.heap.length;
  }

  peek() {
    if (this.size() === 0) return undefined;
    return this.heap[0];
  }

  add(element) {
    this.heap.push(element);
    this._heapifyUp(this.size() - 1);
  }

  poll() {
    if (this.size() === 0) return undefined;
    if (this.size() === 1) return this.heap.pop();

    this._swap(0, this.size() - 1);
    const removed = this.heap.pop();
    this._heapifyDown(0);
    return removed;
  }

  //Extra methods for convenience
  isEmpty() {
    return this.size() === 0;
  }
  enqueue(element) {
    this.add(element);
  }
  dequeue() {
    return this.poll();
  }

  // === Internal Methods (Private by Convention) ===

  _heapifyUp(index) {
    if (index === 0) {
      return;
    }
    const parentIdx = this._parent(index);
    if (this.compare(this.heap[parentIdx], this.heap[index])) {
      this._swap(parentIdx, index);
      this._heapifyUp(parentIdx);
    }
  }

  _heapifyDown(index) {
    const childIdx = this._getHigherPriorityChild(index); // child index with which we need to swap
    if (index !== childIdx) {
      this._swap(index, childIdx);
      this._heapifyDown(childIdx);
    }
  }

  _getHigherPriorityChild(index) {
    let left = this._leftChild(index);
    let right = this._rightChild(index);
    if (
      left < this.heap.length &&
      this.compare(this.heap[index], this.heap[left])
    ) {
      index = left;
    }
    if (
      right < this.heap.length &&
      this.compare(this.heap[index], this.heap[right])
    ) {
      index = right;
    }
    return index;
  }

  _leftChild(index) {
    return index * 2 + 1;
  }

  _rightChild(index) {
    return index * 2 + 2;
  }

  _parent(index) {
    return Math.floor((index - 1) / 2);
  }

  _swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }
}

class MinPriorityQueue extends PriorityQueue {
  constructor() {
    super((a, b) => a - b);
  }
}
class MaxPriorityQueue extends PriorityQueue {
  constructor() {
    super((a, b) => b - a);
  }
}
export { MinPriorityQueue, MaxPriorityQueue, PriorityQueue };
