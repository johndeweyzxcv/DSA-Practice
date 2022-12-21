// https://www.codewars.com/kata/52685f7382004e774f0001f7

function division_mod(dividend, divisor) {
    let result = {"quotient": 0, "remainder": 0}
    result["quotient"] = parseInt(dividend / divisor)
    result["remainder"] = (dividend - (result["quotient"] * divisor))
    return result
}

function clean_format(format_to_clean) {
    let final_result = ""

    for(let i=0; i<format_to_clean.length; i++) {
        var convert_string = format_to_clean[i].toString()
        var new_string;

        if(convert_string.length == 1) {
            new_string = "0"
            new_string += convert_string
        } else {
            new_string = convert_string
        }

        if(i == format_to_clean.length - 1) {
            final_result += new_string
        } else {
            final_result += new_string + ":"
        }
    }

    return final_result
}

function make_readable(seconds) {
    if(seconds == 0) {
        return "00:00:00"
    }

    let formats = [0, 0, 0]
    for(let i=0; i<formats.length; i++) {
        if(seconds < 60 || i == 2) {
            formats[i] = seconds
            break
        } else if(seconds >= 60) {
            let div_mod_result = division_mod(seconds, 60)
            let quotient_result = div_mod_result.quotient
            let remainder_result = div_mod_result.remainder
            
            formats[i] = remainder_result
            seconds = quotient_result
        }
    }

    formats.reverse()
    let finalize_format = clean_format(formats)
    return finalize_format
}

console.log(make_readable(4728))

// let x = 5
// let y = 33
// let final_result = division_mod(x, y)
// console.log("Quotient -> " + final_result.quotient)
// console.log("Remainder -> " + final_result.remainder)