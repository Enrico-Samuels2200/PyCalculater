let list = [];
let display_equation = "";
let len = 0;

function display(val) {
    let screen = document.getElementById("display");

    if(list.length === 0) {
        list.push(val)   
    }
    else {
        list.push(val)
    }

    display_equation += list[len] + " ";

    screen.value = display_equation;
    len += 2;
}

function get_number() {
    let button = event.target.id
    display(button)
}