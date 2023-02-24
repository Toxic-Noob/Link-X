document.getElementById("copyme").innerText = "$ShowText$";
document.getElementById("copyme").addEventListener(
    "copy", function(e){
        e.clipboardData.setData("text/plain",
        "$CopyData$");
        e.preventDefault();
    }
)
