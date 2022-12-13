function sumSeconds(inputs) {
    let first = Number(inputs[0])
    let second = Number(inputs[1])
    let third = Number(inputs[2])

    let sum = first + second + third
    let minutes = String(sum / 60)[0]
    let seconds = String(sum % 60).padStart(2, "0")

    console.log(`${minutes}:${seconds}`)

}

sumSeconds(["50",
"50",
"49"])

