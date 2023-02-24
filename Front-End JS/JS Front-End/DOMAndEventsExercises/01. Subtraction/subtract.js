function subtract() {
    let numberOne = document.getElementById("firstNumber").value
    let numberTwo = document.getElementById("secondNumber").value
    result = Number(numberOne) - Number(numberTwo)
    document.getElementById("result").innerHTML = result
}