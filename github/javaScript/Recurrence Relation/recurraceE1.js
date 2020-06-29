function recurrence(number) {
    if(number > 0 ) {
        console.log(`This is Number ${number}`);
        recurrence(number - 1 );
    }
}

const number = 10;
recurrence(number)


/* 
If we pass number as N then it'll make N+1 call total, and Print Executes for N time
So Complexity = O(n)

Recurrence Relation -> T(n)= T(n-1) + 1
*/