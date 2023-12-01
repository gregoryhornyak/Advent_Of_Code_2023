// https://adventofcode.com/2023/day/1
// read in line by line
// for each line:
//  extract digits into a list
//  local_sum = 0th and last element of the list

//------------------------//

import fs from "fs"

const list_of_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
const main = (which_task) => {
    fs.readFile("input.txt", (err, data) => {
        if (err) throw err;
        var total = 0
        var lines = data.toString().split("\n") //list
        var local_list = []
        var local_sum = 0
        var temp_string = ""
        for (let i = 0; i < lines.length; i++) { // for each line
            console.log("--------------------\n" + lines[i])
            temp_string = "" // reset
            for (let scan = 0; scan < lines[i].length; scan++) { // for each letter
                temp_string += lines[i][scan]
                console.log(temp_string)
                // first scan if word in search_string
                for (const [key, value] of Object.entries(list_of_digits)) {
                    if (temp_string.includes(key)) {
                        // word found
                        console.log(key, value)
                        if (which_task == 2) { local_list.push(value) }
                        temp_string = temp_string.slice(-1) // reset search_string
                    }
                }
                // then scan if digit in search_string
                if (temp_string.slice(-1) >= '1' && temp_string.slice(-1) <= '9') {
                    // digit found
                    console.log(parseInt(temp_string.slice(-1)))
                    local_list.push(parseInt(temp_string.slice(-1)))
                    temp_string = "" // reset search_string
                }
            }
            // post fixing
            console.log("Original digits:", local_list)
            if (local_list.length == 1) {
                local_list.push(local_list[0])
                console.log("EXTENDED digits:", local_list)
            }
            local_sum = parseInt(local_list[0]) * 10 + parseInt(local_list.slice(-1))
            console.log("local sum:", local_sum)
            total += local_sum
            local_sum = 0
            local_list = [] // reset local list
        }
        console.log("\n\nTOTAL:", total)
    })
}

main(2)
