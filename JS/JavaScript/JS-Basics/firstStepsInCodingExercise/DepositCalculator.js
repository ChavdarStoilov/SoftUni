function calculator(deposit) {

    let deposit_sum = parseFloat(deposit[0]);
    let deposit_time = parseInt(deposit[1]);
    let interest = parseFloat(deposit[2]) / 100;

    let full_interest = deposit_sum * interest

    let month_interest = full_interest / 12

    let result = deposit_sum + month_interest * deposit_time

    console.log(result);
}

calculator(["200 ","3 ","5.7 "]);