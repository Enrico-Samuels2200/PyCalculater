let list = [];
let display_equation = "";
let screen = document.getElementById("display");

// Used to add a value to display_equation for use in the display() function.
function update() {
    display_equation = "";

    // Every item in the array list will get added to display_equation.
    list.forEach((item) => {
        display_equation += item + " ";
    })
}

// Displays the values on the calculator string. 
function display(result) {
    let value = event.target.id

    // If the user enters 'c' then it'll remove the last value in the array and update display_equation.
    if(value === "c") {
        list.splice(-1, 1);
        update()
    }
    // Pushes every other value to the array list.
    else {
       list.push(value)
       update()
    }
    // Updates the calculator screen.
    screen.value = display_equation;
}

// Async function is used to retrieve data from the backend(Python) script.
async function get() {
    // result store the value we receive from the python script.
    result = await eel.start(display_equation)();
    list = []
    list.push(result)
    update()
    screen.value = display_equation;
}