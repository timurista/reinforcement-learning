function choose(choices) {
    var index = Math.floor(Math.random() * choices.length);
    return choices[index];
}

const CHOICES = [
    "ArrowRight",
    "ArrowUp"
]

function getAction(choices=CHOICES) {
    return choose(choices)
}

module.exports = {
    choose,
    getAction
}
