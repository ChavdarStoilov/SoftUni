function cooking(number, ...args) {
    result = number;
    for (i in args) {
        switch (args[i]) {
        case "chop":
            result /=  2;
            break;

        case "dice":
            result = Math.sqrt(result);

            break;

        case "spice":
            result += 1;

            break;

        case "bake":
            result *= 3;

            break;

        case "fillet":
            result -= (result * 0.20);

            break;
        }
        console.log(result);
    }
}

// cooking("32", "chop", "chop", "chop", "chop", "chop");
cooking('9', 'dice', 'spice', 'chop', 'bake', 'fillet')