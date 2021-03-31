genAlert = require("./native-alert.js").genAlert
restartAlert = require("./native-restart-alert.js").restartAlert

// console.log("it gens an alert")
// // genAlert("AAC");

// // , "RKT", "BAC", "PFE", "BNGO"]
// , "BAC", "PFE", "BNGO"
for (let symbol of ["RKT"]) {
    genAlert(symbol, (id) => {
        console.log(id)
        restartAlert(id)
    })
}


// genAlert("NYSE:AAC", "BATS:AAC");

