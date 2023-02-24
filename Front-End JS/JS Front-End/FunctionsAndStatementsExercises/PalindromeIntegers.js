function palindorme(arry) {

    for (index in arry) {
        let stringConventor = String(arry[index]);
        first = stringConventor[0];
        last = stringConventor.substr(-1);

        if (first == last) {
            console.log("true");
        }
        else {
            console.log("false");
        }
    }
    
}

palindorme([123,323,421,121]);