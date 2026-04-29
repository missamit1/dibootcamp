const colorsContainer = document.querySelector(".colors");
const board = document.querySelector(".board");

let selectedColor = "black";
let isDrawing = false;

const colors = [
  "black",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "purple",
  "pink"
];

for (let color of colors) {
  const colorBox = document.createElement("div");

  colorBox.classList.add("color");
  colorBox.style.backgroundColor = color;

  colorBox.addEventListener("click", function () {
    selectedColor = color;
  });

  colorsContainer.appendChild(colorBox);
}

for (let i = 0; i < 400; i++) {
  const square = document.createElement("div");

  square.classList.add("square");

  square.addEventListener("mousedown", function () {
    isDrawing = true;
    square.style.backgroundColor = selectedColor;
  });

  square.addEventListener("mouseover", function () {
    if (isDrawing === true) {
      square.style.backgroundColor = selectedColor;
    }
  });

  board.appendChild(square);
}

document.addEventListener("mouseup", function () {
  isDrawing = false;
});
const resetBtn = document.querySelector("#resetBtn");

resetBtn.addEventListener("click", function () {
  const squares = document.querySelectorAll(".square");

  for (let square of squares) {
    square.style.backgroundColor = "white";
  }
});