/* Binary Search: Search a sorted array by repeatedly dividing the search interval in half. 
Begin with an interval covering the whole array. If the value of the search key is less 
than the item in the middle of the interval, narrow the interval to the lower half. 
Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

if we find value then we're going to return the index of that target


pseudo code

1. Divide the list of num by 2 until the start index >= lastIndex
2. check it's the target ? 
    if yes 
        return
    else if middle value < target 
        return right portion of the array
    else
        return left portion of the array
3. follow same process until we found the target value

*/


function DoBinarySearch(ListOfNumbers, target) {
    const midIndex = Math.round(ListOfNumbers.length / 2);
    return RecursionSearch(ListOfNumbers, 0, ListOfNumbers.length, target, midIndex);
}

function RecursionSearch(ListOfNumbers, initialIndex, lastIndex, target, midIndex) {
    console.log(`searching from ${midIndex} <-> ${lastIndex}`);
    if(ListOfNumbers[midIndex] === target ) {
        return midIndex;
    }

    if(midIndex >= lastIndex) {
        return null
    }

    return ListOfNumbers[midIndex] < target ? 
        RecursionSearch(ListOfNumbers, midIndex, lastIndex,target, Math.round( (midIndex + lastIndex) / 2) ) :
        RecursionSearch(ListOfNumbers, 0, midIndex, target, Math.round(midIndex / 2) - 1);
}


const listOfNum = [1,2,3,4,5,6,7,8,9,10, 11,12,13,14,15,16,17,18, 19, 20];
const target = 11;
const searchResult = DoBinarySearch(listOfNum, target);
console.log(`This is the Ans -> ${searchResult}`);



