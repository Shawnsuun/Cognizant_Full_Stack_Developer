// Select color input
// Select size input

// When size is submitted by the user, call makeGrid()


function makeGrid() {
    //get height and width variables from html by id
    const ht = document.querySelector("#inputHeight").value;
    const wd = document.getElementById("inputWidth").value;

    //get table variable from from html by id
    const table = document.getElementById("pixelCanvas");
    //nested for loops to create grids
    for (var i = 0; i < ht; i ++) {
        //create a row element
        const row = document.createElement("tr");
        //append the row to table
        table.appendChild(row);
        for (var j = 0; j < wd; j ++) {
            //create a column element
            const col = document.createElement("td");
            //listen to click event, get color and update clicked grid's background color
            col.addEventListener("click", (event) => {
                const color = document.getElementById("colorPicker").value;
                event.target.style.backgroundColor = color;
            })
            //append the column element to row
            row.append(col);
        }
    }
}


function clearGrid() {
    //get table variable from from html by id
    const table = document.getElementById("pixelCanvas");
    //initialize row element
    let row = table.firstElementChild;
    //loop to remove all the row elements until row is empty
    while (row) {
        row.remove();
        row = table.firstElementChild;
    }
}

//listen to submit button, each submit will clear last grid and create a new one
document.addEventListener("submit", (event) => {
    event.preventDefault();
    clearGrid();
    makeGrid();
})
