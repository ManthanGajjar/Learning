function Test(number) { // for N time, called it as T(N)
    if(number > 0) { // for 1 time
        for(let i = 0; i < number; i++ ) { // for N + 1 time
            console.log(`inside loop ${i}`); // for N time
        }
        Test(number - 1); // for N - 1time
    }
}

const number = 3;
Test(number);



/* So The Recurrence Relation => T(N) = 1 + N+1 + N + T(N-1) 
T(N) = T(N-1) + 2N + 2 = T (N-1) + N Only If N > 0 if N < 0 then T(N) = 1 or Constance

Complexity = O(N2) ( N square )
*/