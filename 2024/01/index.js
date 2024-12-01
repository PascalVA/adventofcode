var fs = require('fs');
var readline = require('readline');

async function parseFileContents(file) {
    var list1 = [];
    var list2 = [];

    const fileStream = fs.createReadStream(file);
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    for await(const line of rl) {
        var split = line.split(" ");

        list1.push(split[0]);
        list2.push(split[split.length-1]);
    }

    return [list1, list2];
}

parseFileContents('input.txt').then(function(lists) {
    var result = [];

    list1 = lists[0].sort();
    list2 = lists[1].sort();

    // [part 1]
    list1.forEach(function(item, index) {
        result.push(Math.abs(list2[index] - item));
    });

    console.log('Part 1:', result.reduce(function(accumulator, current) {
        return accumulator + current;
    }));

    // [part 2]
    // we create a lookup table to avoid using a nested for loop
    var countsMap = {}
    list2.forEach(function(item, index) {
        if (!countsMap[item]) {
            countsMap[item] = 0;
        }
        countsMap[item] += 1;
    });

    var result = 0
    list1.forEach(function(item, index) {
        if (countsMap[item]) {
            result = result + (item * countsMap[item])
        }
    });

    console.log('Part 2:', result);
});
