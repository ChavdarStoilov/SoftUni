function data(data){
    let first_name = data[0]
    let last_name = data[1]
    let age = data[2]
    let town = data[3]
    
    console.log('You are ' + first_name + ' ' + last_name + ', a ' + age + '-years old person from '+ town +'.');
} 

data(['Maria', 'Ivanova', 20, 'Sofia'])