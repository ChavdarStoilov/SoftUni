function cats(arry) {
    
    class Cat {
        constructor(name, age) {
        this.name = name;
        this.age = age;
        }

        meow() {
            return `${this.name}, age ${this.age} says Meow`
        }
    }

    for (theCat in arry) {
        let [name, age] = arry[theCat].split(" ")
        const cats = new Cat(name, age)
        console.log(cats.meow())
    }
}


cats(['Mellow 2', 'Tom 5'])