// Goal - Perform linear search -> Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].

// Input : arr[] = [10,20,30,40,60,50,110,100,130,170]
// x = 60;
// Output : 4

function linearSearch(listOfArray, searchingElement) {
    for( let i = 0; i < listOfArray.length; i++ ) {
        if(listOfArray[i] === searchingElement ) {
            return i;
        }
    }
    return null;
}

const inputs = [10,20,30,40,60,50,110,100,130,170];
const searchElement = 60
const findSearchElement = linearSearch(inputs, searchElement);
console.log(findSearchElement);
