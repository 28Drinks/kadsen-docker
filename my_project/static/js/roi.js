function toggleVisibility() {
    var x = document.getElementById("options-form");

    // var cssX = window.getComputedStyle(x);

    // let test = cssX.getPropertyValue('display');

    // console.log(test)

    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}