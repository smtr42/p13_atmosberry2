

function tokenWarning() {
    let x = document.getElementById("warning-message");

    if (x.style.display === "none") {
      x.style.display = "block";
    } 

    let y = document.getElementById("warning-button");
    if (y.style.display !== "none") {
        y.style.display = "none";
      } 
    
    let z = document.getElementById("real");
    if (z.style.display === "none") {
        z.style.display = "block";
    }
  }