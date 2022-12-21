// Two Sum
// Codewars problem link https://www.codewars.com/kata/52c31f8e6605bcc646000082

// Example:
// target number = 15
// array = [12, 5, 32, 6, 10, 7]
// returns [1, 4]
// 1 is the index of 5 and 4 is the index of 10, 10 + 5 = target number

function two_sum(numbers, n) {
    let values = []

    for(let i=0; i<numbers.length; i++) {
        // a + b = n
        // To find (a) subtract (n) to (b) and to find (b) subtract (n) to (a) 
        let a = n - numbers[i]

        // 8 = 5 + 3; 5 = 8 - 3; 3 = 8 - 5

        if(values.includes(a)) {
            let index = values.indexOf(a)
            return [index, i]
        } else {
            values.push(numbers[i])
        }
    }

    return 0
}

let test_1 = [12, 5, 32, 6, 10, 7]
let target_1 = 15

let test_2 = [1, 2, 3]
let target_2 = 4

console.log(two_sum(test_1, target_1))
console.log(two_sum(test_2, target_2))