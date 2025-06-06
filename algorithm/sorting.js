//Merge Sort
//divide sort then merge //need extra space but efficient.
// Merge Sort
function mergeSort(arr) {
  if (arr.length <= 1) return arr;

  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));

  return merge(left, right);
}

function merge(left, right) {
  let result = [];
  let l = 0;
  let r = 0;

  while (l < left.length && r < right.length) {
    if (left[l] < right[r]) {
      result.push(left[l]);
      l++;
    } else {
      result.push(right[r]);
      r++;
    }
  }

  return result.concat(left.slice(l)).concat(right.slice(r));
}
// Quick Sort
//
function swap(items, leftIndex, rightIndex) {
  var temp = items[leftIndex];
  items[leftIndex] = items[rightIndex];
  items[rightIndex] = temp;
}
function partition(items, left, right) {
  var pivot = items[Math.floor((right + left) / 2)], //middle element
    i = left, //left pointer
    j = right; //right pointer
  while (i <= j) {
    //if odd length mid can be missed
    while (items[i] < pivot) {
      i++;
    }
    while (items[j] > pivot) {
      j--;
    }
    if (i <= j) {
      swap(items, i, j); //sawpping two elements
      i++;
      j--;
    }
  }
  return i;
}

function quickSort(items, left, right) {
  var index;
  if (items.length > 1) {
    index = partition(items, left, right); //index returned from partition
    if (left < index - 1) {
      //more elements on the left side of the pivot
      quickSort(items, left, index - 1);
    }
    if (index < right) {
      //more elements on the right side of the pivot
      quickSort(items, index, right);
    }
  }
  return items;
}

// Selection Sort
//find smallest number swap with first & repeat

function selectionSort(arr) {
  for (let i = 0; i < arr.length - 1; i++) {
    let minIndex = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[minIndex]) {
        minIndex = j;
      }
    }
    if (minIndex !== i) {
      [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
    }
  }
  return arr;
}
// Insertion Sort
//good if almost sorted
// if curr number is smaller than prev then move all greter next to it
//sorted from left to right, s->big
function insertionSort(arr) {
  // Iterate through the array starting from the second element
  for (let i = 1; i < arr.length; i++) {
    // Store the current value to be inserted
    let currentValue = arr[i];
    // Initialize a pointer to the element before the current one
    let j = i - 1;
    // Move elements of arr[0..i-1], that are greater than currentValue,
    // to one position ahead of their current position
    while (j >= 0 && arr[j] > currentValue) {
      arr[j + 1] = arr[j];
      j--;
    }
    // Place the currentValue in its correct position
    arr[j + 1] = currentValue;
  }
  // Return the sorted array
  return arr;
}
// Bubble Sort
//compare adjacent element if not in order swap values..
// at each iteration biggest number goes to the right
function bubbleSort(arr) {
  // Variable to track if any swaps were made in the current iteration
  let swapped;
  // Repeat until no more swaps are made
  for (let i = 0; i < arr.length - 1; i++) {
    swapped = false;
    // Iterate through the array up to the second-to-last element
    for (let j = 0; j < arr.length - i - 1; j++) {
      // If the current element is greater than the next element, swap them
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        // Set swapped to true to indicate that a swap was made
        swapped = true;
      }
    }
    // If no swaps were made in the iteration, the array is already sorted
    if (!swapped) {
      break;
    }
  }
  // Return the sorted array
  return arr;
}
const items = [6, 3, 5, 2, 9, 7];
console.log(quickSort(items, 0, items.length - 1));

console.log(mergeSort(items));
